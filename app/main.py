import streamlit as st

# App Title
st.title("Simple BMI Calculator")

# Input Fields
st.header("Enter Your Details")
weight = st.number_input("Weight (in kg)", min_value=0.0, step=0.1)
height = st.number_input("Height (in meters)", min_value=0.0, step=0.01)

# Calculate BMI
if height > 0:
    bmi = weight / (height ** 2)
    st.subheader("Your BMI:")
    st.write(f"{bmi:.2f}")

    # Display BMI Category
    st.subheader("BMI Category:")
    if bmi < 18.5:
        st.write("Underweight")
    elif 18.5 <= bmi < 24.9:
        st.write("Normal weight")
    elif 25 <= bmi < 29.9:
        st.write("Overweight")
    else:
        st.write("Obesity")
else:
    st.write("Please enter a valid height.")
