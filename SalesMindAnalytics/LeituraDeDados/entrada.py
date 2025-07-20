#import bibliotecas
from bibliotecas import *

#carregando os dados clientes e vendas
def clientes():
    return pd.read_csv("SalesMindAnalytics/Dados/dadosclientes.csv")

def vendas():
    return pd.read_csv("SalesMindAnalytics/Dados/dadosvendas.csv")
