import streamlit as st
import joblib

model = joblib.load("Diabetes")

st.title("Diabetes Prediction")
    
    
# Diabetes Prediction Page

# getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Pregnancies = st.text_input('Number of Pregnancies')

with col2:
    Glucose = st.text_input('Glucose Level')

with col3:
    BloodPressure = st.text_input('Blood Pressure value')

with col1:
    SkinThickness = st.text_input('Skin Thickness value')

with col2:
    Insulin = st.text_input('Insulin Level')

with col3:
    BMI = st.text_input('BMI value')

with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

with col2:
    Age = st.text_input('Age of the Person')


# creating a button for Prediction

if st.button('Diabetes Test Result'):
    diab_prediction = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if (diab_prediction[0] == 1):
      st.success('The person is diabetic')
    else:
      st.success('The person is not diabetic')