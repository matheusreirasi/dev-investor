import pandas as pd

def string_to_float(df: pd.DataFrame, colunas: list) -> pd.DataFrame:
    for coluna in colunas:
        df[coluna] = (
            df[coluna]
            .astype(str)
            .str.replace('%', '', regex=False)
            .str.replace(',', '.', regex=False)
        )
        df[coluna] = pd.to_numeric(df[coluna], errors='coerce')
    return df
"""
def string_to_float(df, lista_de_colunas):
  for coluna in lista_de_colunas:
    if (df[coluna].dtype == object):
      df[coluna] = df[coluna].str.replace(".", "")
      df[coluna] = df[coluna].str.replace(",", ".")
      df[coluna] = df[coluna].str.rstrip("%").astype("float")/100
"""