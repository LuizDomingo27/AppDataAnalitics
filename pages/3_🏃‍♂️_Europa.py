import streamlit as st
import numpy as np
from Model import JogosPorEquipes  

st.sidebar.markdown("#### Developement by *Luiz Domingo*")
st.sidebar.image('img2.jpg',width=150)
btn = st.sidebar.link_button("Perfil","https://www.linkedin.com/in/luiz-domingo-silva-dev-dev/")
tab = st.tabs(['Europa'])

# Tab com jogos Europeu
with tab[0]:
  st.markdown('# Data Analitics Futbol Europeu')
  col1, col2 = st.columns(2, vertical_alignment='top', width= 520)
  df = JogosPorEquipes.dadosEuropa
  ligas = sorted(df['Season'].unique())
 
  with col1:
    liga = st.selectbox('Ligas', ligas)

  df_equipes = df[df['Season'] == liga]
  equipes = sorted(df_equipes['Home'].unique())
  
  with col2:
    equipe = st.selectbox('Equipes', equipes)

  # Criando o DataFrame de acordo com a equipe selecionada
  df_jogos = df_equipes[(df_equipes['Home'] == equipe)|(df_equipes['Away'] == equipe)].set_index("Home")
  st.divider()
  st.write(f"Total de Jogos {df_jogos['Away'].count()}")
  st.dataframe(df_jogos.iloc[:, 2:-1], width="stretch") 

  # Jogos com mais de um Gol
  jogosMais = df_equipes[(df_equipes['Home'] == equipe) & ((df_equipes['GH'] + df_equipes['GA']) > 2)]
  st.dataframe(jogosMais.iloc[:, 2:-1].set_index('Home'))

 

