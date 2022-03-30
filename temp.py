# -*- coding: utf-8 -*-
import numpy as np
import pickle
import pandas as pd
import streamlit as st 
import os



pickle_in=open("F:\clg\project heart\model.pkl","rb")
model=pickle.load(pickle_in)



def welcome():
    return "Welcome All"


def predict_stock(age,trestbps,chol,fbs,restecg,thalach,oldpeak,ca,sex_Male,cp_atypical_angina,cp_non_anginal_pain,cp_typical_angina,exang_exercise_induced_angina,slope_upsloping,thal_normal,thal_reversable_defect):
    prediction=model.predict([[age,trestbps,chol,fbs,restecg,thalach,oldpeak,ca,sex_Male,cp_atypical_angina,cp_non_anginal_pain,cp_typical_angina,exang_exercise_induced_angina,slope_upsloping,thal_normal,thal_reversable_defect]])
    print(prediction)
    return prediction


def main():
 
    html_temp = """
    <div style="background-color:black;padding:10px">
    <h2 style="color:white;text-align:center;">MPG Prediction Using Streamlit </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("age")
    trestbps = st.text_input("trestbps")
    chol = st.text_input("chol")
    fbs = st.text_input("fbs")
    restecg=st.text_input("restecg")
    thalach=st.text_input("thalach")
    oldpeak=st.text_input("oldpeak")
    ca=st.text_input("ca")
    sex_Male=st.text_input("sex_Male")
    cp_atypical_angina=st.text_input("cp_atypical angina")
    cp_non_anginal_pain=st.text_input("cp_non-anginal pain")
    cp_typical_angina=st.text_input("cp_typical angina")
    exang_exercise_induced_angina=st.text_input("exang_exercise induced angina")
    slope_upsloping=st.text_input("slope_upsloping")
    thal_normal=st.text_input("thal_normal")
    thal_reversable_defect=st.text_input("thal_reversable defect")
   
    result=""
    if st.button("Predict"):
        result=predict_stock(age,trestbps,chol,fbs,restecg,thalach,oldpeak,ca,sex_Male,cp_atypical_angina,cp_non_anginal_pain,cp_typical_angina,exang_exercise_induced_angina,slope_upsloping,thal_normal,thal_reversable_defect)
    st.success('The output is {}'.format(result))
    

     
    
if __name__=='__main__':
    main()


