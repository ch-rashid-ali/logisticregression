import streamlit as st
import pickle
import numpy as np

# Saved model ko load karein
with open("logistic_regression_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🩺 Diabetes Prediction App")
st.write("Patient ki details enter karein taake Diabetes ka pata lagaya ja sake:")

# User inputs
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=150, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=900, value=79)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input("Age", min_value=1, max_value=120, value=33)

# Prediction Button
if st.button("Predict"):
    features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ Patient ko Diabetes hone ka imkaan hai (Positive).")
    else:
        st.success("✅ Patient Normal hai (Negative).")