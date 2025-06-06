import streamlit as st

st.set_page_config(page_title="Semester Project App")

st.title("🎓 Semester Project Web App")
st.write("Welcome! This is our interactive web app for the semester project.")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello, {name}! Thanks for using our app.")
