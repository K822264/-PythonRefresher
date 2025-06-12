import pickle # Used to load our ML model - model.pkl
import numpy as np
import streamlit as st # Main library used to create interactive apps 

model = pickle.load(open('model.pkl', 'rb'))
# this loads the trained model from the file model.pkl
# 'rb'- binary read mode to read our pickle file since it is in a binary format

col0, col1, col2, col3, col4, col5, col6 = st.columns(7) 
# st.columns to arrange the elements horizontally
with col0:
    st.write('')
with col1:
    st.write('')
with col2:
    st.write('')    
with col3: 
    st.title("ⴍage") # places the title(wage) at the center of the web page


with col4:
    st.write('')
with col5:
    st.write('')
with col6:
    st.write('')

col7, col8, col9 = st.columns(3)
with col7:
    st.write('')    
with col8:
    st.markdown("<h6 style='text-align: center;'>A simple web app to predict annual salary</h6>", unsafe_allow_html=True)
# Places the subtitles below the title, this uses a HTML format
with col9:
    st.write('')
    
# Predefined list for gender, education,job found in the dataset
gen_list = ["Female", "Male"]
edu_list = ["Bachelor's", "Master's", "PhD"]
job_list = ["Director of Marketing", "Director of Operations", "Senior Data Scientist", "Senior Financial Analyst", "Senior Software Engineer"]

job_idx = [0, 1, 10, 11, 20] # Job_index contains integers that represent each job title

# st.radio (radio buttons), user selects one option
gender = st.radio('Pick your gender', gen_list)

# st.slider shows a slider to select the age
age = st.slider('Pick your age', 21, 55)

# st.selectbox, displays a dropdown menu
education = st.selectbox('Pick your education level', edu_list)
job = st.selectbox('Pick your job title', job_list)
experience = st.slider('Pick your years of experience', 0.0, 25.0, 0.0, 0.5, "%1f")

col10, col11, col12, col13, col14 = st.columns(5)
with col10:
    st.write('')
with col11:
    st.write('')    
with col12:
    predict_btn = st.button('Predict Salary') # Places the predict salary button at the center of the page
with col13:
    st.write('')
with col14:
    st.write('')

# This converts all inputs from the user to numeric (int or float) which the model understands
if(predict_btn):
    inp1 = int(age)
    inp2 = float(experience)
    inp3 = int(job_idx[job_list.index(job)])
    inp4 = int(edu_list.index(education))
    inp5 = int(gen_list.index(gender))
    X = [inp1, inp2, inp3, inp4, inp5]
    salary = model.predict([X]) # This predicts the salary based on the variable X 
    col15, col16, col17 = st.columns(3)
    with col15:
        st.write('')    
    with col16:
        st.text(f"Estimated salary: ${int(salary[0])}") # Displays the predicted salary at the center of the screen

    with col17:
        st.write('')



