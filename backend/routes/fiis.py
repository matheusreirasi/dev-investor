from fastapi import APIRouter
from fastapi.responses import JSONResponse
from helpers.FII_Cauculus import CalculadoraFiis

router = APIRouter(prefix='/fiis')

@router.get('')
def get_fiis():
    calc = CalculadoraFiis()
    return calc.fiis()

@router.get('/dy')
def get_fiis_dy():
    calc = CalculadoraFiis()
    return JSONResponse(content=calc.dy())

@router.get('/pvp')
def get_fiis_pvp():
    calc = CalculadoraFiis()
    return JSONResponse(content=calc.p_vp())

@router.get('/imoveis')
def get_fiis_imoveis():
    calc = CalculadoraFiis()
    return JSONResponse(content=calc.qtd_imoveis())

@router.get('/vacancia')
def get_fiis_vacancia():
    calc = CalculadoraFiis()
    return JSONResponse(content=calc.vacancia())

@router.get('/selecionados')
def get_fiis_selecionados():
    calc = CalculadoraFiis()
    return JSONResponse(content=calc.fiis_selecionados())

