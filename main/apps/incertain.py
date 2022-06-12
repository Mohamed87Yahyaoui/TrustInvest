import streamlit as st
import pandas as pd
def app():
   with st.form(key="incertain"):
      st.write("Marché Stable")
      AutofinancementS = st.text_input("Van Autofinancement marché 1:")
      Amortissement_ConstantS = st.text_input("Van Amortissement Constant marché 1 :")
      Annuité_ConstanteS= st.text_input("Van Annuité Constante marché 1 :")

      st.write("Marché Défavorable")
      AutofinancementD = st.text_input("Van Autofinancement marché 2 :")
      Amortissement_ConstantD = st.text_input("Van Amortissement Constant marché 2 :")
      Annuité_ConstanteD = st.text_input("Van Annuité Constante marché 2 :")


      st.write("Marché favorable")
      AutofinancementF = st.text_input("Van Autofinancement marché 3 :")
      Amortissement_ConstantF = st.text_input("Van Amortissement Constant marché 3 :")
      Annuité_ConstanteF = st.text_input("Van Annuité Constante marché 3 :")

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

          if maximin==minAuto:
              meilleureChoix="Autofinancement"
          elif maximin==minAmor:
              meilleureChoix = "Ammorticement constant"
          else:
              meilleureChoix = "Annuité constante"
          st.write("Selon le critère MAXIMIN, la meilleure stratégie est : "+meilleureChoix)



      #Critère du MAXIMAX
          maxAuto = max(ListAuto)
          maxAmor = max(ListAmor)
          maxAnn = max(ListAnn)
          maximax = max(maxAuto, maxAmor, maxAnn)

          if maximax==maxAuto:
              meilleureChoix="Autofinancement"
          elif maximax==maxAmor:
              meilleureChoix = "Ammorticement constant"
          else:
              meilleureChoix = "Annuité constante"
          st.write("Selon le critère MAXIMAX, la meilleure stratégie est : "+meilleureChoix)

      #Critère du MINIMAX
          maxAuto = max(ListAuto)
          maxAmor = max(ListAmor)
          maxAnn = max(ListAnn)
          minimax=min(maxAuto, maxAmor, maxAnn)

          if minimax==maxAuto:
              meilleureChoix="Autofinancement"
          elif minimax==maxAmor:
              meilleureChoix = "Ammorticement constant"
          else:
              meilleureChoix = "Annuité constante"
          st.write("Selon le critère MINIMAX, la meilleure stratégie est : "+meilleureChoix)

      #Critère de Laplace
          moyAuto =(float(AutofinancementS)+float(AutofinancementD)+float(AutofinancementF))/3
          moyAmor = (float(Amortissement_ConstantS) + float(Amortissement_ConstantD) + float(Amortissement_ConstantF))/3
          moyAnn = (float(Annuité_ConstanteS) + float(Annuité_ConstanteD) + float(Annuité_ConstanteF))/3
          laplace=max(moyAuto, moyAmor, moyAnn)

          if laplace==moyAuto:
              meilleureChoix="Autofinancement"
          elif laplace==moyAmor:
              meilleureChoix = "Ammorticement constant"
          else:
              meilleureChoix = "Annuité constante"
          st.write("Selon le critère LAPLACE, la meilleure stratégie est : "+meilleureChoix)

      #Critère de Savage
          maxMarche1=max(float(AutofinancementS),float(Amortissement_ConstantS ),float(Annuité_ConstanteS))
          maxMarche2 = max(float(AutofinancementD), float(Amortissement_ConstantD), float(Annuité_ConstanteD))
          maxMarche3 = max(float(AutofinancementF), float(Amortissement_ConstantF), float(Annuité_ConstanteF))
          ListAutoSavage = [maxMarche1-float(AutofinancementS),maxMarche2- float(AutofinancementD),maxMarche3- float(AutofinancementF)]
          ListAmorSavage = [maxMarche1-float(Amortissement_ConstantS),maxMarche2- float(Amortissement_ConstantD), maxMarche3-float(Amortissement_ConstantF)]
          ListAnnSavage = [maxMarche1-float(Annuité_ConstanteS),maxMarche2- float(Annuité_ConstanteD), maxMarche3-float(Annuité_ConstanteF)]
          regretAuto=max(ListAutoSavage)
          regretAmort=max(ListAmorSavage)
          regretAnn=max(ListAnnSavage)
          savage=min(regretAuto, regretAmort, regretAnn)

          if savage==regretAuto:
              meilleureChoix="Autofinancement"
          elif savage==regretAmort:
              meilleureChoix = "Ammorticement constant"
          else:
              meilleureChoix = "Annuité constante"
          st.write("Selon le critère SAVAGE, la meilleure stratégie est : "+meilleureChoix)