import streamlit as st

# Set page configuration
st.set_page_config(page_title="BMI Calculator", layout="centered")

# Title
st.title("💪 BMI Calculator")
st.write("Calculate your Body Mass Index easily.")

# Inputs
name = st.text_input("Enter your name:")
height = st.number_input("Enter your height in meters:", min_value=0.1, format="%.2f")
weight = st.number_input("Enter your weight in kilograms:", min_value=1)

# BMI Calculation
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"### {name}'s BMI is: **{bmi:.2f}**")

        # Result Category
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Height must be greater than 0.")
