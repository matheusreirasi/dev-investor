from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from route import router
from routes import acoes, fiis

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(acoes.router, prefix='/api')
app.include_router(fiis.router, prefix='/api')