import streamlit as st
import joblib
import numpy as np

# 1. Load the AI "Brain"
ai_brain = joblib.load('fraud_model.pkl')

# 2. Page Config & Style
st.set_page_config(page_title="FraudGuard AI Demo", page_icon="🛡️")

st.title("🛡️ FraudGuard: AI Transaction Security")
st.write("""
This system uses Machine Learning to scan bank transactions for theft. 
**Try the 'Quick Test' buttons below** to see how the AI reacts to different behaviors!
""")

# --- NEW: INTERVIEWER QUICK-TEST BUTTONS ---
st.subheader("🚀 Quick Test Scenarios")
col_a, col_b = st.columns(2)

with col_a:
    if st.button("✅ Load Normal Transaction"):
        st.session_state.money = 50.0
        st.session_state.v14 = 0.5
        st.session_state.v17 = 0.2
        st.toast("Normal data loaded!")

with col_b:
    if st.button("🚨 Load Suspicious Transaction"):
        st.session_state.money = 999.0
        st.session_state.v14 = -12.0
        st.session_state.v17 = -8.5
        st.toast("Fraudulent pattern loaded!")

st.divider()

# --- INPUT SECTION ---
st.subheader("Manual Data Entry")

# Using session_state so the buttons above can fill these boxes automatically
money = st.number_input("Transaction Amount ($)", min_value=0.0, key="money")

with st.expander("Show Advanced Security Patterns"):
    st.write("These patterns are calculated by the bank based on location, device, and history.")
    v14 = st.number_input("Security Signal A (V14)", help="Usually a positive number for safe users. Deep negatives suggest a stolen card.", key="v14")
    v17 = st.number_input("Security Signal B (V17)", help="Measures if the location matches the user's home city.", key="v17")

# --- ANALYSIS ---
if st.button("🔍 Run Security Scan"):
    # Build the 30 features
    features = [0.0] * 30
    features[14] = v14
    features[17] = v17
    features[29] = money
    
    final_data = np.array([features])
    
    # Get Results
    prediction = ai_brain.predict(final_data)[0]
    risk_score = ai_brain.predict_proba(final_data)[0][1]
    
    st.subheader("Result:")
    if prediction == 1 or risk_score > 0.15:
        st.error(f"🚨 **FRAUD ALERT DETECTED**")
        st.progress(risk_score)
        st.write(f"**Risk Level:** {risk_score:.1%} - The system has flagged this as highly suspicious.")
    else:
        st.success(f"✅ **TRANSACTION AUTHORIZED**")
        st.progress(risk_score)
        st.write(f"**Risk Level:** {risk_score:.1%} - Pattern matches standard user behavior.")