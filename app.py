import streamlit as st
import joblib

model=joblib.load('dementia_model.pk1')

st.title('Dementia Risk Predictor')
                
