import streamlit as st
import joblib
import numpy as np
import pandas as pd

# 1. Load the AI "Brain"
ai_brain = joblib.load('fraud_model.pkl')

st.set_page_config(page_title="Professional Fraud Engine", layout="wide")

st.title("🛡️ Enterprise Fraud Detection Dashboard")
st.write("This interface allows full control over all 30 PCA-transformed features from the original dataset.")

# --- SIDEBAR: PRIMARY CONTROLS ---
st.sidebar.header("Main Transaction Data")
money = st.sidebar.number_input("Transaction Amount ($)", min_value=0.0, value=125.0)
time_val = st.sidebar.number_input("Time (Seconds)", min_value=0, value=400)

# --- MAIN AREA: ALL 28 V-FEATURES ---
st.subheader("Neural Pattern Analysis (V1 - V28)")
st.info("Adjust the sliders below to simulate different transaction patterns.")

# We create 4 columns to fit all 28 sliders neatly
cols = st.columns(4)
v_values = []

for i in range(1, 29):
    with cols[(i-1) % 4]:
        # We create a slider for each V-feature from V1 to V28
        val = st.slider(f"Feature V{i}", -20.0, 20.0, 0.0, help=f"Adjust the weight of component V{i}")
        v_values.append(val)

# --- PREDICTION LOGIC ---
st.divider()

if st.button("🚀 Run Comprehensive Analysis", use_container_width=True):
    # Assemble the full list: Time + V1-V28 + Amount = 30 features
    # Order: Time, V1, V2 ... V28, Amount
    full_feature_list = [time_val] + v_values + [money]
    
    final_data = np.array([full_feature_list])
    
    # Get Prediction
    prediction = ai_brain.predict(final_data)[0]
    risk_score = ai_brain.predict_proba(final_data)[0][1]

    # Display Results in a clean layout
    res_col1, res_col2 = st.columns(2)
    
    with res_col1:
        st.metric("Risk Probability", f"{risk_score:.2%}")
        st.progress(risk_score)

    with res_col2:
        if prediction == 1 or risk_score > 0.15:
            st.error("### 🚨 RESULT: FRAUD DETECTED")
            st.write("The multi-dimensional pattern matches high-risk fraudulent behavior.")
        else:
            st.success("### ✅ RESULT: LEGITIMATE")
            st.write("The transaction profile is within normal behavioral parameters.")