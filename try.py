# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, label_binarize
from sklearn.model_selection import KFold
import warnings
warnings.filterwarnings("ignore")
import pickle

def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:5px"> 
    <h1 style ="color:black;text-align:center;">Contact </h1> 
    </div> 
    """
    
     # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 


st.sidebar.header('User Input Parameters')

shi = pd.read_csv('C:/Users/Hp/Downloads/New completed/shivamogga.csv')

def user_input_features():
    DISTRICT =  st.sidebar.selectbox('District',shi.DISTRICT.unique())
    CHARGE_NAME =  st.sidebar.selectbox('CHARGE NAME',shi.CHARGE_NAME.unique())
    All =  st.sidebar.selectbox('R/U/D',shi.All.unique())
    Name =  st.sidebar.selectbox('Name',shi.Name.unique())
    Official_Designation =  st.sidebar.selectbox('Official_Designation',shi.Official_Designation.unique())
    Census_Designation  =  st.sidebar.selectbox('Census_Designation',shi.Census_Designation.unique())
    Mobile_Number  =  st.sidebar.selectbox('Mobile_Number',shi.Mobile_Number.unique())
    mail  =  st.sidebar.selectbox('e-mail',shi.mail.unique())

    data = {'DISTRICT':DISTRICT,
            'CHARGE_NAME':CHARGE_NAME,
            'All':All,
            'Name':Name,
            'Official_Designation':Official_Designation,
            'Census_Designation':Census_Designation,
            'Mobile_Number':Mobile_Number,
            'mail':mail,}
    features = pd.DataFrame(data,index = [0])
    return features 
    
df = user_input_features()

if __name__=='__main__': 
    main()

