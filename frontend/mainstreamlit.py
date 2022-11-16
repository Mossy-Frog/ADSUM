import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import json

st.title("Welcome to the ADSUM app")

#Creates the variables input by the user
patient_name =st.text_area('Give name of the patient')
age = st.slider('Put the age of the patient', 0,100)
weight = st.slider('Put a weight on the gravity of symptoms of the patient', 0,10)
symptoms = st.text_area('Input symptoms of the patient')


param = st.text_area('Input one parameter of the patient for a search')

AIsymptoms = st.text_area('Input symptoms of a patient to launch the AI')



#Put the variables into dictionnaries understable for the backend

inputsadd = {"patient_name" : patient_name, "age" : age, "weight" : weight, "symptoms" : symptoms }
inputsshow = {"param" : param}


inputsAI = {"AIsymptoms" : AIsymptoms}



#Buttons created to launch the functions

if st.button("Add patient"):
    res = requests.post(url = "http://127.0.0.1:8000/add", data = json.dumps(inputsadd) )
    st.subheader(f"Response from api = {res.text}")

if st.button("show patient"):
    res = requests.post(url = "http://127.0.0.1:8000/show", data = json.dumps(inputsshow) )
    st.subheader(f"Response from api = {res.text}")

if st.button("Launch AI"):
    res = requests.post(url = "http://127.0.0.1:8000/AI", data = json.dumps(inputsAI) )
    st.subheader(f"Response from api = {res.text}")

#cd Desktop/BT5/ADSUM/frontend
#streamlit run mainstreamlit.py
#to run the code, do it after the backend
