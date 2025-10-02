# 🟢 Beginner Track — ModelOps

## 🎯 Objectives

Learn how to take a **ready-made ML model** and make it accessible through a simple user interface. You’ll build a lightweight app, containerize it, and deploy it to the cloud.

* Build a **Streamlit or Gradio UI** to interact with a pre-trained model
* **Containerize** the app with Docker
* **Deploy** it to Hugging Face Spaces for a live, shareable demo


## 📅 Weekly Breakdown

### ✅ Week 1: Setup + UI + Local Inference

* Import the provided **pre-trained model artifacts (`luxury_model.pkl` and `non_luxury_model.pkl`)**, which include preprocessing and trained estimators for luxury and non-luxury car price prediction
* Build a **Streamlit or Gradio interface** that:

  * Accepts user input for all features required by the model
  * Ensures inputs are collected in the correct format (numeric, categorical, boolean, etc.)
  * Displays the model’s predicted output back to the user (e.g., estimated price)
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
* **Model runtime**: Two provided models - `luxury_model.pkl` and `non_luxury_model.pkl` (scikit-learn pipelines with preprocessing + models)
* **Packaging**: pip + `requirements.txt`
* **Containerization**: Docker
* **Deployment**: Hugging Face account + Spaces


## 📋 Model Features

These are the **inputs required by the car pricing models** and their data types. The models predict car prices based on various features:

### 📊 **Categorical Features & Their Unique Values**

* **brand** → `['Ford', 'Honda', 'Hyundai', 'Kia', 'Nissan', 'Toyota', 'Audi', 'BMW', 'Chevrolet', 'Lexus', 'Mercedes Benz'] ... (+1 more)`
  
