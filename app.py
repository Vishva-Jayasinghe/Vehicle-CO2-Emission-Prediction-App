import streamlit as st
import joblib
import pandas as pd
import os

# Load model (fixed path)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "vehicle_emission_pipeline.joblib")

model = joblib.load(model_path)

st.title("🚗 Vehicle CO2 Emission Predictor")

# User inputs
make = st.text_input("Make")
model_name = st.text_input("Model")
vehicle_class = st.text_input("Vehicle Class")
transmission = st.text_input("Transmission")

model_year = st.number_input("Model Year", value=2020)
engine_size = st.number_input("Engine Size", value=2.0)
cylinders = st.number_input("Cylinders", value=4)

fuel_city = st.number_input("Fuel Consumption in City")
fuel_hwy = st.number_input("Fuel Consumption Highway")
fuel_comb = st.number_input("Fuel Consumption Combined")

smog_level = st.number_input("Smog Level")

if st.button("Predict CO2 Emission"):
    data = pd.DataFrame([{
        "Make": make,
        "Model": model_name,
        "Vehicle_Class": vehicle_class,
        "Transmission": transmission,
        "Model_Year": model_year,
        "Engine_Size": engine_size,
        "Cylinders": cylinders,
        "Fuel_Consumption_in_City(L/100 km)": fuel_city,
        "Fuel_Consumption_in_City_Hwy(L/100 km)": fuel_hwy,
        "Fuel_Consumption_comb(L/100km)": fuel_comb,
        "Smog_Level": smog_level
    }])

    prediction = model.predict(data)
    st.success(f"Predicted CO2 Emission: {prediction[0]:.2f}")



    