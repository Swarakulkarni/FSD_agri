# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 16:23:39 2022

@author: Erum Parkar
"""

#libraries
import streamlit as st
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#models
W = joblib.load("D:/Login_Register_Agriconnect/streamlit/Weather.pkl")
lm = pd.read_csv("D:/Login_Register_Agriconnect/streamlit/weatherHistory_LabelMapping(Summary).csv")

def prediction(Precip_Type,Temperature,Humidity,Wind_Speed,Visibility,Pressure):  
   
    wd = pd.read_csv("D:/Login_Register_Agriconnect/streamlit/weatherHistory_Preprocessed(NOT STANDARDIZED).csv")
    X = wd.drop(columns=['Summary'])
    Y = wd['Summary']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, random_state = 42)
    scale= StandardScaler()
    scale.fit(X_train) 
    X_train = scale.transform(X_train) 
    X_test = scale.transform(X_test) 
   
    pre =[[Precip_Type,Temperature,Humidity,Wind_Speed,Visibility,Pressure]]
    pre = scale.transform(pre)
    print(pre)
    prediction = W.predict(pre)
    print(prediction)
    return prediction

def main():

      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:green;padding:13px">
    <h1 style ="color:black;text-align:center;"> Weather Prediction ML Model </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    Precip_Type = st.number_input("Precip Type")
    Temperature = st.number_input("Temperature (C)")
    Humidity = st.number_input("Humidity")
    Wind_Speed = st.number_input("Wind Speed (km/h)")
    Visibility = st.number_input("Visibility (km)")
    Pressure = st.number_input("Pressure (millibars)")
    result =""
         
    Precip_Type = float(Precip_Type)
    Temperature = float(Temperature)
    Humidity = float(Humidity)
    Wind_Speed = float(Wind_Speed)
    Visibility = float(Visibility)
    Pressure = float(Pressure)
    
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        r = prediction(Precip_Type,Temperature,Humidity,Wind_Speed,Visibility,Pressure)
        i = r[0]
        result = lm.iloc[i]
        print(result.values)
        s = str(result.values)
        s = s[2:-2]
        # df1 = df[df.Climate.apply(lambda x: x == s)]
        st.success('The output is {}'.format(s))

    
   
if __name__=='__main__':
    main()