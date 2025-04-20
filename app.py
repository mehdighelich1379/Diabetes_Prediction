import streamlit as st
import pickle
import numpy as np


with open(r'C:\Users\T A T\project\Machin Learning\classification project\Diabetes\models\Final_Diabetes_catboost_model.txt' , 'rb') as file:
          model = pickle.load(file)


st.title('Diabetes Prediction')


pregnancies = st.number_input('Enter the number of pregnancies', min_value=0)
glucose = st.number_input('Enter the glucose level', min_value=0)
blood_pressure = st.number_input('Enter the blood pressure', min_value=0)
skin_thickness = st.number_input('Enter the skin thickness', min_value=0)
insulin = st.number_input('Enter the insulin level', min_value=0)
bmi = st.number_input('Enter the BMI', min_value=0.0)
pedigree = st.number_input('Enter the diabetes pedigree function', min_value=0.0)
age = st.number_input('Enter the age', min_value=0)


if st.button('Predict'):
    features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, pedigree, age]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.write('The person is likely to have diabetes.')
    else:
        st.write('The person is unlikely to have diabetes.')
