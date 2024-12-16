import streamlit as st
import pandas as pd
import requests
import plotly.express as px

# Título do app
st.title('INVENTÁRIO ACABAMENTO DE PLACAS :shopping_trolley:')

# Caminho do arquivo XLSX
caminho_arquivo = 'Relatorio placas negativas.xlsx'

# Tenta carregar o arquivo
try:
    # Carregar os dados
    df = pd.read_excel(caminho_arquivo)

    # Exibe os dados carregados
    st.subheader("Dados Carregados:")
    st.dataframe(df)

    # Calcular a soma de cada coluna
    soma_colunas = df.sum(axis=0)  # Soma dos valores por coluna

    # Exibe a soma de cada coluna
    st.subheader("Soma dos Valores por Coluna:")
    st.write(soma_colunas)
    
except FileNotFoundError:
    st.error("Erro: O arquivo não foi encontrado. Verifique o caminho do arquivo.")
except Exception as e:
    st.error(f"Erro ao ler o arquivo: {e}")
