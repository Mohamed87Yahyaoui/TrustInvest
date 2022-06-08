import streamlit as st
import pandas as pd

with st.form(key="autofinancement1"):
   titre = st.text_input("Titre:")
   inv = st.text_input("Investissement:")
   ca = st.text_input("Chiffre d'affaire:")
   vac = st.text_input("Vaiation du chiffre d'affaire en %")
   ta = st.text_input("Taux d'amortissement en %")
   ra = st.text_input("Régime d'amortissement", value="Linéaire")
   vr = st.text_input("Valeur résiduelle")
   cf = st.text_input("Charges fixes")
   cv = st.text_input("Charges variables en %")
   bfr = st.text_input("Besoin en fond de roulement en %")
   rbfr = st.text_input("Recupération du besoin en fond de roulement en %")

   submissionButton = st.form_submit_button(label="Valider")
   if submissionButton==True:
      cvauto = (float(cv) / 100) * float(ca)
      amorti = (float(ta) / 100) * float(inv)
      rbrute = float(ca) - cvauto - float(cf) - amorti
      rnet = rbrute - (0.3 * rbrute)
      caf = rnet + amorti

      st.write('cvauto ' + str(cvauto))
      st.write('amorti ' + str(amorti))
      st.write('rbrute ' + str(rbrute))
      st.write('rnet ' + str(rnet))
      st.write('caf ' + str(caf))

      nbannee = 5

      caList = []
      cafList = []
      bfrList = []
      cafList.append("RAS")
      cafList.append(caf)
      caList.append(float(ca))
      for i in range(nbannee - 1):
         ca = float(ca) + float(ca) * (float(vac) / 100)
         caList.append(ca)
         cvauto = (float(cv) / 100) * float(ca)
         rbrute = float(ca) - cvauto - float(cf) - amorti
         rnet = rbrute - (0.3 * rbrute)
         caf = rnet + amorti
         cafList.append(caf)
      print(cafList)

      #Reccup bfr
      Sbfr=0
      for i in range(nbannee):
         bfrList.append((float(bfr) / 100) * caList[i])
         Sbfr=bfrList[i]+Sbfr

      Rbfr=Sbfr*float(rbfr)
      print(Rbfr)

      #Variation du besoin de fond de roulement

      Vbfr=[]
      Vbfr.append(bfrList[0])
      for i in range(1,nbannee):
         Vbfr.append(bfrList[i]-bfrList[i-1])

      print(Vbfr)

      #van










