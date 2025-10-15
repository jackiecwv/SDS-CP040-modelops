import pickle
import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
import os

os.chdir(os.path.dirname(__file__))

# Load the pretrained model
model = joblib.load("model.pkl")

# Create FastAPI app
app = FastAPI(title="Car Price Prediction API", version="1.0.0")

# --- Pydantic model for input ---
class CarInput(BaseModel):
    Manufacturer: str = Field(..., example="Toyota")
    Model: str = Field(..., example="Corolla")
    Fuel_type: str = Field(..., alias="Fuel type", example="Petrol")
    Engine_size: float = Field(..., alias="Engine size", example=1.8)
    Year_of_manufacture: int = Field(..., alias="Year of manufacture", example=2019)
    Mileage: float = Field(..., example=45000)


# --- Endpoints ---
@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/metadata")
def get_metadata():
    return {
        "model_info": "Car Price Prediction Model",
        "model": "model.pkl",
        "version": "1.0.0",
        "features": [
            "Manufacturer", "Model", "Fuel_type", "Engine_size",
            "Year_of_manufacture", "Mileage"
        ],
    }


@app.post("/predict")
def predict_car_price(payload: CarInput):
    payload_dict = payload.model_dump(by_alias=True)

    manufacturer = payload_dict["Manufacturer"].strip()
    model_name = payload_dict["Model"].strip()
    fuel = payload_dict["Fuel type"].strip()
    engine = float(payload_dict["Engine size"])
    year = int(payload_dict["Year of manufacture"])
    mileage = float(payload_dict["Mileage"])

    CURRENT_YEAR = 2025
    age = max(CURRENT_YEAR - year, 0)
    mileage_per_year = mileage / max(age, 1)
    vintage = int(age >= 20)

    row = {
        "Manufacturer": manufacturer,
        "Model": model_name,
        "Fuel type": fuel,
        "Engine size": engine,
        "Year of manufacture": year,
        "Mileage": mileage,
        "age": age,
        "mileage_per_year": mileage_per_year,
        "vintage": vintage,
    }

    df = pd.DataFrame([row])
    prediction = model.predict(df)[0]

    return {"predicted_price_gbp": float(prediction)}


@app.get("/", response_class=HTMLResponse)
def read_root():
    html_path = os.path.join("templates", "index.html")
    with open(html_path, "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

