import streamlit as st
import pandas as pd
import numpy as np
import webbrowser as wb

# Configuração inicial do streamlit - page
st.set_page_config(
  page_title= "Futbol Data | LD System",
  page_icon="⚽",
  layout="wide",
  initial_sidebar_state= "expanded"
)

# Criando o titulo
st.markdown('# Data Analitics of **FIFA**')
st.sidebar.markdown("#### Developement by *Luiz Domingo*")

# Criando o botal para navegar até o perfil
btn = st.sidebar.link_button("Perfil","https://www.linkedin.com/in/luiz-domingo-silva-dev-dev/")
