

# Ethereum Fraud Detection

### Project Overview:
This project aims to detect fraudulent transactions on the Ethereum blockchain using machine learning techniques. The dataset contains various attributes related to Ethereum transactions, and the goal is to classify whether a transaction is fraudulent (flagged as 1) or not (flagged as 0). The classification models used include Logistic Regression, SVM, Decision Tree, Random Forest, and Gradient Boosting.

---

### 1. **Data Understanding:**

The dataset used contains 9841 rows and 51 columns, with transaction data attributes such as:
- `Address`
- `FLAG` (target variable indicating fraud)
- `Avg min between sent tnx`, `Received Tnx`, `ERC20 min/max val sent`, etc.

Steps for data understanding include:
- Reading the dataset and checking the first few rows.
- Checking data types, number of missing values, and statistical information.

---

### 2. **Data Preprocessing:**
- **Null Value Treatment:** Columns with missing values were identified. Numerical missing values were replaced with the median, and categorical missing values were replaced with the mode.
- **Label Encoding:** Categorical columns (like `Address`, `ERC20 most sent token type`) were label encoded for use in machine learning algorithms.
- **Feature Scaling:** Features were standardized using `StandardScaler` to ensure equal contribution to the models.
- **Train-Test Split:** The data was split into training (70%) and testing (30%) sets using `train_test_split`.

---

### 3. **Model Building:**

Multiple classification models were implemented to predict fraudulent transactions. The performance of each model was evaluated using the test dataset.

- **Logistic Regression:** Achieved an accuracy of 88%.
- **Support Vector Machine (SVM):** Achieved an accuracy of 85%.
- **Gradient Boosting Classifier:** Achieved an accuracy of 99%.
- **Decision Tree Classifier:** Achieved an accuracy of 99%.
- **Random Forest Classifier:** Achieved an accuracy of 99%.

For each model, a classification report was generated, detailing precision, recall, and F1-scores.

---

### 4. **Model Evaluation:**

The following metrics were used to evaluate the models:
- **Accuracy:** Measures overall performance. The best-performing models (Gradient Boosting and Random Forest) achieved 99% accuracy.
- **Precision, Recall, and F1-Score:** Gradient Boosting and Random Forest models had high precision (0.99), recall (1.00), and F1-scores (0.99).

---

### 5. **Hyperparameter Tuning:**

The Random Forest model was further optimized using RandomizedSearchCV. Hyperparameters such as `n_estimators`, `criterion`, `max_depth`, and `min_samples_split` were tuned. The best parameters obtained were:
- `n_estimators: 50`
- `criterion: entropy`
- `max_depth: 4`
- `min_samples_split: 3`

The tuned Random Forest model achieved a training accuracy of 98.3% and testing accuracy of 98.1%.

---

### 6. **Conclusion:**

The project successfully detects fraudulent transactions with high accuracy. The Random Forest and Gradient Boosting models performed the best, offering over 99% accuracy. Hyperparameter tuning further improved the Random Forest model's performance. Future improvements could include using more complex models or further feature engineering to enhance model performance.


