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
st.markdown('# Data Analitics Futbol Europeu')

# Carregando os dados
df = JogosPorEquipes.SearchGame()

# Criando a variável para armazenar as ligas
ligas = df['Season'].unique()
liga = st.sidebar.selectbox('Ligas', ligas)

# Criando a variavél para filtrar as equipes de acordo com aliga selecionada
df_equipes = df[df['Season'] == liga]
equipes = df_equipes['Home'].unique()
equipe = st.sidebar.selectbox('Equipes', equipes)

# Criando o DataFrame de acordo com a equipe selecionada
df_jogos = df_equipes[(df_equipes['Home'] == equipe)|(df_equipes['Away'] == equipe)].set_index("Home")
st.markdown(f"## {equipe}")
st.divider()
st.write(f"Total de Jogos {df_jogos['Away'].count()}")
st.dataframe(df_jogos.iloc[:, 2:-1], width="stretch") 

# Criando o botal para navegar até o perfil
st.sidebar.markdown("#### Developement by *Luiz Domingo*")
btn = st.sidebar.link_button("Perfil","https://www.linkedin.com/in/luiz-domingo-silva-dev-dev/")

