import streamlit as st # Imports the streamlit library
import datetime # This is a python Library that works with date and time

st.set_page_config(page_title="Semester Project App")
# the streamlit function(.set_page_config), establishes the web page
st.title("Title: Bio Data") # Displays a large bold title at the head of the web app
st.write("This is a sample web app.") # This writes a normal sentence  of text on the web page.

first_name = st.text_input("First Name") #This adds a text input field labeled "First Name"
                                          #The user's input is stored in the variable (first_name)
last_name = st.text_input("Last Name") # Adds a text input field labeled 'Last Name'
                                       # The user's input is stores in the variable (last_name)
                                       
gender = st.selectbox("Gender", ["Male", "Female"]) 
#(.selectbox, creates a drop-down menu, that gives the user to select one option only, male or female)
age = st.number_input("Your Age", 0,100,30,1) 
# Creates a input box, min_age = 0, max_age = 100, default_age = 30, increase or decrease by 1

DOB = st.date_input("Your Birthday", value=datetime.date(2000, 1, 1), min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2025, 12, 31))
 # (.date_input); a streamlit function that displays a calendar, then stored in DOB
# value =  the default datetime, that appears before the user inputs any
# min_value = the minimum datetime the program will allow
# max_value = the maximum datetime the program will allow

Marital_status = st.radio("Marital Status", ["Single", "Married"])
# the function ().radio) that allows the user to chooce only one option ( radio buttons)
# the inputs from the user is stored in the variable (Marital_status)

Years_of_experience = st.slider("Years of experience", 0, 40)  
# the streamlit function (.slider) allows the user to slide from left or right to select between 0-40
# The input is store in the variable ( Year_of_experience)                      




