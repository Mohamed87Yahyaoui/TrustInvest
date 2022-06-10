import streamlit as st
from multiapp import MultiApp
from apps import home, register, login,autofinancement1,ammortissmentConstant,annC # import your app modules here

app = MultiApp()

st.markdown("""
# Trust & Invest
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Register", register.app)
app.add_app("Login", login.app)
app.add_app("Autofinancement", autofinancement1.app)
app.add_app("Ammortissement Constant", ammortissmentConstant.app)
app.add_app("Annuite Constante", annC.app)
# The main app
app.run()