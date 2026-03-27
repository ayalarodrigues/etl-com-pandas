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
    print(df.head())

    print("\n === Etapa de Padronização de colunas de texto ===")

    df["nome_cliente"] = df["nome_cliente"].str.strip().str.title() #nomes com inicial maiúscula
    df["estado"] = df["estado"].str.strip().str.upper() #estados com letra maiúscula
    df["cidade"] = df["cidade"].str.strip().str.title() #cidades padronizadas

    print("\nAmostra após padronização:\n")
    print(df[["nome_cliente", "estado", "cidade"]].head(10))

    return df
 

def main():

    vendas, clientes, produtos, base_bruta = extracao()
    print("\nExtração realizada!\n")

    df = transformacao(base_bruta)
    

if __name__ == "__main__":
    main()
