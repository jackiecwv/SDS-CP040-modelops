# 🟢 Beginner Track — ModelOps

## 🎯 Objectives

Learn how to take a **ready-made ML model** and make it accessible through a simple user interface. You’ll build a lightweight app, containerize it, and deploy it to the cloud.

* Build a **Streamlit or Gradio UI** to interact with a pre-trained model
* **Containerize** the app with Docker
* **Deploy** it to Hugging Face Spaces for a live, shareable demo


## 📅 Weekly Breakdown

### ✅ Week 1: Setup + UI + Local Inference

* Import the provided **pre-trained model artifact (`model.pkl`)**, which includes preprocessing and trained estimator for car price prediction
* Build a **Streamlit or Gradio interface** that:

  * Accepts user input for all features required by the model
  * Ensures inputs are collected in the correct format (numeric, categorical, boolean, etc.)
  * Displays the model's predicted output back to the user (estimated car price in GBP)
* Test locally to confirm the full pipeline runs end-to-end (input → model → prediction → UI output)
* **Deliverables**:

  * `app.py` (Streamlit or Gradio)
  * Local run verified with screenshot/GIF of working UI


### ✅ Week 2: Containerization + Deployment (Hugging Face Spaces)

* Write a **Dockerfile** to package the app and model into a container
* Add instructions to the README for building and running the container locally
* Create a **Hugging Face Space** for the project
* Push the repo to Hugging Face with `requirements.txt` and app files
* Verify the app runs fully in the cloud
* **Deliverables**:

  * Working Docker image (runs locally)
  * Public Space URL
  * README updated with build commands and demo link


### ✅ Week 3: Cloud Demo & Sharing

* Polish the Hugging Face Space (e.g., title, description, example input)
* Add the Space link and badge to the README for easy access
* Record a short demo (GIF or screen recording) of your app running in the cloud
* **Deliverables**:

  * Public Hugging Face Space badge + link in README
  * Demo GIF/screenshot


## 🛠️ Technical Requirements

* **UI**: Streamlit ≥1.30 or Gradio ≥4
* **Model runtime**: Provided `model.pkl` (scikit-learn pipeline with preprocessing + model)
* **Packaging**: pip + `requirements.txt`
* **Containerization**: Docker
* **Deployment**: Hugging Face account + Spaces


## 📋 Model Features

These are the **inputs required by the car pricing model** and their data types. The model predicts car prices based on the following features:

### 📊 **Input Features**

* **manufacturer** → `string` - The brand or company producing the vehicle (e.g., Ford, Toyota, Porsche)

* **model** → `string` - The specific model of the car (e.g., Fiesta, RAV4, Polo)

* **engine_size** → `float` - Engine capacity in liters (e.g., 1.0, 2.0, 4.0)

* **fuel_type** → `string` - Type of fuel used by the car (Petrol, Diesel, Hybrid, Electric)

* **year_of_manufacture** → `int` - Year the vehicle was manufactured

* **mileage** → `int` - Total distance the car has traveled, measured in miles

### 🎯 **Target Variable**

* **price** → `float` - Sale price of the car in GBP (British Pounds)

## 🎯 End Goal

By the end of this track, you’ll have a **live, shareable ML demo app** with a simple UI, containerized in Docker, and deployed to Hugging Face Spaces — an ideal portfolio-ready project showing you can take a model into production.
