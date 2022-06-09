import streamlit as st
import hashlib
import sqlite3

def app():
   conn=sqlite3.connect('data.db', check_same_thread=False)
   cur=conn.cursor()


   def make_hashes(password):
	   return hashlib.sha256(str.encode(password)).hexdigest()
   # Giving a title

   def addDataRegister(fname, lname, email, password, gender, age, country):
      cur.execute("""CREATE TABLE IF NOT EXISTS USER(fname TEXT(50), lname TEXT(50), email TEXT(200), password TEXT(100), gender TEXT(10), age TEXT(3), country TEXT(15))""")
      cur.execute("INSERT INTO USER VALUES (?,?,?,?,?,?,?)", (fname, lname, email, make_hashes(password), gender, age, country))
      conn.commit()
      conn.close()



   with st.form(key="Sign up"):
      fname = st.text_input('First Name:')
      lname = st.text_input('Last Name:')
      email = st.text_input('Email:')
      password = st.text_input("Enter a password", type="password")
      conf_password = st.text_input('Confirm your password', type="password")
      gender = st.radio('Gender', ('Male', 'Female'))
      age = st.slider('Age:', 20, 90)

      countryList = ["Morocco", "France", "USA"]
      country = st.selectbox("Country", countryList)
      if password == conf_password:
         pass
      else:
         st.warning("password do not match with confirm password")

      submissionButton = st.form_submit_button(label="Sign up")
      if submissionButton == True:
         print("hello")
         addDataRegister(fname, lname, email, password, gender, age, country)
         print("hello")
         st.success("Succedssfully registred, please try login into your account")



