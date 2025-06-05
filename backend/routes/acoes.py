from fastapi import APIRouter
from fastapi.responses import JSONResponse
from helpers.Stock_Calculus import CalculadoraAcoes

router = APIRouter(prefix='/acoes')

@router.get('')
def get_acoes():
    calc = CalculadoraAcoes()
    return calc.acoes()

@router.get('/dy')
def get_acoes_dy():
    calc = CalculadoraAcoes()
    return JSONResponse(calc.dy())

@router.get('/pvp')
def get_acoes_pvp():
    calc = CalculadoraAcoes()
    return JSONResponse(calc.p_vp())

@router.get('/roe')
def get_acoes_roe():
    calc = CalculadoraAcoes()
    return JSONResponse(calc.roe())

@router.get('/selecionados')
def get_acoes_selecionados():
    calc = CalculadoraAcoes()
    return JSONResponse(calc.acoes_selecionadas())
