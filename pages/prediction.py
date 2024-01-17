import streamlit as st
from model import *
from fire_state import create_store, get_state, set_state

slot = "Prediction"

key1 = create_store(slot, [
    ("Genre", "Male"),
    ("Age", 0),
    ("Income", 0),
    ("Spending", 0),
    ("Answer", '')
])

genre = st.radio("Genre", ["Male", "Female"], horizontal= False)

age = st.number_input("Age", min_value=0, step=1, value=get_state(slot, "Age"))
set_state(slot, ("Age", age))

annual_income = st.text_input("Annual Income (k$):", value=get_state(slot, "Income"))
set_state(slot, ("Income", annual_income))

spending_score = st.text_input("sepnding score (1-100)", value=get_state(slot, "Spending"))
set_state(slot, ("Spending", spending_score))

def predict_class():
    ans = kmeans.predict([[annual_income, spending_score]])
    formated_ans = ans[0]
    set_state(slot,("Answer", f"<h2 style='text-align:center;'>Ce client fait partie de la classe {formated_ans}</h2>"))

pred_button = st.button("Prédire type de client ", on_click=predict_class)

st.markdown(f"{get_state(slot, 'Answer')}", unsafe_allow_html=True)
