import streamlit as st

def loginForm():

# creating a form
   my_form_login=st.form(key='login')
# creating input fields
   email=my_form_login.text_input('Email:')
   password=my_form_login.text_input("Enter a password", type="password")
# creating radio button

   submit=my_form_login.form_submit_button('login')

loginForm()