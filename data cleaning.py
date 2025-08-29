import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
df = pd.read_csv("cirrhosis.csv")
# print(df.head())
# print(df.info())
# print(df.isnull().sum())
df['Age_Years'] = df['Age']/365.25 #conversion of age from days to years
df['Age_Years'] = df['Age_Years'].round(1)
# print(df['Age_Years'].describe()) #confirmation
df.drop(columns=['Age'],inplace=True) #dropping the original 'Age' column as it is no longer needed
#for numerical columns
num_cols = ['Platelets', 'Prothrombin', 'Cholesterol', 'Tryglicerides', 'Copper']
for col in num_cols:
    if col in df.columns:
        df[col].fillna(df[col].median(), inplace=True)

#for categorical columns
cat_cols = ['Stage', 'Ascites', 'Hepatomegaly', 'Spiders', 'Alk_Phos', 'SGOT']
for col in cat_cols:
    if col in df.columns:
        df[col].fillna(df[col].mode()[0], inplace=True)

df['Drug'] = df['Drug'].fillna("Unknown")
# print(df.isnull().sum()) #final check that shows everything is null
df.drop('ID',axis=1,inplace=True)
# print(df.shape)
# print(df.head())
# PERFORMING EDA TO UNDERSTAND RELATIONSHIPS:
# Patient Survival Status (Censored C or Deceased D):
sns.set(style="whitegrid", palette="muted")
plt.figure(figsize=(6,4))
sns.countplot(x='Status', data=df)  
plt.title("Patient Survival Status Distribution")
# plt.show()

# Numerical Features Distribution using Histogram
num_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[num_cols].hist(figsize=(12,10), bins=30)
plt.suptitle("Numerical Features Distributions")
plt.show()