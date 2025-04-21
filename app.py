import streamlit as st
import pickle
import numpy as np
import catboost


with open('Final_Diabetes_catboost_model.txt' , 'rb') as file:
          model = pickle.load(file)


st.sidebar.header("Diabetes Prediction")


pregnancies = st.sidebar.number_input('Enter the number of pregnancies', min_value=0)
glucose = st.sidebar.number_input('Enter the glucose level', min_value=0)
blood_pressure = st.sidebar.number_input('Enter the blood pressure', min_value=0)
skin_thickness = st.sidebar.number_input('Enter the skin thickness', min_value=0)
insulin = st.sidebar.number_input('Enter the insulin level', min_value=0)
bmi = st.sidebar.number_input('Enter the BMI', min_value=0.0)
pedigree = st.sidebar.number_input('Enter the diabetes pedigree function', min_value=0.0)
age = st.sidebar.number_input('Enter the age', min_value=0)


if st.button('Predict'):
    features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, pedigree, age]])
    prediction = model.predict_proba(features)[0][1]

    st.write(f'The predicted probability of diabetes is: **{prediction:.2f}**')

    if prediction >= 0.6:
        st.error('The person is likely to have diabetes.')
    else:
        st.success('The person is unlikely to have diabetes.')
