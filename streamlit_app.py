import streamlit as st
import pandas as pd
import joblib


st.title("CKD Prediction Form")
st.markdown("---")

# ----------------------------------------------------------------------
# 1. Load Model and Features (from app.py)
#
# We use st.cache_resource to load these heavy objects only once.
# This makes the app run much faster.
# ----------------------------------------------------------------------

@st.cache_resource
def load_model_and_features():
    try:
        model = joblib.load('xgb_model_reduced.pkl')
        features = joblib.load('features.pkl')
        return model, features
    except FileNotFoundError:
        st.error("Error: Model files `xgb_model_reduced.pkl` and `features.pkl` not found.")
        st.stop()

model, features = load_model_and_features()

# ----------------------------------------------------------------------
# 2. Build the User Interface (from index.html)
#
# We will create a two-column layout for a cleaner look and use
# st.form to group the inputs and the predict button.
# ----------------------------------------------------------------------

with st.form("ckd_prediction_form"):
    st.header("Enter Patient Data")
    
    # We will use st.columns to create a 2-column layout for the inputs
    cols = st.columns(2)
    inputs = {}
    
    # Replicating the loop from your index.html
    for i, feature in enumerate(features):
        col = cols[i % 2]  # Alternate between the two columns
        
        # Determine the input widget based on the feature name
        if feature == 'Gender':
            inputs[feature] = col.selectbox(
                label=feature,
                options=[1, 0],
                format_func=lambda x: "1 (Male)" if x == 1 else "0 (Female)"
            )
            
        elif feature in ['MuscleCramps', 'Itching', 'FamilyHistoryHypertension']:
            inputs[feature] = col.selectbox(
                label=feature,
                options=[0, 1],
                format_func=lambda x: "0 (NO)" if x == 0 else "1 (YES)"
            )
            
        else:
            hint = ""
            if feature == 'ProteinInUrine':
                hint = "Typical range: 0.03 – 3.0 mg/dL"
            elif feature == 'FastingBloodSugar':
                hint = "Typical range: 70–130 mg/dL"
            elif feature == 'HbA1c':
                hint = "Typical range: 4.0–6.5%"
            elif feature == 'SystolicBP':
                hint = "Typical range: 90–140 mmHg"
            elif feature == 'GFR':
                hint = "Normal: >90, CKD: <60"
            elif feature == 'SerumCreatinine':
                hint = "Normal: 0.6–1.3 mg/dL"
            elif feature == 'BUNLevels':
                hint = "Normal: 7–20 mg/dL"
                
            inputs[feature] = col.number_input(
                label=feature,
                step=0.01,
                help=hint
            )

    st.markdown("---")
    submitted = st.form_submit_button("Predict")

# ----------------------------------------------------------------------
# 3. Handle Prediction (from app.py)
#
# This code runs only when the button is clicked.
# ----------------------------------------------------------------------

if submitted:
    try:
        # Create a DataFrame from the inputs, just like in your Flask code
        input_df = pd.DataFrame([inputs], columns=features)
        
        # Make the prediction
        prediction = model.predict(input_df)[0]
        
        # Display the result
        if prediction == 1:
            st.error("Result: CKD Detected")
            st.markdown(
                """
                <style>
                .st-emotion-cache-1629p2n {
                    background-color: #fce4ec;
                    border: 2px solid #ef5350;
                    color: #ef5350;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
        else:
            st.success("Result: No CKD")
            st.balloons()
            
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")