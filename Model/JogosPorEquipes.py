#%%
import pandas as pd
import streamlit as st


@st.cache_data(ttl=1000)
def SearchGame():
  #if "data" not in st.session_state:
    dfE = pd.read_csv('datasets/Dados.csv')
   # st.session_state.data = df
    #df_jogos = st.session_state.data 
    return dfE
  

@st.cache_data(ttl=1000)
def SearcJogosBR():
  #if "data" not in st.session_state:
    dfB = pd.read_csv('datasets/BR.csv')
    dfB['Data'] = pd.to_datetime(dfB['Data'], errors='coerce')
    #st.session_state.data = df
    #dfbr = st.session_state.data
    return dfB


dadosBR = SearcJogosBR()
dadosEuropa = SearchGame() 
