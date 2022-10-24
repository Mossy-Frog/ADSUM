import streamlit as st
import pandas as pd
import plotly.express as px


st.text_input('Email address')
st.radio('Pick your gender',['Male','Female'])
st.text_area('Input symptoms of the patient')
st.slider('Put a weight on the gravity of symptoms of the patient', 0,10)



#streamlit run mainstreamlit.py