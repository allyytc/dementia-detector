import streamlit as st
import joblib

model=joblib.load('dementia_model.pk1')

st.title('Dementia Risk Predictor')
age=st.slider('Age', min_value=18, max_value=120, value=75)
MMSE= st.slider('MMSE', min_value=0, max_value=30, value=25)
EDUC= st.slider('EDUC', min_value=0, max_value=23, value=12)
SES= st.slider('SES', min_value=1, max_value=5, value=3)
eTIV= st.slider('eTIV (Brain Volume)', min_value=1000, max_value=2500, value=1600)
nWBV= st.slider('nWBV (Normalized Brain Volume)', min_value=0.6, max_value=0.9, value=0.72)
ASF=st.slider('ASF (Atlas Scaling Factor', min_value=0.8, max_value=1.5, value=1.0)
sex = st.selectbox('Sex', options=[1, 0], format_func=lambda x: 'Male' if x == 1 else 'Female')
