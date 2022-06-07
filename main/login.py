import streamlit as st
import sqlite3
import hashlib

conn=sqlite3.connect('data.db', check_same_thread=False)
cur=conn.cursor()

def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def login_user(username,password):
	conn.execute('SELECT * FROM USER WHERE email =? AND password = ?',(email,make_hashes(password)))
	data = cur.fetchall()
	return data


with st.form(key="login"):
   email = st.text_input('Email:')
   password = st.text_input("Enter a password", type="password")

   submissionButton = st.form_submit_button(label="Sign up")
   if submissionButton == True:
      user=login_user(email,make_hashes(password))
      print(user)
      if user:
         print(user)
         st.success("Logged In as {}".format(user.fname+user.lname))
         from auto import *




