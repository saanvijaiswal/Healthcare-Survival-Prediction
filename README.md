# Cirrhosis Patient Survival Prediction

This project focuses on cleaning, analyzing, and modeling a real-world clinical dataset of cirrhosis patients.  
It demonstrates an **end-to-end data pipeline**: from raw messy data → cleaned dataset → insights → predictive modeling.  

## 1. Introduction
- **Cirrhosis** is a late stage of scarring (fibrosis) of the liver caused by various liver conditions. Predicting survival is crucial for treatment planning.  
- **Objective**: Build a data analysis and machine learning pipeline to predict patient survival outcomes.  
- **Dataset**: [Cirrhosis Patient Survival Prediction Dataset (Kaggle)](https://www.kaggle.com/datasets/joebeachcapital/cirrhosis-patient-survival-prediction)  

## 2. Tech Stack
- **Languages**: Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)  
- **Techniques**: Data Cleaning, Imputation, EDA, Feature Engineering, Classification, Model Evaluation  
- **Tools**: VS Code, GitHub

## 3. Data Cleaning & Preprocessing
- Inspected dataset for missing values, duplicates, and outliers.  
- Converted **Age** from days → years.  
- Imputed missing values:  
  - Median for numerical features (e.g., Platelets, Prothrombin).  
  - Mode or **"Unknown"** category for categorical features (e.g., Drug, Ascites).  
- Dropped irrelevant columns (e.g., unique patient IDs).  
- Encoded categorical variables using One-Hot Encoding.  
- Scaled numerical features for ML models.

## Outputs
Distribution of Variables
https://github.com/saanvijaiswal/Healthcare-Survival-Prediction/blob/main/outputs/Distribution%20of%20variables%20(1).png
https://github.com/saanvijaiswal/Healthcare-Survival-Prediction/blob/main/outputs/Distribution%20of%20variables.png

Patient Survival Status 
https://github.com/saanvijaiswal/Healthcare-Survival-Prediction/blob/main/outputs/Patient%20Survival%20Status%20Distribution.png

## 4. Exploratory Data Analysis (EDA)
- **Target Distribution**: Visualized survival outcomes.  
- **Numerical Analysis**: Histograms & boxplots for lab test results (Bilirubin, Albumin, Cholesterol).  
- **Categorical Analysis**: Count plots of clinical indicators (Ascites, Hepatomegaly, Stage).  
- **Correlation Heatmap**: Identified relationships between clinical variables.  
- **Feature vs Target**: Example – Bilirubin and Albumin levels were strongly linked to survival status.  


## 5. Model Building
- Data split into **train/test** sets (80/20).  
- Models trained and compared:  
  - Logistic Regression  
  - Random Forest Classifier  
  - Support Vector Machine (SVM)  
- Evaluation Metrics: Accuracy, Precision, Recall, F1-score.  
- **Random Forest** performed best and provided **feature importance** insights.  



## 6. Results & Insights
- **Key Predictors**: Bilirubin, Albumin, Stage, Age, Ascites.  
- Random Forest achieved the highest accuracy on the test set.  
- Feature importance analysis highlighted which clinical features most impact survival.  


## 7. Future Work
- Extend with **Survival Analysis** techniques (Kaplan-Meier, Cox Proportional Hazards) for time-to-event predictions.  

