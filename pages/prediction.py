import streamlit as st
from model import *

genre = st.radio("Genre", ["Male", "Female"], horizontal= False)

age = st.number_input("Age", min_value=0, step=1)

annual_income = st.text_input("Annual Income (k$):")

spending_score = st.text_input("sepnding score (1-100)")

if st.button("predire type de client"):
    ans = kmeans.predict([[annual_income, spending_score]])
    st.write("Ce client fait partie du groupe : ", ans[0])