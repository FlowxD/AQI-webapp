# -*- coding: utf-8 -*-
"""
Created on Fri May  7 13:33:37 2021

@author: Mandar 
"""
import streamlit as st
import pickle




model = pickle.load(open('xgb_AQI2.pkl', 'rb'))

#names = model.get_booster().feature_names






t = st.number_input('Enter Avg Temperature', min_value=0.0)
tmax = st.number_input('Enter Miximum Temperature', min_value=0.0)
tmin = st.number_input('Enter Minimum Temperature', min_value=0.0)
pha = st.number_input('Atmospheric pressure in hPa', min_value=0.0)
hum = st.number_input('Average Humidity in %', min_value=0.0)
vv  = st.number_input('Average Visibility', min_value=0.0)
v = st.number_input('Average Wind Speed', min_value=0.0)
vm = st.number_input('Maximum Sustained Speed', min_value=0.0)

if st.button('predict'):
    x = model.predict([[t,tmax,tmax,pha,hum,vv,v,vm]])

    st.write('Prediction for AQI PM2.5 is ')
    st.write(x)
