import streamlit as st
import numpy as np


# Configuração inicial do streamlit - page
st.set_page_config(
  page_title= "Futbol Data | LD System",
  page_icon="⚽",
  layout="wide",
  initial_sidebar_state= "expanded"
)

 # Criando o botal para navegar até o perfil
st.sidebar.markdown("#### Developement by *Luiz Domingo*")
st.sidebar.image('img1.jpg',width=150)
btn = st.sidebar.link_button("Perfil","https://www.linkedin.com/in/luiz-domingo-silva-dev-dev/")

# Criando o titulo
st.markdown('# LD Data Analitics ⚽')