* **model** → Model options vary by brand:
  * **Toyota**: `['4Runner', '86', 'Alphard', 'Aurion', 'Avalon', 'Avanza', 'C-HR', 'Camry', 'Celica', 'Coaster', 'Corolla', 'Corolla Cross', 'Cressida', 'Crown', 'Echo', 'FJ Cruiser', 'Fortuner', 'Granvia', 'Hiace', 'Highlander', 'Hilux', 'Innova', 'Land Cruiser', 'Land Cruiser 70', 'Land Cruiser 76 series', 'Land Cruiser 79 series', 'Other', 'Pickup', 'Prado', 'Previa', 'Prius', 'Raize', 'Rav 4', 'Rush', 'Scion', 'Sequoia', 'Sienna', 'Supra', 'Tacoma', 'Tundra', 'Urban Cruiser', 'Veloz', 'Venza', 'Yaris', 'Zelas']`
  * **Honda**: `['Accord', 'CR-V', 'City', 'Civic', 'Crosstour', 'ENS1', 'HR-V', 'Jazz', 'MR-V', 'Odyssey', 'Odyssey J', 'Other', 'Pilot', 'S2000', 'ZR-V']`
  * **Nissan**: `['300ZX', '350Z', '370z', '400Z', 'Altima', 'Armada', 'GT-R', 'Juke', 'Kicks', 'Leaf', 'Maxima', 'Micra', 'Murano', 'Navara', 'Other', 'Pathfinder', 'Patrol', 'Patrol Pickup', 'Pickup', 'Qashqai', 'Quest', 'Rogue', 'Sentra', 'Sunny', 'Tiida', 'Titan', 'Urvan', 'Van', 'Versa', 'X-Trail', 'Xterra', 'Z']`
  * **Hyundai**: `['Accent', 'Avanti', 'Azera', 'Centennial', 'Coupe', 'Creta', 'Elantra', 'Genesis', 'Getz', 'Grand Santa Fe', 'Grand i10', 'Grandeur', 'H 100', 'H1', 'Kona', 'Matrix', 'Other', 'Palisade', 'Porter', 'Santa Fe', 'Sonata', 'Staria', 'Tucson', 'Veloster', 'Venue', 'Verna', 'i10', 'i20', 'i30']`
  * **KIA**: `['Bongo', 'Cadenza', 'Carens', 'Carnival', 'Cerato', 'EV6', 'Forte', 'K3', 'K5', 'K8', 'K900', 'Mohave', 'Niro', 'Oprius', 'Optima', 'Other', 'Pegas', 'Picanto', 'Quoris', 'Rio', 'Sedona', 'Seltos', 'Sonet', 'Sorento', 'Soul', 'Sportage', 'Stinger', 'Telluride']`
  * **Ford**: `['Bronco', 'Crown Victoria', 'Ecosport', 'Edge', 'Escape', 'Escort', 'Everest', 'Expedition', 'Explorer', 'F-Series Pickup', 'Fiesta', 'Figo', 'Flex', 'Focus', 'Fusion', 'GT', 'Mondeo', 'Mustang', 'Mustang Mach-E', 'Other', 'Pickup', 'Ranger', 'Shelby Cobra', 'Super Duty', 'Taurus', 'Territory', 'Thunderbird', 'Tourneo', 'Transit']`
  * **Chevrolet**: `['Apache', 'Avalanche', 'Aveo', 'Blazer', 'Camaro', 'Caprice', 'Captiva', 'Chevelle', 'Colorado', 'Corvette', 'Cruze', 'Epica', 'Equinox', 'Express', 'Groove', 'Impala', 'Lumina', 'Malibu', 'Menlo', 'Nova', 'Pickup', 'SSR', 'Silverado', 'Sonic', 'Spark', 'Suburban', 'Tahoe', 'Trailblazer', 'Traverse', 'Trax']`
  * **Lexus**: `['CT-Series', 'ES-Series', 'GS-Series', 'GX 460', 'GX-Series', 'IS-C', 'IS-F', 'IS-Series', 'IS300', 'IS350', 'LC 500', 'LFA', 'LM 300', 'LM 350h', 'LS-Series', 'LX-Series', 'LX570', 'LX600', 'NX 200t', 'NX 300', 'NX 350', 'NX 350H', 'NX-Series', 'Other', 'RC', 'RC F', 'RX-Series', 'SC-Series', 'TX', 'UX 200', 'UX-Series']`
  * **Mercedes Benz**: `['190', '240/260/280', '400/420', '450 SEL', 'A-Class', 'A200', 'AMG', 'B-Class', 'C-Class', 'C-Class Coupe', 'C43', 'CL-Class', 'CLA', 'CLC', 'CLE-Class', 'CLK-Class', 'CLS 450', 'CLS-Class', 'E-Class', 'E-Class Coupe', 'EQA', 'EQB', 'EQC', 'EQE', 'EQS', 'G-Class', 'GL-Class', 'GLA', 'GLB', 'GLC', 'GLC 63', 'GLE Coupe', 'GLE-Class', 'GLK-Class', 'GLS-Class', 'GT', 'M-Class', 'Other', 'R-Class', 'S-Class', 'S-Class Coupe', 'SEC-Class', 'SEL-Class', 'SL-Class', 'SLC', 'SLK-Class', 'SLR', 'SLS', 'Sprinter', 'V-Class', 'Viano', 'Vito', 'X Class']`
  * **BMW**: `['1-Series', '2-Series', '3-Series', '4-Series', '5-Series', '6-Series', '7-Series', '8-Series', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M8', 'M850i', 'Other', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'XM', 'Z3', 'Z4', 'Z8', 'i3', 'i7', 'i8', 'iX']`
  * **Audi**: `['A1', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'Other', 'Q2', 'Q3', 'Q5', 'Q7', 'Q8', 'R8', 'RS Q8', 'RS e-tron', 'RSQ3', 'S3/RS3', 'S4/RS4', 'S5/RS5', 'S6/RS6', 'S7/RS7', 'S8', 'SQ8', 'TT', 'e-tron']`

* **region_specs** → `['GCC Specs', 'American Specs', 'European Specs', 'Canadian Specs', 'Korean Specs', 'Other', 'Japanese Specs', 'Chinese Specs']`

* **location_cleaned** → `['Dubai', 'Sharjah', 'Abu Dhabi', 'Ajman', 'Al Ain', 'Umm Al Qawain', 'Ras Al Khaimah', 'Fujeirah']`

### 🔢 **Numeric Features & Their Data Types**

* **km** → `int64` (Mileage in kilometers)
* **warranty** -> bool (Is there a warranty on the car)
* **Service History** -> bool (Is there a service history available)
* **No Accident** -> bool (Have there been any accidents)
* **Luxury** -> bool (Is is a luxury car)
* **Age** -> `int64` (What is the age of the car *current date - model year*)

## 🎯 End Goal

By the end of this track, you’ll have a **live, shareable ML demo app** with a simple UI, containerized in Docker, and deployed to Hugging Face Spaces — an ideal portfolio-ready project showing you can take a model into production.
