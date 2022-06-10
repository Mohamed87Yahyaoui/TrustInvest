import streamlit as st
import pandas as pd

R1 = [-800,-200,-100]
R2 = [700,500,500]
R3 = [1500,1300,1100]

R4=[R1,R2,R3]
df=pd.DataFrame(R4,index=["S1","S2","S3"],columns=["R1","R2","R3"])

#critére MAXIMIN
