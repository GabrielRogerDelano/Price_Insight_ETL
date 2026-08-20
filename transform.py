import pandas as pd
from extract import extract

def transform(endpoint: str, lista_colunas_requeridas: str):
    data = extract(endpoint)

    df = pd.json_normalize(data)
    df.dropna(inplace=True)

    df_requerido = df[lista_colunas_requeridas]

    return df_requerido