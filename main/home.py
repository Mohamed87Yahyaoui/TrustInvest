import streamlit as st

st.title("Trust & Invest")

menu = ["Home","Login","Register"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
	st.subheader("Home")

elif choice == "Login":
	from login import loginForm

elif choice == "Register":
	from register import *