# Deployment Guide

This guide covers deploying the Car Price Prediction API to Render or Hugging Face Spaces.

## Prerequisites

- Docker installed locally (for testing)
- Git repository with your code
- Model file (`model.pkl`) - see note below about model location

## Important: Model File

✅ The model file is **automatically included** in the Docker image during build. The Dockerfile copies the model from `../../../../models/model.pkl` and sets the `MODEL_PATH` environment variable to `/app/model.pkl`.

**No additional configuration needed** - the model is ready to use out of the box!

## Deployment Options

---

## 1. Deploy to Render

### Step 1: Prepare Your Repository
Ensure your repository contains:
- `Dockerfile`
- `.dockerignore`
- `main.py`
- `index.html`
- `requirements.txt`
- Access to `../../../../models/model.pkl` (relative to your project directory)

### Step 2: Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up or log in with GitHub

### Step 3: Create New Web Service
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Configure the service:
   - **Name**: `car-price-prediction-api`
   - **Environment**: `Docker`
   - **Region**: Choose closest to your users
   - **Branch**: `main` (or your branch)
   - **Instance Type**: `Free` or `Starter`

### Step 4: Environment Variables
Render automatically provides these:
- `PORT`: Port to run the application (handled automatically by the Dockerfile)

No manual configuration needed - the model is included in the Docker image!

### Step 5: Deploy
1. Click "Create Web Service"
2. Render will automatically build and deploy your Docker container
3. Wait for deployment to complete (first build may take 5-10 minutes)

### Step 6: Access Your API
- Your API will be available at: `https://your-service-name.onrender.com`
- Test the health endpoint: `https://your-service-name.onrender.com/health`

---

## 2. Deploy to Hugging Face Spaces

### Step 1: Create Hugging Face Account
1. Go to [huggingface.co](https://huggingface.co)
2. Sign up or log in

### Step 2: Create New Space
1. Click your profile → "New Space"
2. Configure:
   - **Space name**: `car-price-prediction`
   - **License**: Choose appropriate license
   - **SDK**: Select "Docker"
   - **Visibility**: Public or Private

### Step 3: Push Your Code
```bash
# Clone your new space
git clone https://huggingface.co/spaces/YOUR_USERNAME/car-price-prediction
cd car-price-prediction

# Copy your files
cp /path/to/your/Dockerfile .
cp /path/to/your/.dockerignore .
cp /path/to/your/main.py .
cp /path/to/your/index.html .
cp /path/to/your/requirements.txt .
# Copy templates directory if exists
cp -r /path/to/your/templates .
# Ensure model is accessible at ../../../../models/model.pkl relative to Dockerfile

# Commit and push
git add .
git commit -m "Initial deployment"
git push
```

### Step 4: Configure Space (if needed)
Create a `README.md` in your Space with frontmatter:

```yaml
---
title: Car Price Prediction API
emoji: 🚗
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---
```

### Step 5: Wait for Build
Hugging Face will automatically build your Docker container. Check the "Logs" tab for progress.

### Step 6: Access Your API
- Your API will be available at: `https://huggingface.co/spaces/YOUR_USERNAME/car-price-prediction`
- API endpoint: `https://YOUR_USERNAME-car-price-prediction.hf.space`

---

## Testing Locally with Docker

Before deploying, test your Docker setup locally:

```bash
# Build the image (model is included automatically)
docker build -t car-price-api .

# Run the container
docker run -p 8000:8000 car-price-api

# Test the API
curl http://localhost:8000/health
curl http://localhost:8000/ready
```

Open your browser to `http://localhost:8000` to see the interface.

---

## API Endpoints

Once deployed, your API provides:

- `GET /` - Web interface
- `GET /health` - Health check
- `GET /ready` - Readiness check (model loaded)
- `GET /features` - Available feature values
- `GET /metadata` - Model metadata
- `POST /predict` - Make predictions

### Example Prediction Request

```bash
curl -X POST "https://your-api-url.com/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "Manufacturer": "BMW",
    "Model": "X3",
    "Fuel type": "Diesel",
    "Engine size": 2.0,
    "Year of manufacture": 2018,
    "Mileage": 45000
  }'
```

---

## Troubleshooting

### Model Not Found
- Ensure the model exists at `../../../../models/model.pkl` relative to the Dockerfile when building
- Check Docker build logs to verify the model was copied successfully
- Verify the `/ready` endpoint returns `{"model_loaded": true}`

### Port Issues
- Render: Uses `PORT` environment variable automatically
- Hugging Face: Defaults to port 8000
- The Dockerfile handles this with `${PORT:-8000}`

### Build Failures
- Check Docker build logs
- Verify all files are present
- Ensure requirements.txt has correct versions
- Check `.dockerignore` isn't excluding necessary files

### Memory Issues (Free Tier)
- Reduce model size if possible
- Use smaller instance type on Render
- Consider lazy loading for heavy resources

---

## Cost Considerations

### Render
- **Free Tier**: 750 hours/month, sleeps after inactivity
- **Starter**: $7/month, always on
- **Standard**: $25/month, more resources

### Hugging Face
- **Free**: Limited resources, may be slow
- **Upgrade**: Contact Hugging Face for enterprise options

---

## Production Recommendations

1. **Model Management**: Consider using a model versioning system or cloud storage
2. **Monitoring**: Add logging and monitoring (e.g., Sentry, LogRocket)
3. **Security**:
   - Restrict CORS origins in `main.py:117`
   - Add API authentication if needed
   - Use HTTPS (both platforms provide this)
4. **Performance**:
   - Use caching for predictions
   - Consider adding a CDN for static assets
   - Monitor response times

---

## Support

- **Render Docs**: https://render.com/docs
- **Hugging Face Docs**: https://huggingface.co/docs/hub/spaces
- **FastAPI Docs**: https://fastapi.tiangolo.com

Happy Deploying! 🚀
