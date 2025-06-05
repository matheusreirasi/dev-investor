import requests
import pandas as pd

def get_acoes_fundamentus():
    metadata = {"User-Agent":"Mozilla/5.0"}
    url = 'https://www.fundamentus.com.br/resultado.php'

    page = requests.get(url, headers= metadata)
    df = pd.DataFrame(pd.read_html(page.content, decimal=',', thousands='.')[0])
    df = df.where(pd.notnull(df), None)

    return df.to_dict(orient="records")


def get_fiis_fundamentus():
    metadata = {"User-Agent":"Mozilla/5.0"}
    url = 'https://www.fundamentus.com.br/fii_resultado.php'

    page = requests.get(url, headers= metadata)
    df = pd.DataFrame(pd.read_html(page.content, decimal=',', thousands='.')[0])
    df = df.where(pd.notnull(df), None)

    return df.to_dict(orient="records")

class FundamentusScraper:
    def __init__(self):
        self.header = {"User-Agent":"Mozilla/5.0"}

    