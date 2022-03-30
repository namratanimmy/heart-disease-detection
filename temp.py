# -*- coding: utf-8 -*-
import numpy as np
import pickle
import pandas as pd
import streamlit as st 
import os
import base64
from PIL import Image

pickle_in=open("model.pkl","rb")
model=pickle.load(pickle_in)



def welcome():
    return "Welcome All"


def predict(age,trestbps,chol,fbs,restecg,thalach,oldpeak,ca,sex_Male,cp_atypical_angina,cp_non_anginal_pain,cp_typical_angina,exang_exercise_induced_angina,slope_upsloping,thal_normal,thal_reversable_defect):
    prediction=model.predict([[age,trestbps,chol,fbs,restecg,thalach,oldpeak,ca,sex_Male,cp_atypical_angina,cp_non_anginal_pain,cp_typical_angina,exang_exercise_induced_angina,slope_upsloping,thal_normal,thal_reversable_defect]])
    print(prediction)
    return prediction


def main():
    html_temp = """
    <div style="font-style: italic;font:Sans-serif;padding:10px">
    <h2 style="color:white;text-align:left;font-size:54px">HEART DISEASE DETECTION</h2>
    </div>
    """

    
    st.markdown(html_temp,unsafe_allow_html=True)
    img = Image.open("image.png")
    st.image(img, width=600)
    st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)
    age = st.text_input("age")
    trestbps = st.text_input("blood pressure(mm Hg)")
    chol = st.text_input("cholestrol")
    fbs = st.text_input("fasting blood sugar >120mg/dl ?")
    restecg=st.text_input("resting electrocardiographic res (0,1,2)")
    thalach=st.text_input("max heart rate")
    oldpeak=st.text_input("oldpeak")
    ca=st.text_input("no of major vessesls(0,1,2,3)")
    sex_Male=st.text_input("sex(male-1,female-0)")
    cp_atypical_angina=st.text_input("cp_atypical angina?")
    cp_non_anginal_pain=st.text_input("cp_non-anginal pain?")
    cp_typical_angina=st.text_input("typical angina?")
    exang_exercise_induced_angina=st.text_input("exercise induced angina?")
    slope_upsloping=st.text_input("slope of peak exercise ST segment upsloping?")
    thal_normal=st.text_input("normal blood flow?")
    thal_reversable_defect=st.text_input("blood flow is observed but not normal?")
    result=""
    if st.button("PREDICT HEART DISEASE"):
        result=predict(age,trestbps,chol,fbs,restecg,thalach,oldpeak,ca,sex_Male,cp_atypical_angina,cp_non_anginal_pain,cp_typical_angina,exang_exercise_induced_angina,slope_upsloping,thal_normal,thal_reversable_defect)
    st.success('HEART DISEASE -- {}'.format(result))
 
    

     
    
if __name__=='__main__':
    main()


