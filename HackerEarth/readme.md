Sculpture Shipping Cost Prediction

## 1. Project Overview
The objective of this project is to develop a machine learning model to predict shipping costs for sculptures based on various attributes, including artist reputation, sculpture dimensions, material, shipping requirements, and destination details. This model will assist the company in estimating costs accurately, improving logistics planning, and offering better service to customers.

## 2. Problem Statement
Predict the shipping cost required to transport sculptures based on provided features.

## 3. Data Overview
- **Dataset Source**: The dataset was sourced from Kaggle, containing relevant features like artist reputation, sculpture dimensions, material type, and shipping details.
- **Features**:
  - *Categorical*: Material, Express Shipment, Installation Included, Transport Mode, Fragile Status, etc.
  - *Numerical*: Artist Reputation, Height, Width, Weight, Base Shipping Price, Cost, etc.
  - *Date*: Scheduled Date, Delivery Date

## 4. Exploratory Data Analysis (EDA)
Exploratory Data Analysis helped uncover the distribution of various features and relationships:
- **Null Values**: Handled by either imputing or dropping missing values.
- **Correlation**: Strong correlation found between cost and weight, sculpture price, and shipping base price.
- **Outliers**: Addressed using techniques like Box-Cox transformation for normal distribution adjustment.
- **Distribution Analysis**: Histograms and box plots were used to check the distribution of features and identify outliers.

## 5. Feature Engineering
- **Label Encoding**: Applied to categorical variables for model compatibility.
- **Date Transformation**: Extracted day, month, and year components from scheduled and delivery dates and computed date differences for more detailed analysis.
- **Outlier Removal**: Used the IQR method to eliminate outliers in features like Width, Weight, and Height.

## 6. Model Building
### 6.1 Preprocessing
- **Data Normalization**: StandardScaler was applied to normalize numerical features.
- **Data Split**: Split data into training and test sets (70% - 30% ratio).

### 6.2 Model Selection and Evaluation
- **Model**: Linear Regression was selected as the initial model.
- **Performance Metrics**: Evaluated using RMSE, MSE, MAE, R-squared, and Adjusted R-squared.

### 6.3 Model Optimization
To improve model accuracy:
- **Feature Selection**: Removed features with high Variance Inflation Factor (VIF) to reduce multicollinearity.
- **Results**: Final model achieved an RMSE of approximately 0.0017 with an R-squared of 0.92, indicating strong predictive power.

## 7. Results and Interpretation
- **Key Findings**: 
  - Higher shipping costs are associated with fragile and express shipments.
  - Sculpture material and dimensions have a significant impact on the cost.
- **Top Influencing Features**: Material, weight, shipping type, and installation inclusion contribute heavily to cost prediction.

## 8. Conclusion
The model provides reliable predictions for shipping costs, facilitating better pricing and logistics decisions. Further improvements could involve testing additional models or using feature engineering techniques for better temporal and spatial understanding.
