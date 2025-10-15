from fastapi import FastAPI
import joblib
import pandas as pd

# Load the pre-trained model
model = joblib.load('models/model.pkl')

app = FastAPI()

# Define a health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Define a prediction endpoint
@app.post("/predict")
def predict_car_price(payload_dict: dict):
    # Extract features from input dictionary
    manufacturer = str(payload_dict["Manufacturer"]).strip()
    model_name = str(payload_dict["Model"]).strip()
    fuel = str(payload_dict["Fuel type"]).strip()
    engine = float(payload_dict["Engine size"])
    year = int(payload_dict["Year of manufacture"])
    mileage = float(payload_dict["Mileage"])
    
    # Derived features (training pipeline expected these)
    CURRENT_YEAR = 2025
    age = max(CURRENT_YEAR - year, 0)
    mileage_per_year = mileage / max(age, 1)
    vintage = int(age >= 20)

    # Create single-row dataframe with ALL columns needed
    row = {
        "Manufacturer": manufacturer,
        "Model": model_name,
        "Fuel type": fuel,
        "Engine size": engine,
        "Year of manufacture": year,
        "Mileage": mileage,
        # derived:
        "age": age,
        "mileage_per_year": mileage_per_year,
        "vintage": vintage,
    }
    df = pd.DataFrame([row])

    # Make a prediction using the pre-trained model
    prediction = model.predict(df)[0]
    
    # Return the prediction as a JSON response
    return {
        # "input_features": row,
        "predicted_price": round(float(prediction), 2)
    }

