# Exploratory Data Analysis

## 1. Dataset Overview

The dataset contains 150,000 observations and 20 columns.

- 19 features
- 1 target variable

Data types:
- 8 integer columns
- 12 floating-point columns

## 2. Missing Values

Missing values were identified using:

```python
df.isnull().sum()
```

Results:

| Feature | Missing Values |
|---------|---------------:|
| emp_length | 8,643 |
| dti | 36 |
| revol_util | 101 |

### Conclusion

The largest number of missing values occurs
in the `emp_length` feature.

Missing values have not been removed or filled yet.

## 3. Target Distribution

Class distribution was calculated using:

```python
df["default"].value_counts()
```

Results:

- Class 0: 119,727 (79.818%)
- Class 1: 30,273 (20.182%)

### Visualization

![Target Distribution](images/class_distribution.png)

### Conclusion

The target variable is imbalanced.

Accuracy alone may be misleading when evaluating
classification performance.

Additional evaluation metrics such as Precision,
Recall, F1-score, and ROC-AUC will be considered.

## 4. Next Steps

- Descriptive statistics
- Feature distribution analysis
- Outlier detection
- Correlation analysis