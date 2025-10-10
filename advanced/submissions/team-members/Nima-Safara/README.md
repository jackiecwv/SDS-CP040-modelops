# Car Price Prediction Web Application

This is a full-stack web application that predicts car prices using a pre-trained XGBoost model, served via FastAPI and an interactive HTML frontend.

## Features

### Backend
- **FastAPI** with automatic API documentation (`/docs`, `/redoc`)
- **Robust error handling** with HTTPException and detailed logging
- **Health & readiness checks** (`/health`, `/ready`) for Kubernetes/Docker deployments
- **Environment-based model loading** with `MODEL_PATH` override support
- **Pydantic v2 validation** with field constraints (engine size > 0, year ≥ 1980, etc.)
- **Comprehensive logging** for debugging and monitoring

### Frontend
- **Fully dropdown-based interface** - no typing required, prevents invalid inputs
- **Smart cascading dropdowns** - model options update based on manufacturer selection
- **Model-specific filtering** - fuel types and engine sizes filter based on car model
- **Custom mileage input** - option to enter exact mileage values
- **Enhanced error handling** - user-friendly error messages with actionable feedback
- **API documentation link** - quick access to interactive API docs
- **Responsive design** - works on desktop, tablet, and mobile

## Project Structure
```
Nima-Safara/
├── main.py            # FastAPI backend application
├── index.html         # Frontend user interface
├── requirements.txt   # Python dependencies
└── README.md          # Documentation
```

Model file (outside this folder): `SDS-CP040-modelops/models/model.pkl`

## Setup
1) Create a virtual environment and install dependencies
```
pip install -r requirements.txt
```

2) Optional: set a custom model path
```
# Windows (PowerShell)
$Env:MODEL_PATH = "<ABSOLUTE_PATH_TO>/models/model.pkl"
# macOS/Linux
export MODEL_PATH="<ABSOLUTE_PATH_TO>/models/model.pkl"
```

3) Run the application
```
python main.py
```
The app runs on http://localhost:8000

## Using the App

### Web Interface
1) Open your browser at `http://localhost:8000`
2) Select car details using the dropdowns:
   - **Manufacturer** → **Model** (cascading dropdown)
   - **Fuel Type** (filtered based on model)
   - **Engine Size** (filtered based on model)
   - **Year of Manufacture** (2000-2025)
   - **Mileage** (preset options or custom input)
3) Click "Predict Price"
4) The predicted price displays in GBP (£)

### Interactive API Documentation
- **Swagger UI**: Visit `http://localhost:8000/docs` to:
  - View all endpoints and their schemas
  - Test API calls interactively with "Try it out"
  - See request/response examples
  - Copy curl commands

- **ReDoc**: Visit `http://localhost:8000/redoc` for:
  - Clean, readable documentation
  - Printer-friendly format
  - Easy navigation

## API Endpoints

| Endpoint | Method | Description | Response |
|----------|--------|-------------|----------|
| `/` | GET | Serves the HTML frontend | HTML page |
| `/health` | GET | Liveness probe for K8s/Docker | `{ "status": "healthy" }` |
| `/ready` | GET | Readiness probe (checks model loaded) | `{ "model_loaded": true\|false }` |
| `/features` | GET | Returns available feature values for dropdowns | Feature lists and ranges |
| `/metadata` | GET | Model information and feature schema | Model metadata |
| `/predict` | POST | Predicts car price | `{ "predicted_price_gbp": float }` |
| `/docs` | GET | Interactive API documentation (Swagger UI) | Auto-generated docs |
| `/redoc` | GET | Alternative API documentation (ReDoc) | Auto-generated docs |

### Example: Making a Prediction

**Request** (POST `/predict`):
```json
{
  "Manufacturer": "Toyota",
  "Model": "RAV4",
  "Fuel type": "Hybrid",
  "Engine size": 2.5,
  "Year of manufacture": 2020,
  "Mileage": 30000
}
```

**Success Response** (200):
```json
{
  "predicted_price_gbp": 25430.75
}
```

**Error Responses**:
- **503** - Model not loaded:
  ```json
  {
    "detail": "Model not loaded. Please check server logs and try again later."
  }
  ```
- **500** - Prediction error:
  ```json
  {
    "detail": "Prediction failed: <error details>"
  }
  ```
- **422** - Validation error (invalid input):
  ```json
  {
    "detail": [
      {
        "loc": ["body", "Engine size"],
        "msg": "ensure this value is greater than 0",
        "type": "value_error.number.not_gt"
      }
    ]
  }
  ```

## Technical Details

### Model Features
The model uses the following features:
- **Input**: Manufacturer, Model, Fuel type, Engine size, Year of manufacture, Mileage
- **Derived**: Age (current year - year of manufacture), Mileage per year, Vintage flag (age ≥ 20 years)
- **Current year**: Set to 2025 for age calculations

### Supported Values
The model was trained on these specific values (extracted from OneHotEncoder categories):
- **Manufacturers**: BMW, Ford, Porsche, Toyota, VW
- **Models**:
  - BMW: M5, X3, Z4
  - Ford: Fiesta, Focus, Mondeo
  - Porsche: 718 Cayman, 911, Cayenne
  - Toyota: Prius, RAV4, Yaris
  - VW: Golf, Passat, Polo
- **Fuel Types**: Diesel, Hybrid, Petrol

### Error Handling
- **Backend**: HTTPException with detailed error messages and logging
- **Frontend**: User-friendly error messages with specific guidance:
  - Model loading issues
  - Invalid inputs
  - Network errors
  - Server errors with details

### Deployment Notes
- Frontend uses **relative URLs** for API calls, making it proxy-friendly
- **CORS is open** (`allow_origins=["*"]`) - restrict in production
- **Health checks** available for container orchestration
- **Environment variables** supported for flexible deployment
- Dependencies have **version ranges** to avoid breaking changes

## Troubleshooting

### Model Loading Issues
If you see "Model not loaded" errors:
1. Check the model path: `C:\...\SDS-CP040-modelops\models\model.pkl`
2. Set `MODEL_PATH` environment variable if model is elsewhere
3. Check server logs for detailed error messages

### Version Warnings
You may see sklearn version warnings (trained on 1.7.2, using 1.6.1):
- These are informational warnings only
- The model will still work correctly
- To eliminate warnings: `pip install --upgrade scikit-learn`

### Port Already in Use
If port 8000 is busy:
```python
# In main.py, change:
uvicorn.run(app, host="0.0.0.0", port=8001)  # Use different port
```

## Future Enhancements
- [ ] Add authentication/authorization
- [ ] Implement rate limiting
- [ ] Add prediction history and analytics
- [ ] Support for batch predictions
- [ ] Model versioning and A/B testing
- [ ] Prometheus metrics endpoint
- [ ] Docker containerization
- [ ] Kubernetes deployment manifests
