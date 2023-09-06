import pandas as pd
from sqlalchemy import create_engine

#extração
df = pd.read_csv('./dados.csv')

#transformação
def carregar_dados(dados_filtrados):
    """Função para transformar os dados filtrados em um novo arquivo"""
    arquivo_filtrado = df['OwnerName']
    return arquivo_filtrado

#Carregamento
novos_dados = carregar_dados(df)
novos_dados.to_csv("dados_filtrados.csv", index=False)
