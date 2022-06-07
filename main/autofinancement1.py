import streamlit as st

with st.form(key="autofinancement1"):
   titre = st.text_input("Titre:")
   investissement = st.text_input("Investissement:")
   ca = st.text_input("Chiffre d\'affaire:")
   vac = st.text_input("Vaiation du chiffre d'affaire")
   ta = st.text_input("Taux d'amortissement")
   ra = st.text_input("Régime d'amortissement")
   vr = st.text_input("Valeur résiduelle")
   cf = st.text_input("Charges fixes")
   cv = st.text_input("Charges variables")

   submissionButton = st.form_submit_button(label="Valider")