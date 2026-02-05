import pandas as pd
import streamlit as st


#%%
@st.cache_data(ttl=1800)
def SearchGame():
  if "data" not in st.session_state:
    df = pd.read_csv('datasets/Dados.csv')
    st.session_state.data = df
    df_jogos = st.session_state.data 
    return df_jogos
