# 🔴 Advanced Track — ModelOps

## 🎯 Objectives

Learn how to build and deploy a **production-grade ML service** with a proper backend and DevOps practices.

* Develop a **FastAPI backend** (with minimal frontend if desired)
* **Containerize** the application with Docker
* Set up a **basic CI/CD pipeline** with GitHub Actions
* Deploy the service to the cloud (Hugging Face Spaces, Render, AWS/GCP)


## 📅 Weekly Breakdown

### ✅ Week 1: Setup + FastAPI Service + Local Inference

* Import the provided **pre-trained model artifact (`model.pkl`)**, which includes preprocessing and the trained estimator
* Build a **FastAPI backend** with endpoints:

  * `/health` → check service health
  * `/predict` → accept model input and return prediction
  * `/metadata` → return model version info
* Test locally with `uvicorn` to confirm requests flow end-to-end
* **Deliverables**:

  * `main.py` FastAPI service
  * Local run verified with sample API calls


### ✅ Week 2: Containerization (Docker)

* Write a **Dockerfile** for the FastAPI application
* Add `docker-compose.yml` (optional) for easier local testing
* Test locally by building and running the container, verifying predictions work
* **Deliverables**:

  * Working Docker image
  * README updated with Docker quickstart


### ✅ Week 3: Deployment + CI/CD

* Create a **GitHub Actions workflow** to:

  * Run tests on each commit
  * Build the Docker image
  * Optionally push to Docker Hub or GitHub Container Registry
* Choose a deployment option:

  * **Hugging Face Spaces**
  * **Render** (web service)
  * **AWS ECS/Fargate** or **GCP Cloud Run**
* Configure environment variables/secrets for deployment
* Deploy and verify the service is accessible via a public URL
* **Deliverables**:

  * Working `.github/workflows/ci.yml`
  * Public deployment link
  * Updated README with deployment instructions


## 🛠️ Technical Requirements

* **Backend**: FastAPI, Uvicorn
* **Validation**: Pydantic models
* **Containerization**: Docker, docker-compose
* **CI/CD**: GitHub Actions
* **Deployment**: Hugging Face Spaces / Render / AWS ECS / GCP Cloud Run
* **Logging**: Python `logging`


## 📋 Model Features

These are the **inputs required by the model** and their data types:

* `datePostedString` (str)
* `is_bankOwned` (int)
* `is_forAuction` (int)
* `city` (str)
* `yearBuilt` (int)
* `zipcode` (float)
* `longitude` (float)
* `latitude` (float)
* `livingArea` (float)
* `bathrooms` (float)
* `bedrooms` (float)
* `buildingArea` (float)
* `parking` (int)
* `garageSpaces` (float)
* `hasGarage` (int)
* `levels` (str)
* `pool` (int)
* `spa` (int)
* `isNewConstruction` (int)
* `hasPetsAllowed` (int)
* `homeType` (str)
* `county` (str)


## 🎯 End Goal

By the end of this track, you’ll have a **production-ready ML microservice**:

* A FastAPI backend exposing prediction endpoints
* Dockerized and CI/CD-enabled
* Deployed to a cloud platform with a public URL
* Documented with usage instructions and demo links

This will clearly demonstrate to recruiters and hiring managers that you can **deploy and operate ML models in real-world environments**.
