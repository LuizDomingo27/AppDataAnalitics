import streamlit as st
import numpy as np
from Model import JogosPorEquipes  


# Configuração inicial do streamlit - page
st.set_page_config(
  page_title= "Futbol Data | LD System",
  page_icon="⚽",
  layout="wide",
  initial_sidebar_state= "expanded"
)
# Criando o titulo
st.markdown('# LD Data Analitics ⚽')
tab = st.tabs(['Europa','Brasileirão'])

# Tab com jogos Europeu
with tab[0]:
  st.markdown('# Data Analitics Futbol Europeu')
  col1, col2 = st.columns(2, vertical_alignment= 'top', width= 520)
  df = JogosPorEquipes.SearchGame()
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

  # Criando o botal para navegar até o perfil
  st.sidebar.markdown("#### Developement by *Luiz Domingo*")
  btn = st.sidebar.link_button("Perfil","https://www.linkedin.com/in/luiz-domingo-silva-dev-dev/")


# Tab com Jogos do brasileirão
with tab[1]:
  dfb = JogosPorEquipes.SearcJogosBR()
  st.markdown('# Data Analitics Brasileirão')

  equipes_br = sorted(dfb['Home'].unique())
  equipebr = st.selectbox('Equipe', equipes_br, width=150)


