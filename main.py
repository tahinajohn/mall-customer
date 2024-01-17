import streamlit as st
from model import *

st.divider()

# Titre de l'application
st.sidebar.markdown("Home🚀")
st.title("MALL CUSTOMER👔🛒")
st.divider()
st.markdown(f"<h5>Avec le modèle de classification, cette application va classer les différents types de client🤵 dans un centre commercial🏬</h5>", unsafe_allow_html=True)

st.markdown("<h3 style='color : yellow'>Dataset utilisé 📶:</h3>", unsafe_allow_html=True)
st.write(dataset)

st.markdown("<h3 style='color : yellow'>Usages:</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='color : cyan'>Stratégies de marketing ciblé:</h3>", unsafe_allow_html=True)
st.markdown(f"<h5>En comprenant les différents profils de clients, les centres commerciaux peuvent ajuster leurs stratégies marketing. Par exemple, les clients ayant des revenus élevés mais dépensant peu pourraient être ciblés par des promotions spéciales pour les inciter à dépenser davantage.</h5>", unsafe_allow_html=True)

st.write("")

st.markdown("<h3 style='color : cyan'>Optimisation des promotions et des remises :</h3>", unsafe_allow_html=True)
st.markdown(f"<h5>Les informations sur les revenus et les habitudes de dépenses peuvent aider à concevoir des promotions et des remises adaptées à chaque segment de clientèle. Par exemple, des remises spéciales pour les clients à revenus élevés mais qui dépensent peu pourraient les inciter à augmenter leurs achats.</h5>", unsafe_allow_html=True)
