import streamlit as st
# Giving a title

def registerForm():

# creating a form
   my_form_register=st.form(key='register')

   fname=my_form_register.text_input('First Name:')
   lname=my_form_register.text_input('Last Name:')
   email=my_form_register.text_input('Email:')
   password=my_form_register.text_input("Enter a password", type="password")

   gender=my_form_register.radio('Gender',('Male','Female'))

   age=my_form_register.slider('Age:',20,90)

   countryList = ["Morocco","France","USA"]
   country=my_form_register.selectbox("Country",countryList)

   submit=my_form_register.form_submit_button('Register')
# the following gets updated after clicking on submit, printing the details of the fields that are submitted in the form

registerForm()