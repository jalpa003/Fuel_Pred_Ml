# This app was adapted from this source: https://github.com/krishnaik06/Dockers/blob/master/app.py
# Streamlit documentation: https://docs.streamlit.io/

# Load Libraries----------------
import numpy as np
import sklearn
import pickle
import pandas as pd
import streamlit as st 

# Import the Model--------------
pickle_in = open("rf.pkl","rb")
rf = pickle.load(pickle_in)


# A function to predict price------------------------------------------
def predict_Conventional_Fuel(Eng_Displ,Cyl,Gears,Gasoline,Intake_Valves,Exhaust_Valves):
    prediction = rf.predict([[Eng_Displ,Cyl,Gears,Gasoline,Intake_Valves,Exhaust_Valves]])
    print(prediction)
    return prediction


# User Interface--------------------------------------------------------
def main():
    st.title("Conventional Fuel Prediction")
    Eng_Displ = st.text_input("Eng_Displ","Type Here")
    Cyl = st.text_input("# Cyl","Type Here")
    Gears = st.text_input("# Gears","Type Here")
    Gasoline = st.text_input("Max Ethanol % - Gasoline ", "Type Here")
    Intake_Valves = st.text_input("Intake Valves Per Cyl","Type Here")
    Exhaust_Valves = st.text_input("Exhaust Valves Per Cyl","Type Here")
    
    result=""
    if st.button("Predict"):
        result=predict_Conventional_Fuel(Eng_Displ,Cyl,Gears,Gasoline,Intake_Valves,Exhaust_Valves)
        st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()