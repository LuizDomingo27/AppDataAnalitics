import pandas as pd
import streamlit as st


#%%
@st.cache_data
def SearchGame():
  if "data" not in st.session_state:
    df_jogos = pd.read_csv('datasets/Dados.csv')
    st.session_state["data"] = df_jogos
    return df_jogos
