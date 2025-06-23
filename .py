import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Load the dataset
file_path = "D:/Company AI and ML/Cleaned_Titanic_Dataset.csv"
df = pd.read_csv(file_path)

# Step 1: Basic Info
basic_info = {
    "info": df.info(),
    "description": df.describe(include='all'),
    "nulls": df.isnull().sum()
}

# Step 2: Handle missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
if 'Cabin' in df.columns:
    df.drop('Cabin', axis=1, inplace=True)

# Step 3: Encode categorical variables
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

# Step 4: Normalize numerical features
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

# Step 5: Outlier detection and removal (using IQR)
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1
df = df[~((df['Age'] < (Q1 - 1.5 * IQR)) | (df['Age'] > (Q3 + 1.5 * IQR)))]

# Save cleaned data
cleaned_file_path = "D:/Company AI and ML/Cleaned_Titanic_Dataset.csv"
df.to_csv(cleaned_file_path, index=False)

cleaned_file_path
