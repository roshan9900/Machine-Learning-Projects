# Cardiovascular Disease Prediction

## 1. Project Overview

### Problem Statement
The objective is to predict the likelihood of cardiovascular disease in patients using various health-related features such as age, cholesterol level, blood pressure, smoking habits, etc.

### Dataset
The dataset contains 70,000 records with 13 features, divided into three types:
- **Objective Features** (e.g., age, height, weight)
- **Examination Features** (e.g., blood pressure, cholesterol)
- **Subjective Features** (e.g., smoking, alcohol intake)

The target variable is a binary feature indicating the presence or absence of cardiovascular disease (`cardio`).

---

## 2. Exploratory Data Analysis (EDA)

### Summary of Findings
- **Age Distribution**: Most individuals are above 20,000 days old.
- **Gender and Disease Prevalence**: Women show a higher incidence of cardiovascular disease compared to men.
- **Height and Weight Distributions**: The height and weight distributions suggest similar patterns among those with and without the disease.
- **Cholesterol and Glucose**: Higher levels of cholesterol and glucose are more common among individuals with cardiovascular disease.
- **Lifestyle Factors**: Alcohol intake and smoking did not show strong correlations with the disease in this dataset.

---

## 3. Data Preprocessing

### Steps Taken
1. **Removing the `id` Column**: Dropped as it does not contribute to prediction.
2. **Handling Missing Values**: The dataset has no null values, making it suitable for modeling without imputation.
3. **Outlier Treatment**: Capped unrealistic values in blood pressure to reduce noise and improve model accuracy.
4. **Feature Scaling**: Used StandardScaler to normalize features for model training.

---

## 4. Model Building

### Model Chosen: Logistic Regression
- **Baseline Model**: The initial logistic regression model achieved a test accuracy of approximately 71%.
- **Refined Model**: After outlier removal and feature transformation, the accuracy improved slightly to 72%, without signs of overfitting or underfitting.

### Model Evaluation
- **Metrics Used**: Precision, Recall, F1-Score, and Accuracy.
- **Results**:
  - **Precision**: 71% for negative cases, 74% for positive cases.
  - **Recall**: 76% for negative cases, 69% for positive cases.
  - **Accuracy**: Approximately 72% on both train and test sets.

---

## 5. Conclusion

The logistic regression model performed well, achieving a balanced performance across precision, recall, and accuracy. Although improvements could be explored with more complex models, logistic regression provided a reliable prediction baseline without overfitting.

---

## 6. Future Work
1. **Feature Engineering**: Investigate additional derived features or combinations that may improve prediction accuracy.
2. **Advanced Models**: Test more complex classifiers, such as Decision Trees, Random Forest, or Gradient Boosting, for possible performance gains.
3. **Hyperparameter Tuning**: Use grid search or random search to optimize model parameters.

