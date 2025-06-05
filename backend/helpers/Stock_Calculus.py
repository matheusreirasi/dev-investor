from scraping import get_acoes_fundamentus
import pandas as pd
from utils.string_to_float import string_to_float


class CalculadoraAcoes():
    def __init__(self):
        self.dados = pd.DataFrame(get_acoes_fundamentus())
        self.dados = string_to_float(self.dados, ["Div.Yield", "Mrg Ebit", "Mrg. Líq.", "ROIC", "ROE", "Cresc. Rec.5a"])
        self.dados = self.dados.where(pd.notnull(self.dados), '')
        self.requisito_minimo = self.dados[self.dados["Liq.2meses"] > 1000000]
    
    def acoes(self):
        return self.dados.to_dict(orient='records')

    def dy(self):
        # df_filtrado = pd.DataFrame()
        df_filtrado = self.requisito_minimo[self.requisito_minimo['Div.Yield'] > 0].sort_values(by='Div.Yield', ascending=False).head(100)
        return df_filtrado[['Papel','Cotação','Div.Yield']].to_dict(orient='records')
    
    def p_vp(self):
        # df_filtrado = pd.DataFrame()
        df_filtrado = self.requisito_minimo[self.requisito_minimo['P/VP'] > 0].sort_values(by='P/VP', ascending=True).head(100)
        df_p_vp = df_filtrado[['Papel','Cotação','P/VP']]
        print(self.requisito_minimo.dtypes)
        return df_p_vp.to_dict(orient='records')


    def roe(self):
        # df_filtrado = pd.DataFrame()
        self.requisito_minimo['ROE'] = pd.to_numeric(self.requisito_minimo['ROE'], errors='coerce')
        df_filtrado = self.requisito_minimo[self.requisito_minimo['ROE'] > 6].sort_values(by='ROE', ascending=False).head(100)
        df_roe = df_filtrado[['Papel','Cotação','ROE']]
        return df_roe.to_dict(orient='records')
    
    
    def acoes_selecionadas(self):
        df_dy = pd.DataFrame(self.dy())
        df_p_vp = pd.DataFrame(self.p_vp())
        df_roe = pd.DataFrame(self.roe())

        colunas_comuns = set(df_dy.columns) & set(df_p_vp) & set(df_roe)
        df_acoes_comuns = df_dy.merge(df_p_vp, on='Papel').merge(df_roe, on='Papel').drop(columns=['Cotação_x','Cotação_y'])

        return df_acoes_comuns.to_dict(orient='records')
