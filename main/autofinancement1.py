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
      cafList.append(0)
      cafList.append(caf)
      caList.append(float(ca))
      for i in range(1,nbannee):
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
      RbfrList=[]
      RbfrList = [0 for i in range(nbannee)]
      RbfrList.append(Rbfr)


      #Variation du besoin de fond de roulement

      Vbfr=[]
      Vbfr.append(bfrList[0])
      for i in range(1,nbannee):
         Vbfr.append(bfrList[i]-bfrList[i-1])
      Vbfr.append(0)
      print(Vbfr)

      #Valeur résiduelle
      ValResList=[]
      ValResList=[0 for i in range(nbannee)]
      ValResList.append(float(vr))

      #Total 1
      Total1=[]
      Total1=[float(cafList[i])+float(RbfrList[i])+float(ValResList[i]) for i in range(nbannee+1)]

      #Investissement
      InvestList=[]
      InvestList.append(float(inv))
      for i in range(1, nbannee+1):
         InvestList.append(0)

      #Total2
      Total2=[float(inv)-Vbfr[i] for i in range(nbannee)]
      Total2.append(0)

      FNT=[Total2[i]-Total1[i] for i in range(nbannee+1)]

      print(len(cafList))
      print(len(RbfrList))
      print(len(ValResList))
      print(len(Total1))
      print(len(InvestList))
      print(len(Vbfr))
      print(len(Total2))
      print(len(FNT))


      Resultat=[cafList,RbfrList,ValResList,Total1,InvestList,Vbfr,Total2,FNT]
      print(Resultat)
      df = pd.DataFrame(Resultat,index=["cafList", "RbfrList", "ValResList", "Total1", "InvestList", "Vbfr", "Total2", "FNT"])
      st.dataframe(df)

      #van
      Van=0
      for i in range(nbannee+1):
         Van=Van+(FNT[i]/pow(0.1+1,float(nbannee)))
      Van=Van-FNT[0]
      st.write(('Van ' + str(Van)))

      #IP
      Ip=(1+Van)/FNT[0]
      st.write(('Ip ' + str(Ip)))











