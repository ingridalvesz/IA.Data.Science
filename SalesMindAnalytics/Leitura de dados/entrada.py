#import bibliotecas
from bibliotecas import *

#carregando os dados clientes e vendas
def ler_clientes():
    return pd.read_csv("SalesMindAnalytics/Leitura de dados/dadosclientes.csv")

def ler_vendas():
    return pd.read_csv("SalesMindAnalytics/Leitura de dados/dadosvendas.csv")


