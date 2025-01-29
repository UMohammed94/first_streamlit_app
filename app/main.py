import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
# todo clean up the files 
# File to save user data
data_file = Path("user_bmi_data.csv")

# Function to load or create the data file
def load_data():
    if data_file.exists():
        return pd.read_csv(data_file)
    else:
        return pd.DataFrame(columns=["Weight", "Height", "BMI"])

# Function to save new entry to the data file
def save_data(weight, height, bmi):
    data = load_data()
    new_entry = {"Weight": weight, "Height": height, "BMI": bmi}
    data = pd.concat([data, pd.DataFrame([new_entry])], ignore_index=True)
    data.to_csv(data_file, index=False)

# Add a blue banner at the top
st.markdown(
    """
    <style>
    .blue-banner {
        background-color: #007BFF;
        color: white;
        padding: 10px;
        font-size: 20px;
        text-align: center;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    </style>
    <div class="blue-banner">BMI Calculator and Tracker 📊</div>
    """,
    unsafe_allow_html=True
)

# Main app
st.title("BMI Calculator")

# User inputs
weight = st.number_input("Enter your weight (in kg)", min_value=0.0, step=0.1)
height = st.number_input("Enter your height (in meters)", min_value=0.0, step=0.01)

if weight > 0 and height > 0:
    bmi = weight / (height ** 2)
    st.success(f"Your BMI is: {bmi:.2f}")
    
    # Save the data
    if st.button("Save Data"):
        save_data(weight, height, bmi)
        st.success("Your data has been saved!")

# Display historical data
st.header("Historical Data")
data = load_data()

if not data.empty:
    st.dataframe(data)

    # Plot data
    st.header("Visualize Your Progress")
    fig, ax = plt.subplots()
    ax.plot(data["BMI"], label="BMI", marker="o", linestyle="--", color="blue")
    ax.set_xlabel("Entry Number")
    ax.set_ylabel("BMI")
    ax.set_title("BMI Progress Over Time")
    ax.legend()
    st.pyplot(fig)
else:
    st.info("No data available. Save your first entry!")
