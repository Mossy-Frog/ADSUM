import streamlit as st
import pandas as pd
import plotly.express as px


email = st.text_input('Email address')
gender = st.radio('Pick your gender',['Male','Female'])
symptoms = st.text_area('Input symptoms of the patient')
weight = st.slider('Put a weight on the gravity of symptoms of the patient', 0,10)

list_patient = []
list_patient += [email,gender,symptoms,weight]
print(list_patient)

#streamlit run mainstreamlit.py