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
#create function submit
#voir un code type sikitleanr pour comprendre comment commenter 
#faire un schema user story tout ce que l'utilisateur peut faire avec l'application
#faire un tableau de bord genre feuille excel, c'est à dire le temps qu'on a passé à faire quoi, voir le chemin
#faire fonctionner le backend et le front end ensemble