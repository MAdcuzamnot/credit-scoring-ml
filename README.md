# Credit Scoring — Machine Learning Project

## Project Overview

This project focuses on predicting loan defaults using machine learning.

The goal is to analyze borrower characteristics, identify patterns associated with credit risk, and develop models to predict the probability of loan default.

The project covers the complete ML pipeline, from exploratory data analysis (EDA) to model training, evaluation, and comparison.

## Dataset

**Source:** [Credit Risk Dataset — Hugging Face](https://huggingface.co/datasets/RPD123-byte/credit-risk-datasets)

- **Observations:** 150,000
- **Features:** 19
- **Target:** `default` (0 — No Default, 1 — Default)
- **Task:** Binary Classification

## Technologies

- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- Scikit-learn (planned)
- Git / GitHub

## Project Progress

### 1. Exploratory Data Analysis (EDA) — In Progress

- [x] Dataset exploration and data types
- [x] Missing values analysis
- [x] Target distribution and class imbalance
- [x] Descriptive statistics
- [x] Loan amount distribution
- [x] Outlier detection using IQR
- [ ] Feature relationships and correlation analysis

**[View Detailed EDA Notebook](notebooks/01_EDA.ipynb)**

### 2. Data Preprocessing — Planned

- [ ] Missing value handling
- [ ] Feature encoding and scaling
- [ ] Feature engineering
- [ ] Train/test split

### 3. Model Training — Planned

- [ ] Logistic Regression (baseline)
- [ ] Random Forest
- [ ] Gradient Boosting

### 4. Model Evaluation — Planned

- [ ] Precision, Recall, F1-score
- [ ] ROC-AUC
- [ ] Model comparison
- [ ] Feature importance analysis

## Current Status

**Exploratory Data Analysis is in progress.**

The next step is to investigate relationships between borrower characteristics and loan defaults.