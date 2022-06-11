import streamlit as st
import pandas as pd

def app():
    with st.form(key="emprunt"):
        titre = st.text_input("Titre:")
        inv = st.text_input("Investissement:")
        ca = st.text_input("Chiffre d'affaire:")
        vac = st.text_input("Variation du chiffre d'affaire en %")
        ta = st.text_input("Taux d'amortissement en %")
        ra = st.text_input("Régime d'amortissement", value="Linéaire")
        vr = st.text_input("Valeur résiduelle")
        cf = st.text_input("Charges fixes")
        cv = st.text_input("Charges variables en %")
        bfr = st.text_input("Besoin en fond de roulement en %")
        rbfr = st.text_input("Recupération du besoin en fond de roulement en %")
        montantEmprunt = st.text_input("Montant d'emprunt:")
        tauxInteret = st.text_input("Taux d'interet en %:")

        submissionButton = st.form_submit_button(label="Valider")
        if submissionButton == True:
            nbannee=5

            an=(float(montantEmprunt) * (float(tauxInteret)/100)) / (1 - (pow(1+(float(tauxInteret)/100), -nbannee)))
            Cdp=[]
            Cdp.append(float(montantEmprunt))
            interet=[]
            interet.append(float(montantEmprunt)*(float(tauxInteret)/100))
            anList=[an for i in range(nbannee)]

            amortis=[]
            amortis.append(an-interet[0])
            for i in range(1,nbannee):
                Cdp.append(Cdp[i-1]-amortis[i-1])
                interet.append(Cdp[i]*(float(tauxInteret)/100))
                amortis.append(an-interet[i])

            Resultat=[Cdp,interet,anList,amortis]
            df = pd.DataFrame(Resultat, index=["Cdp","Interet","Annuité","Ammortissement"])
            st.dataframe(df)

            cvauto = (float(cv) / 100) * float(ca)
            amorti = (float(ta) / 100) * float(inv)
            rbrute = float(ca) - cvauto - float(cf) - amorti
            rnet = rbrute - (0.3 * rbrute)
            caf = rnet + amorti

            chargeInteret = [interet[i] * (float(tauxInteret) / 100) for i in range(nbannee)]

            st.write('cvauto : ' + str(cvauto))
            st.write('amorti : ' + str(amorti))
            st.write('rbrute : ' + str(rbrute))
            st.write('rnet : ' + str(rnet))
            st.write('caf : ' + str(caf))
            st.write("charges d'interet : " + str(chargeInteret[0]))

            montantEmpruntList = []
            montantEmpruntList.append(float(montantEmprunt))
            for i in range(1, nbannee + 1):
                montantEmpruntList.append(0)

            caList = []
            cafList = []
            bfrList = []
            cafList.append(0)
            cafList.append(caf)
            caList.append(float(ca))
            for i in range(1, nbannee):
                ca = float(ca) + float(ca) * (float(vac) / 100)
                caList.append(ca)
                cvauto = (float(cv) / 100) * float(ca)
                rbrute = float(ca) - cvauto - float(cf) - amorti - chargeInteret[i]
                rnet = rbrute - (0.3 * rbrute)
                caf = rnet + amorti
                cafList.append(caf)
            print(cafList)

            # Reccup bfr
            Sbfr = 0
            for i in range(nbannee):
                bfrList.append((float(bfr) / 100) * caList[i])
                Sbfr = bfrList[i] + Sbfr

            Rbfr = Sbfr * float(rbfr)
            print(Rbfr)
            RbfrList = []
            RbfrList = [0 for i in range(nbannee)]
            RbfrList.append(Rbfr)

            # Variation du besoin de fond de roulement

            Vbfr = []
            Vbfr.append(bfrList[0])
            for i in range(1, nbannee):
                Vbfr.append(bfrList[i] - bfrList[i - 1])
            Vbfr.append(0)
            print(Vbfr)

            # Valeur résiduelle

            ValResList = [0 for i in range(nbannee)]
            ValResList.append(float(vr))

            # Total 1
            Total1 = []
            Total1 = [float(cafList[i]) + float(RbfrList[i]) + float(ValResList[i]) + float(montantEmpruntList[i]) for i
                      in range(nbannee + 1)]

            # Investissement
            InvestList = []
            InvestList.append(float(inv))
            for i in range(1, nbannee + 1):
                InvestList.append(0)

            m = float(montantEmprunt) / nbannee
            MList = []
            MList.append(0)
            for i in range(1, nbannee + 1):
                MList.append(m)
            print("MLIST : " + str(MList))

            # Total2
            Total2 = [InvestList[i] - Vbfr[i] - m for i in range(nbannee + 1)]
            print("TOTAl2 : " + str(Total2))

            FNT = [Total2[i] - Total1[i] for i in range(nbannee + 1)]

            Resultat = [cafList, RbfrList, ValResList, montantEmpruntList, Total1, InvestList, Vbfr, MList, Total2, FNT]
            print(Resultat)
            df = pd.DataFrame(Resultat,
                              index=["cafList", "RbfrList", "ValResList", "Montant d'empr", "Total1", "InvestList",
                                     "Vbfr", "rembourssement d'emp", "Total2",
                                     "FNT"])
            st.dataframe(df)

            # van
            Van = 0
            for i in range(nbannee + 1):
                Van = Van + (FNT[i] / pow(0.1 + 1, float(nbannee)))
            Van = Van - FNT[0]
            st.write(('Van ' + str(Van)))

            # IP
            Ip = (1 + Van) / FNT[0]
            st.write(('Ip ' + str(Ip)))


















