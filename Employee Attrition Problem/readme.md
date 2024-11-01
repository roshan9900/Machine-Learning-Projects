# Employee Attrition Prediction

## 1. Project Overview
The goal of this project is to analyze employee attributes and predict attrition. By identifying key factors, the model aims to support the organization in retaining talent by understanding what drives employees to leave.

## 2. Problem Statement
Identify factors contributing to employee attrition and predict which employees are likely to leave based on their roles, experience, education, and proximity to the company.

## 3. Data Overview
- **Dataset**:
  - Train and test datasets provided with 1,000,000 samples each.
  - Features include `jobType`, `degree`, `major`, `industry`, `yearsExperience`, `milesFromMetropolis`, and `salary`.
- **Attributes**:
  - *Categorical*: `jobType`, `degree`, `major`, `industry`
  - *Numerical*: `yearsExperience`, `milesFromMetropolis`, `salary`

## 4. Exploratory Data Analysis (EDA)
- **Initial Data Inspection**: Verified data types and checked for missing values.
- **Correlations**:
  - Positive correlation between `yearsExperience` and `salary`.
  - Negative correlation between `milesFromMetropolis` and `salary`.
- **Outliers**: Addressed using IQR on salary and experience features.
- **Visualizations**: Used scatter plots, histograms, box plots, and violin plots to understand distributions and relationships.

## 5. Data Preprocessing and Feature Engineering
- **Encoding**: Converted categorical variables using label encoding and one-hot encoding.
- **Scaling**: StandardScaler applied to numerical features to improve model stability.
- **Chi-Square Test**: Analyzed categorical variables for independence, finding significant relationships between job type, degree, and major.

## 6. Model Building
### 6.1 Model Selection
Multiple models were tested:
- **Linear Regression**: Baseline model to assess the initial predictive capability.
- **Random Forest Regressor**: Improved accuracy with feature importance evaluation.
- **Gradient Boosting and AdaBoost**: Enhanced predictions for more balanced performance.
- **Decision Tree Regressor**: Effective in interpretability but showed overfitting.

### 6.2 Model Evaluation and Performance Metrics
Evaluated models based on key metrics:
- **Root Mean Square Error (RMSE)**: Measures average prediction error magnitude.
- **Mean Absolute Error (MAE)**: Average absolute difference between predictions and actual values.
- **R-squared**: Proportion of variance explained by the model; higher values indicate better fit.

#### Model Metrics Summary
| Model                      | RMSE (Train) | RMSE (Test) | MAE (Train) | MAE (Test) | R-squared (Train) | R-squared (Test) |
|----------------------------|--------------|-------------|-------------|------------|--------------------|-------------------|
| Linear Regression          | 19.63        | 19.61       | 15.88       | 15.85      | 0.74               | 0.74              |
| Random Forest Regressor    | 10.31        | 21.05       | 7.93        | 16.75      | 0.93               | 0.70              |
| Gradient Boosting Regressor| 19.86        | 19.85       | 15.95       | 15.95      | 0.73               | 0.73              |
| Decision Tree Regressor    | 8.00         | 26.39       | 3.88        | 20.48      | 0.96               | 0.53              |
| AdaBoost Regressor         | 27.32        | 27.36       | 22.92       | 22.97      | 0.50               | 0.49              |

- **Key Observations**:
  - Random Forest and Gradient Boosting models performed best on training data but had varying test set accuracy, indicating potential overfitting in certain models.
  - Linear Regression maintained a balanced performance across training and testing datasets.
  - Decision Tree Regressor showed high train accuracy but lower test accuracy, suggesting overfitting.

### 6.3 Model Optimization
- **Hyperparameter Tuning**: Conducted using RandomizedSearchCV on Random Forest, optimizing parameters such as `n_estimators`, `max_depth`, and `min_samples_leaf` to achieve the best performance.
  
## 7. Results and Analysis
- **Feature Importance**: Key factors influencing predictions were `yearsExperience`, `industry`, and `jobType`.
- **Top Influencing Factors**: Job type, education, and location proximity were strongly related to attrition likelihood.

## 8. Conclusion
The project highlights critical factors influencing employee attrition, which can aid HR in developing targeted retention strategies. The model’s predictive power enables the organization to preemptively address potential attrition cases.

