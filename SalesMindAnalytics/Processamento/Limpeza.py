#import bibliotecas
from LeituraDeDados import bibliotecas


def limpar_dados(df):
    df.dropna(inplace=True)
    vendas["data"] = pd.to_datetime(vendas["data"], format="%Y-%m-%d")