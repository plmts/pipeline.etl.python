import pandas as pd

#extração
def extrair_dados():
    """função para extrair os dados do bd"""
    df = pd.read_csv('./dados.csv')
    dados_filtrados = df['OwnerName']
    return dados_filtrados

#transformação
def carregar_dados(dados_filtrados):
    """Função para transformar os dados filtrados em um novo arquivo"""
    arquivo_filtrado = dados_filtrados.to_csv("dados_filtrados.csv", index=False)
    return arquivo_filtrado

