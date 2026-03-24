import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# 1. Conexão segura com o banco de dados usando o .env
load_dotenv()
db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)

# Função para carregar dados de uma view
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# Título do dashboard
st.title('Dashboard de Temperaturas IoT 🌡️')

# Gráfico 1: Média de temperatura por dispositivo
st.header('Média de Temperatura por Dispositivo')
df_avg_temp = load_data('avg_temp_por_dispositivo')
fig1 = px.bar(df_avg_temp, x='device_id', y='avg_temp', color='device_id')
st.plotly_chart(fig1)

# Gráfico 2: Contagem de leituras por hora
st.header('Leituras por Hora do Dia')
df_leituras_hora = load_data('leituras_por_hora')
# Ordenando as horas para o gráfico de linha fazer sentido
df_leituras_hora = df_leituras_hora.sort_values(by='hora')
fig2 = px.line(df_leituras_hora, x='hora', y='contagem', markers=True)
st.plotly_chart(fig2)

# Gráfico 3: Temperaturas máximas e mínimas por dia
st.header('Temperaturas Máximas e Mínimas por Dia')
df_temp_max_min = load_data('temp_max_min_por_dia')
# Ordenando pela data
df_temp_max_min = df_temp_max_min.sort_values(by='data')
fig3 = px.line(df_temp_max_min, x='data', y=['temp_max', 'temp_min'], markers=True)
st.plotly_chart(fig3)