import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt

# Load the trained model
with open("rainfall_model.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("🌦️ Annual Rainfall Prediction App ☔")

st.write("Enter the monthly rainfall data to predict annual rainfall and get risk warnings.")

# User Inputs
year = st.number_input("Year", value=2024, step=1)
jan = st.number_input("January Rainfall (mm)", value=0.0)
feb = st.number_input("February Rainfall (mm)", value=0.0)
mar = st.number_input("March Rainfall (mm)", value=0.0)
apr = st.number_input("April Rainfall (mm)", value=0.0)
may = st.number_input("May Rainfall (mm)", value=0.0)
jun = st.number_input("June Rainfall (mm)", value=0.0)
jul = st.number_input("July Rainfall (mm)", value=0.0)
aug = st.number_input("August Rainfall (mm)", value=0.0)
sep = st.number_input("September Rainfall (mm)", value=0.0)
oct = st.number_input("October Rainfall (mm)", value=0.0)
nov = st.number_input("November Rainfall (mm)", value=0.0)
dec = st.number_input("December Rainfall (mm)", value=0.0)

# Derived Features
jan_feb = jan + feb
mar_may = mar + apr + may
jun_sep = jun + jul + aug + sep
oct_dec = oct + nov + dec

# Predict Button
if st.button("Predict Annual Rainfall"):
    # Ensure features match model input (17 total)
    features = np.array([[year, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec, jan_feb, mar_may, jun_sep, oct_dec]])

    # Make Prediction
    prediction = model.predict(features)[0]

    # Display Result
    st.subheader(f"🌧️ Predicted Annual Rainfall: **{prediction:.2f} mm**")

    # Risk Warnings
    if prediction > 1500:
        st.warning("⚠️ High rainfall! Possible **flood risk**.")
    elif prediction < 1000:
        st.warning("⚠️ Low rainfall! Possible **drought risk**.")
    else:
        st.success("✅ Rainfall is within a **safe range**.")

    # 🌟 Visualization: Rainfall Bar Chart
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    rainfall_values = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(months, rainfall_values, color="royalblue")
    ax.set_xlabel("Months")
    ax.set_ylabel("Rainfall (mm)")
    ax.set_title(f"Monthly Rainfall for {year}")
    st.pyplot(fig)
