

# Email Classification with BERT

### Project Overview:
The project aims to classify email messages as either "spam" or "ham" (not spam) using a pre-trained BERT model. The dataset consists of email messages labeled as either ham or spam, and BERT is used to extract contextual embeddings for text classification. The objective is to implement and fine-tune the BERT model for binary email classification, achieving a high level of accuracy.

---

### 1. **Data Understanding:**

- **Dataset**: The dataset consists of 5572 email messages categorized as spam or ham:
  - `ham`: 4825 entries (86.59%)
  - `spam`: 747 entries (13.41%)

- **Columns**:
  - `Category`: Spam or ham labels.
  - `Message`: The email message text.
  
- **Initial Data Insights**:
  - There are no missing values in the dataset.
  - The dataset is highly imbalanced, with the majority of messages labeled as ham.

---

### 2. **Data Preprocessing:**

- **Label Encoding**: 
  - A new column `label` was created where spam is labeled as `1` and ham as `0`.

- **Data Balancing**: 
  - The dataset was imbalanced, so down-sampling was performed to balance the ham and spam classes. After balancing, there were 1494 entries (747 ham, 747 spam).

- **Train-Test Split**: 
  - The data was split into training (70%) and testing (30%) sets.
  - Training set size: 1045 entries.
  - Test set size: 449 entries.

---

### 3. **Model Building:**

- **BERT Preprocessing and Encoding**:
  - BERT preprocessor and encoder were loaded from TensorFlow Hub.
  - Preprocessing included tokenization, segmentation, and attention masks for input to the BERT model.

- **Model Architecture**:
  - Input: Text messages.
  - Preprocessing: BERT uncased preprocessor.
  - Encoder: BERT uncased encoder.
  - Output: A dense layer with a sigmoid activation function for binary classification.
  - The BERT encoder's pooled output was passed through a dropout layer and fed into the final output layer.

- **Metrics**: The model was compiled with:
  - **Accuracy**
  - **Precision**
  - **Recall**

---

### 4. **Model Training:**

- **Optimizer**: Adam optimizer.
- **Loss Function**: Binary crossentropy.
- **Training**: The model was trained for 10 epochs with a batch size of 32.

Key results during training:
- **Epoch 1**: Accuracy: 63%, Precision: 63%, Recall: 60%.
- **Epoch 10**: Accuracy: 90%, Precision: 85%, Recall: 96%.

---

### 5. **Model Evaluation:**

The model's performance was evaluated on the test dataset after training:
- **Accuracy**: 90%
- **Precision**: 95% for ham, 85% for spam.
- **Recall**: 82% for ham, 96% for spam.
- **F1-score**: 88% for ham, 90% for spam.

These results demonstrate that the model effectively distinguishes between spam and ham emails, with slightly better performance in detecting spam.

---

### 6. **Conclusion:**

The BERT-based email classifier successfully achieves a high accuracy of 90%, with strong precision and recall for both classes. The BERT model proved to be effective for the task of email classification. Future work could involve further fine-tuning of hyperparameters or experimenting with additional pre-trained models to improve performance.

---

### Appendix:
- **Python Libraries Used**:
  - `pandas`, `numpy`, `matplotlib`, `tensorflow`, `tensorflow_hub`, `tensorflow_text`
  
