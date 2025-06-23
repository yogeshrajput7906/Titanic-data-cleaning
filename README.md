# Titanic Data Cleaning

This project is part of **Task 1** of the **AI & ML Internship at Elevate Labs**.

---

## 📝 Project Description

The goal of this task is to clean and preprocess the Titanic dataset to prepare it for machine learning. This includes handling missing data, encoding categorical variables, feature scaling, and outlier removal.

By completing this task, I have demonstrated my understanding of basic data cleaning techniques, which are essential before building any machine learning model.

---

## 📂 Files Included

- `Cleaned_Titanic_Dataset.csv` – Cleaned version of the Titanic dataset
- `titanic_preprocessing.py` – Python code for data cleaning and preprocessing
- `README.md` – Project overview and description

---

## Preprocessing Steps

1. Loaded dataset using pandas
2. Handled missing values in `Age` and `Embarked`
3. Dropped the `Cabin` column due to excessive missing data
4. Encoded categorical variables:
   - `Sex` with Label Encoding
   - `Embarked` with One-Hot Encoding
5. Standardized `Age` and `Fare` using `StandardScaler`
6. Removed outliers in `Age` using IQR method

---

## 📊 Dataset Used

[Titanic Dataset on Kaggle](https://www.kaggle.com/datasets/yasserh/titanic-dataset)

---

Created by [Yogesh Rajput]

