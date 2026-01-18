# 🎓 Student Performance – End-to-End Machine Learning Project (AWS Elastic Beanstalk)

An end-to-end machine learning project that predicts student academic performance using demographic, behavioral, and academic features.  
This project includes data ingestion, validation, feature engineering, model training, experiment tracking, and deployment through a REST API hosted on AWS Elastic Beanstalk.

---

## 🚀 Overview

- **Goal:** Predict student final scores (or pass/fail) using study and attendance data.  
- **Built with:** Python, FastAPI, Scikit-learn and AWS Elastic Beanstalk.  
- **Deployment:** Elastic Beanstalk with S3 for artifact storage and CloudWatch for monitoring.  
- **Key Features:**
  - Automated data processing pipeline  
  - Feature engineering and model tuning  
  - REST API for real-time predictions  
  - Configurable CI/CD deployment workflow  

---

## 🧰 Tech Stack

| Category | Tools Used |
|-----------|-------------|
| **Language** | Python 3.13 |
| **Framework** | FastAPI, Uvicorn |
| **Machine Learning** | scikit-learn, XGBoost |
| **Data Processing** | pandas, numpy, Great Expectations |
| **Deployment** | AWS Elastic Beanstalk, AWS S3, CloudWatch |
| **CI/CD** | AWS CodePipeline (optional) |
| **Version Control** | GitHub |
| **Containerization** | Docker (optional) |

---

## 🧠 Key Highlights

- Built a complete **end-to-end machine learning pipeline** for student performance prediction.  
- Developed **data ingestion**, **validation**, and **feature engineering** workflows with modular Python scripts.  
- Deployed the trained model as a **REST API** using **FastAPI** on **AWS Elastic Beanstalk**.  
- Integrated **AWS S3** for artifact storage and **AWS CloudWatch** for monitoring logs.  
- Optimized model performance using **Optuna** for hyperparameter tuning.  
- Applied **Pydantic** and **Great Expectations** for schema and data validation.  
- Ensured full reproducibility with **environment isolation** and **version-locked dependencies**.  

---

## 🔮 Future Improvements

- Integrate **MLflow** for centralized experiment tracking.  
- Enable **automatic retraining** based on data drift detection.  
- Add **GitHub Actions** or **AWS CodePipeline** for CI/CD automation.  
- Containerize and deploy via **AWS ECS** or **Kubernetes (EKS)**.  
- Add a **frontend dashboard** for prediction visualization and data analytics.


