import streamlit as st
import pandas as pd

with st.form(key="autofinancement1"):
   titre = st.text_input("Titre:")
   inv = st.text_input("Investissement:")
   ca = float(st.text_input("Chiffre d\'affaire:"))
   vac = float(st.text_input("Vaiation du chiffre d'affaire en %"))
   ta = float(st.text_input("Taux d'amortissement en %"))
   ra = st.text_input("Régime d'amortissement", value="Linéaire")
   vr = float(st.text_input("Valeur résiduelle"))
   cf = float(st.text_input("Charges fixes"))
   cv = float(st.text_input("Charges variables en %"))
   bfr = float(st.text_input("Besoin en fond de roulement en %"))
   rbfr = float(st.text_input("Recupération du besoin en fond de roulement en %"))

   submissionButton = st.form_submit_button(label="Valider")
   if submissionButton==True:
      cvauto = (cv / 100) * ca
      amorti = (ta / 100) * inv
      rbrute = ca - cvauto - cf - amorti
      rnet = rbrute - (0.3 * rbrute)
      caf = rnet + amorti

      st.write('cvauto ' + str(cvauto))
      st.write('amorti ' + str(amorti))
      st.write('rbrute ' + str(rbrute))
      st.write('rnet ' + str(rnet))
      st.write('caf ' + str(caf))

      nbannee=5

      caList=[]
      cafList=[]
      bfrList=[]
      cafList.append("RAS")
      cafList.append(caf)
      caList.append(ca)
      for i in range(nbannee-2):
         ca = ca + ca * (vac / 100)
         caList.append(ca)
         cvauto = (cv / 100) * ca
         rbrute = ca - cvauto - cf - amorti
         rnet = rbrute - (0.3 * rbrute)
         caf = rnet + amorti
         cafList.append(caf)
      print(cafList)

      for i in range(nbannee-1):
         bfrList.append((bfr/100)*caList[i])


      for i in range(nbannee-2):
         rbfrList.append('RAS')




