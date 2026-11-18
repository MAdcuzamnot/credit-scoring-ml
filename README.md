# Credit Scoring ML

A machine learning project focused on predicting credit default risk using borrower financial and credit history data.

The goal is to build an end-to-end binary classification pipeline, starting with exploratory data analysis and progressing to model training and evaluation.

## Dataset

- Source: Lending Club dataset (Hugging Face)
- Observations: 150,000
- Features: 19
- Target: `default` (0 — non-default, 1 — default)

The dataset is excluded from the repository.

## Project Progress

- [x] Data loading and initial exploration
- [x] Exploratory Data Analysis (EDA)
- [x] Missing values and outlier analysis
- [x] Feature relationships and correlation analysis
- [x] Train/test split
- [x] Initial missing value imputation
- [x] Initial categorical encoding
- [x] Numerical feature scaling
- [ ] Complete preprocessing pipeline
- [ ] Logistic Regression baseline
- [ ] Random Forest and Gradient Boosting
- [ ] Model evaluation and comparison

## Notebooks

- [01_EDA.ipynb](notebooks/01_EDA.ipynb) — exploratory data analysis and key findings.
- [02_Preprocessing.ipynb](notebooks/02_Preprocessing.ipynb) — data preparation for machine learning.

## Tech Stack

Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Jupyter Notebook.