"""
With this code, the goal is to demonstrate the process of deploying machine learning models to a production environment.
"""
# Import necessary libraries
import joblib
import pandas as pd
from pydantic import BaseModel, Field, ConfigDict
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from pathlib import Path
import logging
import json

# Define a Pydantic model for the input payload
class CarFeatures(BaseModel):
    Manufacturer: str
    Model: str
    Fuel_type: str = Field(..., alias="Fuel type")
    Engine_size: float = Field(..., alias="Engine size", gt=0)
    Year_of_manufacture: int = Field(
        ..., alias="Year of manufacture", ge=1980
    )
    Mileage: float = Field(..., ge=0)

    # Pydantic v2 configuration: allow population by field name when alias exists
    model_config = ConfigDict(populate_by_name=True)

CURRENT_YEAR = 2025

# Create FastAPI app
app = FastAPI(title="Car Price Prediction API", version="1.0.0")

# Add CORS middleware to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("car-price-api")

# Resolve and load model robustly
model = None

def resolve_model_path() -> Path:
    """Resolve model path via env var MODEL_PATH or relative to this file."""
    env_path = os.getenv("MODEL_PATH")
    if env_path:
        return Path(env_path).expanduser().resolve()
    # Repo root is four levels up from this file: .../SDS-CP040-modelops
    repo_root = Path(__file__).resolve().parents[4]
    return repo_root / "models" / "model.pkl"

@app.on_event("startup")
def load_model_on_startup():
    global model
    model_path = resolve_model_path()
    try:
        model = joblib.load(model_path)
        logger.info(f"Model loaded from: {model_path}")
    except Exception as e:
        logger.error(f"Failed to load model from {model_path}: {e}")
        model = None

# Root endpoint - serve the HTML page
@app.get("/")
def read_root():
    return FileResponse(str((Path(__file__).parent / "index.html").resolve()))

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Readiness endpoint (verifies model is loaded)
@app.get("/ready")
def readiness_check():
    return {"model_loaded": model is not None}

# Get available feature values from the model
@app.get("/features")
def get_available_features():
    """Return valid values for each feature; falls back to defaults if unavailable."""
    # Defaults
    engine_sizes = [
        0.8, 1.0, 1.2, 1.4, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.5,
        2.7, 3.0, 3.5, 4.0, 4.5, 5.0
    ]
    years = list(range(2000, CURRENT_YEAR + 1))[::-1]
    mileage_options = [
        0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000,
        60000, 70000, 80000, 90000, 100000, 120000, 150000, 180000, 200000,
        250000, 300000
    ]

    manufacturers = ["BMW", "Ford", "Porsche", "Toyota", "VW"]
    models = ["M5", "X3", "Z4", "Fiesta", "Focus", "Mondeo", "718 Cayman", "911", "Cayenne", "Prius", "RAV4", "Yaris", "Golf", "Passat", "Polo"]
    fuel_types = ["Diesel", "Hybrid", "Petrol"]
    model_by_manufacturer = {}

    # Try to extract from the trained model if available
    try:
        if model is not None and hasattr(model, "named_steps"):
            preprocessor = model.named_steps.get("preprocessor")
            if preprocessor is not None and hasattr(preprocessor, "named_transformers_"):
                cat_transformer = preprocessor.named_transformers_.get("cat")
                if cat_transformer is not None and hasattr(cat_transformer, "categories_"):
                    categories = cat_transformer.categories_
                    manufacturers = sorted(categories[0].tolist())
                    models = sorted(categories[1].tolist())
                    fuel_types = sorted(categories[2].tolist())
        # Optionally enrich with a mapping of Manufacturer -> [Models]
        # If a JSON file sits next to the model (e.g., models_map.json), load it
        try:
            model_path = resolve_model_path()
            meta_path = model_path.parent / "models_map.json"
            if meta_path.exists():
                with open(meta_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if isinstance(data, dict):
                    model_by_manufacturer = {str(k): list(v) for k, v in data.items()}
        except Exception as e:
            logger.warning(f"Could not load models_map.json: {e}")
    except Exception as e:
        logger.warning(f"Falling back to default features due to error: {e}")

    return {
        "Manufacturer": manufacturers,
        "Model": models,
        "Fuel_type": fuel_types,
        "Engine_sizes": engine_sizes,
        "Years": years,
        "Mileage_options": mileage_options,
        "ModelByManufacturer": model_by_manufacturer,
    }

# Model metadata endpoint
@app.get("/metadata")
def get_metadata():
    return {
        "model_info": "Car Price Prediction Model",
        "model": "model.pkl",
        "version": "1.0.0",
        "features": [
            "manufacturer", "model", "engine_size", "fuel_type",
            "year_of_manufacture", "mileage"
        ]
    }       

# Prediction endpoint
@app.post("/predict")
def predict_car_price(payload: CarFeatures):
    """
    Predict car price based on provided features.

    Raises:
        HTTPException: 503 if model is not loaded
        HTTPException: 500 if prediction fails
    """
    # Check if model is loaded
    if model is None:
        logger.error("Prediction attempted but model is not loaded")
        raise HTTPException(
            status_code=503,
            detail="Model not loaded. Please check server logs and try again later."
        )

    try:
        # Pydantic model handles data extraction and validation

        # Derived features (training pipeline expected these)
        age = max(CURRENT_YEAR - payload.Year_of_manufacture, 0)
        mileage_per_year = payload.Mileage / max(age, 1)
        vintage = int(age >= 20)

        # Create single-row dataframe with ALL columns needed
        row = {
            "Manufacturer": payload.Manufacturer,
            "Model": payload.Model,
            "Fuel type": payload.Fuel_type,
            "Engine size": payload.Engine_size,
            "Year of manufacture": payload.Year_of_manufacture,
            "Mileage": payload.Mileage,
            # derived:
            "age": age,
            "mileage_per_year": mileage_per_year,
            "vintage": vintage,
        }
        row_df = pd.DataFrame([row])

        # Make prediction using the pre-trained model
        prediction = model.predict(row_df)[0]

        logger.info(f"Prediction successful for {payload.Manufacturer} {payload.Model}: £{prediction:.2f}")

        # Return the prediction result
        return {"predicted_price_gbp": round(float(prediction), 2)}

    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )

if __name__ == "__main__":
    # This block allows you to run the app directly for testing
    uvicorn.run(app, host="0.0.0.0", port=8000)
