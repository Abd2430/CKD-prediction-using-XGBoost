
# Chronic Kidney Disease (CKD) Prediction App
I developed this project to build and deploy a machine learning model for predicting Chronic Kidney Disease (CKD). The goal was to create an accurate and interpretable tool that can assist healthcare professionals in early diagnosis, showcasing my end-to-end data science skills.

The project follows a complete machine learning workflow, from data preprocessing to model training, evaluation, and deployment as an interactive web application using Streamlit.

## 🚀 App Overview
I built this application to allow users to input various clinical parameters and receive an instant prediction of whether a patient is likely to have CKD. The app is hosted on Streamlit Community Cloud for public access.

## 🎯 My Contributions & Workflow
Data Preprocessing: I handled imbalanced data by using SMOTE (Synthetic Minority Oversampling Technique), which was critical for ensuring the model could accurately predict both positive and negative cases.

## Model Selection: 
I trained and evaluated several machine learning algorithms to find the best fit for this problem. My process included:

Building a Logistic Regression model as a simple baseline.

Training and tuning a Random Forest Classifier to assess its performance.

Testing a Support Vector Machine (SVM) to see its effectiveness on the dataset.

## Hyperparameter Tuning: 
I used XGBoost, a powerful gradient boosting algorithm, and performed hyperparameter tuning with GridSearchCV to fine-tune the model for maximum predictive performance.

## Model Interpretation: 
To explain the model's decisions, I used SHAP (SHapley Additive exPlanations) to identify and visualize the most influential features.

## Deployment: 
I deployed the final, best-performing model as an interactive web application on Streamlit Community Cloud, making it accessible to anyone.

## 📊 My Results & Analysis
My analysis showed that XGBoost was the best model for this prediction task, consistently outperforming the other algorithms. I validated this with key visualizations:

## ROC Curve Comparison
This plot shows the superior performance of my tuned XGBoost model, with a higher area under the curve (AUC).

## SHAP Feature Importance
This plot summarizes the importance of each feature in my model's predictions. The SHAP values helped me understand why the model made its predictions, confirming that Serum Creatinine, Systolic Blood Pressure, and GFR were the most critical factors, aligning with medical knowledge.


## PROJECT STRUCTURE
.
├── .streamlit/
│   └── config.toml           # Streamlit app theme
├── assets/                   # Folder for images in this README
├── notebooks/                
│   └── ckd_analysis_and_training.ipynb # My complete analysis and training workflow
├── requirements.txt          # All Python libraries used in the project
├── README.md                 # This file
├── Chronic_Kidney_Dsease_data.csv # The dataset I used
├── features.pkl              # List of features used by the model
└── xgb_model_reduced.pkl     # My final, best-performing model


## 🛠️ How to Run the App Locally
To run this app on your own machine, follow these simple steps:

1. Clone the repository:
   git clone https://github.com/Abd2430/ckd-prediction/
   cd your-repository

2. Install dependencies:
   pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run streamlit_app.py

