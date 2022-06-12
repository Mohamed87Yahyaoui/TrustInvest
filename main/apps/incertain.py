import streamlit as st
import pandas as pd
def app():
   with st.form(key="incertain"):
      st.write("Marché Stable")
      AutofinancementS = st.text_input("Van Autofinancement:")
      Amortissement_ConstantS = st.text_input("Van Amortissement Constant:")
      Annuité_ConstanteS= st.text_input("Van Annuité_Constante:")

      st.write("Marché Défavorable")
      AutofinancementD = st.text_input("Van Autofinancement:")
      Amortissement_ConstantD = st.text_input("Van Amortissement Constant:")
      Annuité_ConstanteD = st.text_input("Van Annuité_Constante:")


      st.write("Marché favorable")
      AutofinancementF = st.text_input("Van Autofinancement:")
      Amortissement_ConstantF = st.text_input("Van Amortissement Constant:")
      Annuité_ConstanteF = st.text_input("Van Annuité_Constante:")

      submissionButton = st.form_submit_button(label="Valider")
      if submissionButton == True:
          ListAuto=[float(AutofinancementS),float(AutofinancementD),float(AutofinancementF)]
          ListAmor=[float(Amortissement_ConstantS ),float(Amortissement_ConstantD),float(Amortissement_ConstantF)]
          ListAnn=[float(Annuité_ConstanteS),float(Annuité_ConstanteD),float(Annuité_ConstanteF)]



      #Critère du MAXIMIN
          minAuto=min(ListAuto)
          minAmor=min(ListAmor)
          minAnn=min(ListAnn)
          maximin=max(minAuto,minAmor,minAnn)

      #Critère du MAXIMAX
          maxAuto = max(ListAuto)
          maxAmor = max(ListAmor)
          maxAnn = max(ListAnn)
          maximax = max(maxAuto, maxAmor, maxAnn)

      #Critère du MINIMAX
          maxAuto = max(ListAuto)
          maxAmor = max(ListAmor)
          maxAnn = max(ListAnn)
          min(maxAuto, maxAmor, maxAnn)

      #Critère de Laplace
          moyAuto =(float(AutofinancementS)+float(AutofinancementD)+float(AutofinancementF))/3
          moyAmor = (float(Amortissement_ConstantS) + float(Amortissement_ConstantD) + float(Amortissement_ConstantF))/3
          moyAnn = (float(Annuité_ConstanteS) + float(Annuité_ConstanteD) + float(Annuité_ConstanteF))/3
          max(moyAuto, moyAmor, moyAnn)

      #Critère de Savage
          maxMarche1=max(float(AutofinancementS),float(Amortissement_ConstantS ),float(Annuité_ConstanteS))
          maxMarche2 = max(float(AutofinancementD), float(Amortissement_ConstantD), float(Annuité_ConstanteD))
          maxMarche3 = max(float(AutofinancementF), float(Amortissement_ConstantF), float(Annuité_ConstanteF))
          ListAutoSavage = [maxMarche1-float(AutofinancementS),maxMarche1- float(AutofinancementD),maxMarche1- float(AutofinancementF)]
          ListAmorSavage = [maxMarche2-float(Amortissement_ConstantS),maxMarche2- float(Amortissement_ConstantD), maxMarche2-float(Amortissement_ConstantF)]
          ListAnnSavage = [maxMarche3-float(Annuité_ConstanteS),maxMarche3- float(Annuité_ConstanteD), maxMarche3-float(Annuité_ConstanteF)]
          regretAuto=max(ListAutoSavage)
          regretAmort=max(ListAmorSavage)
          regretAnn=max(ListAnnSavage)
          min(regretAuto, regretAmort, regretAnn)