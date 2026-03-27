import pandas as pd


# ----------------------------------------------------------#

# -----------EXERCÍCIO 1-----------#

def extracao():

    vendas = pd.read_csv("vendas.csv")
    clientes = pd.read_csv("clientes.csv")
    produtos = pd.read_csv("produtos.csv")
    base_bruta = pd.read_csv("dados_vendas_etl_pandas_6000_linhas.csv")

    print("\n--- ARQUIVOS LIDOS ---\n")

    print("\nShape da base:\n", base_bruta.shape)
    print("\nShape de vendas:\n", vendas.shape)
    print("\nShape de produtos:\n", produtos.shape)
    print("\nShape de clientes:\n", clientes.shape)


    return vendas, clientes, produtos, base_bruta

def transformacao(base_bruta):
    print("\n === Etapa de Transformação ===")
    
    df = base_bruta.copy()

    print("\nShape da base:\n", df.shape)
    print("\nColunas: ")
    print(df.columns)
    print("\nValores nulos por coluna:\n")
    print(df.isna().sum())
    print("\nPrimeiras 5 linhas:\n")
    print(df.head(20))

    print("\n === Etapa de Padronização de colunas de texto ===")

    df["nome_cliente"] = df["nome_cliente"].str.strip().str.title() #nomes com inicial maiúscula
    df["estado"] = df["estado"].str.strip().str.upper() #estados com letra maiúscula
    df["cidade"] = df["cidade"].str.strip().str.title() #cidades padronizadas

    print("\Conversão de data_venda:\n")
    df["data_venda"] = pd.to_datetime(df["data_venda"], errors="coerce")

    print(df["data_venda"].head(20))

    print("Conversão de valor_unitario:\n")

    #a coluna tem que ser vista como texto, mas não lembro como faz
    #df["valor_unitario"] = df["valor_unitario"].to_string()
    df["valor_unitario"] = df["valor_unitario"].str.replace(",", ".", regex=False)
    df["valor_unitario"] = pd.to_numeric(df["valor_unitario"], errors="coerce")

    print(df["valor_unitario"].head(20))

    print("Conversão de desconto_pct:\n")

    df["desconto_pct"] = df["desconto_pct"]

    #verifica se o texto contém "%s"
    #na = False se houver nulo, ele não quebra. Considera como false
    percentual = df["desconto_pct"].str.contains("%", na = False) #identifica quais linhas precisam de transformação
    
    
    ''' Não dá pra converter 'x% em número de uma forma "direta" com to_numeric, etc.
    Vai ter que converter a coluna pra número "10" vira 10, "0.15" vira 0.15 e assim por diante...'''
    #df.loc seleciona linhas e colunas
    #percentual seleciona só as linhas onde havia "%"
    df.loc[percentual, "desconto_pct"] = (
        df.loc[percentual, "desconto_pct"].str.replace("%s", "", regex = False)#remove o símbolo "%"
    )
    #pega a coluna e converte para número
    df["desconto_pct"] = pd.to_numeric(df["desconto_pct"], errors="coerce")
    
    #pega os valores que tinham "%" e divide por 100
    df.loc[percentual, "desconto_pct"] = df.loc[percentual, "desconto_pct"] / 100

    print(df["desconto_pct"].head(20))


    #print(df.info())

    print("\nAmostra após padronização:\n")
    
    #print(df[["nome_cliente", "estado", "cidade"]].head(10))
    
    print(df[["data_venda", "valor_unitario"]].head(40))

    return df
 

def main():

    vendas, clientes, produtos, base_bruta = extracao()
    print("\nExtração realizada!\n")

    df = transformacao(base_bruta)
    

if __name__ == "__main__":
    main()
