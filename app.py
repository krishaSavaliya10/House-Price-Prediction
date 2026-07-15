import streamlit as st
import pandas as pd
import joblib

model = joblib.load("house_price_model.pkl")

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction")
st.write("Enter the house details below and click Predict.")


area = st.number_input("Area (sq.ft)", min_value=500, max_value=10000, value=1500)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
floors = st.number_input("Floors", min_value=1, max_value=5, value=2)
house_age = st.number_input("House Age (Years)", min_value=0, max_value=100, value=5)
garage = st.number_input("Garage", min_value=0, max_value=5, value=1)
parking = st.number_input("Parking", min_value=0, max_value=10, value=2)

location = st.selectbox(
    "Location",
    ["Urban", "Suburban", "Rural"]
)

furnished = st.selectbox(
    "Furnished",
    ["Yes", "No"]
)

garden = st.selectbox(
    "Garden",
    ["Yes", "No"]
)

condition = st.selectbox(
    "Condition",
    ["Poor", "Average", "Good", "Excellent"]
)

distance = st.number_input(
    "Distance to City (km)",
    min_value=0.0,
    max_value=100.0,
    value=10.0
)


location_map = {
    "Rural": 0,
    "Suburban": 1,
    "Urban": 2
}

furnished_map = {
    "No": 0,
    "Yes": 1
}

garden_map = {
    "No": 0,
    "Yes": 1
}

condition_map = {
    "Average": 0,
    "Excellent": 1,
    "Good": 2,
    "Poor": 3
}

input_data = pd.DataFrame({
    "Area_sqft":[area],
    "Bedrooms":[bedrooms],
    "Bathrooms":[bathrooms],
    "Floors":[floors],
    "House_Age":[house_age],
    "Garage":[garage],
    "Parking":[parking],
    "Location":[location_map[location]],
    "Furnished":[furnished_map[furnished]],
    "Garden":[garden_map[garden]],
    "Condition":[condition_map[condition]],
    "Distance_to_City_km":[distance]
})

if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Estimated House Price: ₹ {prediction[0]:,.2f}")
