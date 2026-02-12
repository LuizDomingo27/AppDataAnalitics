import pandas as pd
import streamlit as st
from Model import JogosPorEquipes as JE

st.sidebar.markdown("#### Developement by *Luiz Domingo*")
st.sidebar.image('img3.jpg',width=150)
btn = st.sidebar.link_button("Perfil","https://www.linkedin.com/in/luiz-domingo-silva-dev-dev/")
tab = st.tabs(['Jogos'])

with tab[0]:
  st.markdown('# Data Analitics Brasileirão')
  col3, col4, col5 = st.columns(3, vertical_alignment='top', width=350)
  jogosBR = JE.dadosBR
  
  jogosAno = jogosBR.query("Season == 2026 and TotalGols > 2")
  st.dataframe(jogosAno.iloc[:,1:8])

  st.markdown("## Jogos com mais de 1 Gol" )
  filtro_Jogos_Mais1_Gol = jogosBR[(jogosBR['Season']==2025) & (jogosBR['TotalGols']>1)] 
  st.dataframe(filtro_Jogos_Mais1_Gol)
