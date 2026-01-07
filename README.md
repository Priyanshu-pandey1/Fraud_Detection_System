# 🛡️ Enterprise Financial Fraud Detection System

## 🚀 [Live Demo: Click Here to View the App](https://frauddetectionsystem-6bkfsscv8svno4cucjysej.streamlit.app/)

## 📌 Project Overview
In the banking industry, missing a single fraudulent transaction is far more costly than a false alarm. This project implements a high-recall **Fraud Detection Engine** capable of scanning credit card transactions for suspicious patterns in real-time. 

Using a dataset of over **284,000 transactions**, I developed a model that prioritizes security while maintaining a user-friendly deployment interface.

## 📊 Technical Achievements
- **Model Performance:** Achieved a **Recall of 88%** on the minority class (Fraud), ensuring that nearly 9 out of 10 fraudulent attempts are caught.
- **Algorithm:** Leveraged **LightGBM** (Light Gradient Boosting Machine) for its superior ability to handle highly imbalanced datasets.
- **Data Privacy:** Handled **30 input features**, including 28 PCA-transformed "V-features" to simulate real-world data privacy standards (GDPR).

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Machine Learning:** LightGBM, Scikit-Learn
* **Serialization:** Joblib
* **Deployment:** Streamlit Cloud
* **Environment:** VS Code & Google Colab

## 🚀 App Functionality
The deployed application provides a "Full-Feature" dashboard where users can:
1.  **Input Transaction Metrics:** Manually set the transaction amount and time.
2.  **Adjust Pattern Signals:** Use sliders to modify all 28 PCA components ($V1$-$V28$).
3.  **Real-Time Risk Scoring:** The model calculates a probability score and flags the transaction as **Legitimate** or **Fraudulent** based on optimized thresholds.

## 📈 Methodology
1.  **Exploratory Data Analysis (EDA):** Identified $V14, V17, \text{ and } V12$ as the highest-impact features using correlation matrices.
2.  **Handling Imbalance:** Applied custom weights and probability threshold tuning to move beyond standard accuracy and focus on **Recall**.
3.  **Inference Pipeline:** Built a robust pipeline to scale user inputs and deliver sub-second predictions.

## 📂 Project Structure
- `app.py`: Streamlit dashboard code with grid-layout UI.
- `fraud_model.pkl`: The serialized LightGBM model.
- `scaler.pkl`: Pre-fitted StandardScaler for feature normalization.
- `requirements.txt`: Necessary libraries for cloud deployment.
