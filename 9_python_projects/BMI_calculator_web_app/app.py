import streamlit as st


st.write("# BMI Calculator")

st.write("## Calculate your Body Mass Index (BMI)")

weight = st.slider("Enter Your Weight (in kg)", 30,200,70)
height = st.slider("Enter Your Height (in cm)", 100,250,170)

if st.button("Calculate BMI"):
        bmi = weight / ((height / 100) ** 2)
        st.write("Your BMI is:", round(bmi, 2))
        st.balloons()


st.write("## BMI Categories")
st.write("1. Underweight: BMI < 18.5")
st.write("2. Normal weight: 18.5 ≤ BMI < 24.9")
st.write("3. Overweight: 25 ≤ BMI < 29.9")
st.write("4. Obesity: BMI ≥ 30")
