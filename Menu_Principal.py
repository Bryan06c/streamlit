import streamlit as st
import pandas as pd


st.title("👋 Hello, ce-ci est un projet Streamlit créer par Bryan!")


st.header("Bienvenue dans ma première application Streamlit")
st.markdown("""
Vous pouvez naviguer sur le menu à gauche pour explorer différentes fonctionnalités :

- **Calculateur de Fonction affine** : Calculer une fonction affine.
- **Data Analyst** : Charger et visualiser de manière interactive des données.
""")

st.subheader("📊 Calculateur de Fonction affine")
st.write("Cet outil vous permet de calculer une fonction affine et de visualiser son graphique.")

st.subheader("📂 Data Analyst")
st.write("Cet outil vous permet de charger un fichier CSV et de visualiser les données de manière interactive.")


