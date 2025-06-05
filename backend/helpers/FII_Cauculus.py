from scraping import get_fiis_fundamentus
import pandas as pd
from utils.string_to_float import string_to_float


class CalculadoraFiis():
    def __init__(self):
        self.dados = pd.DataFrame(get_fiis_fundamentus())
        self.dados = string_to_float(self.dados, ["FFO Yield", "Dividend Yield", "Cap Rate", "Vacância Média"])
        self.dados = self.dados.where(pd.notnull(self.dados), '')
        self.requisito_minimo = self.dados[self.dados["Valor de Mercado"] > 500000000]
    
    def fiis(self):
        return self.dados.to_dict(orient='records')

    def dy(self):
        # df_filtrado = pd.DataFrame()
        df_filtrado = self.requisito_minimo[self.requisito_minimo['Dividend Yield'] > 0].sort_values(by='Dividend Yield', ascending=False).head(100)
        return df_filtrado[['Papel','Segmento','Cotação','Dividend Yield']].to_dict(orient='records')
    
    def p_vp(self):
        # df_filtrado = pd.DataFrame()
        df_filtrado = self.requisito_minimo[self.requisito_minimo['P/VP'] > 0].sort_values(by='P/VP', ascending=True).head(100)
        df_p_vp = df_filtrado[['Papel','Segmento','Cotação','P/VP']]
        return df_p_vp.to_dict(orient='records')

    def qtd_imoveis(self):
        # df_filtrado = pd.DataFrame()
        df_filtrado = self.requisito_minimo[self.requisito_minimo['Qtd de imóveis'] > 0].sort_values(by='Qtd de imóveis', ascending=False).head(100)
        df_qtd_imoveis = df_filtrado[['Papel','Segmento','Cotação','Qtd de imóveis']]
        return df_qtd_imoveis.to_dict(orient='records')

    def vacancia(self):
        df_filtrado = self.requisito_minimo[self.requisito_minimo['Vacância Média'] > 0].sort_values(by='Vacância Média', ascending=False).head(100)
        df_qtd_imoveis = df_filtrado[['Papel','Segmento','Cotação','Vacância Média']]
        return df_qtd_imoveis.to_dict(orient='records')

    
    def fiis_selecionados(self):
        df_dy = pd.DataFrame(self.dy())
        df_p_vp = pd.DataFrame(self.p_vp())
        df_qtd_imoveis = pd.DataFrame(self.qtd_imoveis())
        df_acoes_comuns = df_dy.merge(df_p_vp, on='Papel').merge(df_qtd_imoveis, on='Papel').drop(columns=['Segmento_x','Segmento_y','Cotação_x','Cotação_y'])

        ordem_colunas = ['Papel', 'Segmento', 'Cotação', 'Dividend Yield', 'P/VP', 'Qtd de imóveis']
        df_acoes_comuns = df_acoes_comuns[ordem_colunas]

        return df_acoes_comuns.to_dict(orient='records')