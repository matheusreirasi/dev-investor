from fastapi import FastAPI
from scraping import get_acoes_fundamentus, get_fiis_fundamentus

app = FastAPI()

@app.get('/acoes')
def get_acoes():
    return get_acoes_fundamentus()

@app.get('/fiis')
def get_fiis():
    return get_fiis_fundamentus()