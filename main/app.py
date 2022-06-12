import streamlit as st
from multiapp import MultiApp
from apps import home, autofinancement1,ammortissmentConstant,annC,incertain # import your app modules here

app = MultiApp()

st.markdown("""
# Trust & Invest
Bienvenue dans Trust & Invest, votre meilleure guide pour un choix d'investissement convenable à votre besoin et vision
""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Autofinancement", autofinancement1.app)
app.add_app("Ammortissement Constant", ammortissmentConstant.app)
app.add_app("Annuite Constante", annC.app)
app.add_app("Invesstissement dans un avenir incertain", incertain.app)
# The main app
app.run()