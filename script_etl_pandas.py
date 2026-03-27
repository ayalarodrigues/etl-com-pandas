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
    df = base_bruta

    print("\nShape da base:\n", df.shape)
    print("\nColunas: ")
    print(df.columns)
    print("\nValores nulos por coluna:\n")
    print(df.isna().sum())
    print("\nPrimeiras 5 linhas:\n")
    print(df.head())


def main():

    vendas, clientes, produtos, base_bruta = extracao()
    print("\nExtração realizada!\n")

    df = transformacao(base_bruta)
    

if __name__ == "__main__":
    main()
