# 🏨 Hotel Reservation Prediction Project

[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Build](https://img.shields.io/badge/build-passing-brightgreen)]()
[![Cloud Run](https://img.shields.io/badge/GCP-Deployed-green)]()
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue)]()

---

## 🚀 Overview

An end-to-end machine learning project to predict whether a hotel reservation will be canceled or honored. It includes data processing, model building, experiment tracking, CI/CD automation with Jenkins, containerization using Docker, and deployment on Google Cloud Run.

---

## 🎯 Problem Statement

Hotel reservation cancellations impact revenue and operations. This project aims to build a predictive model that helps hotels proactively identify likely cancellations and take appropriate action.

---

## 🛠 Tech Stack

**Languages & Frameworks:**  
- Python, Flask, Jinja2  
**ML Libraries:**  
- LightGBM, scikit-learn, pandas, NumPy, imbalanced-learn  
**DevOps & MLOps:**  
- Jenkins, Docker, MLflow, Google Cloud (GCS, GCR, Cloud Run)  
**Others:**  
- YAML config files, Google Cloud SDK, GitHub  

---

## 🧠 Solution Highlights

- ✔️ Clean data pipeline with configuration-driven ingestion and preprocessing  
- ✔️ LightGBM classifier with hyperparameter tuning  
- ✔️ Flask web app to predict reservation cancellation  
- ✔️ Fully automated CI/CD pipeline with Jenkins  
- ✔️ Dockerized application deployed on **Google Cloud Run**

---

## 📁 Project Structure


---

## ⚙️ How It Works

1. 🔍 **Data Ingestion**  
   Reads raw CSV from GCS or local path.

2. 🧹 **Preprocessing**  
   Applies encoding, scaling, and feature engineering as per config.

3. 🧠 **Model Training**  
   Uses LightGBM with randomized search for best parameters.

4. 🧪 **Experiment Tracking**  
   MLflow logs metrics, models, and artifacts.

5. 🌐 **Flask Web App**  
   UI for user to input booking details and get predictions.

6. 🐳 **Dockerization**  
   App is containerized using Docker.

7. 🚀 **Deployment**  
   Docker image pushed to GCR and deployed on Google Cloud Run via Jenkins pipeline.

---

## 🔄 Jenkins CI/CD Pipeline

**Pipeline Steps:**

- ✅ Clone GitHub repo  
- ✅ Create virtual environment  
- ✅ Install dependencies  
- ✅ Train & build model  
- ✅ Dockerize the app  
- ✅ Push to Google Container Registry  
- ✅ Deploy to Google Cloud Run

Credentials are managed securely in Jenkins.

---

## 💻 Run Locally

```bash
# Clone repo
git clone https://github.com/ishanpandey15/HotelReservationPredictionProject.git
cd HotelReservationPredictionProject

# Create virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install -e .

# Train model
python pipeline/training_pipeline.py

# Run web app
python application.py
# Build Docker image
docker build -t hotel-reservation-app .

# Run the container
docker run -p 5000:5000 hotel-reservation-app
☁️ Cloud Deployment
Container pushed to: gcr.io/<your-project-id>/hotel-reservation-app

Deployed on: Google Cloud Run

URL: https://ml-project-624667050708.us-central1.run.app/ ( I ended it to avoid charges ).

📈 Future Enhancements
Add test cases and CI test stage

Automate infra setup with Terraform

Deploy ML model as a separate microservice

Integrate monitoring using Prometheus/Grafana

👨‍💻 Author
Ishan Pandey
Data Scientist | AI/ML Engineer 
