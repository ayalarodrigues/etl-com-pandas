import pandas as pd


# ----------------------------------------------------------#

# -----------EXERCÍCIO 1-----------#

def extracao():

    vendas = pd.read_csv("vendas.csv")
    clientes = pd.read_csv("clientes.csv")
    produtos = pd.read_csv("produtos.csv")
    base_bruta = pd.read_csv("dados_vendas_etl_pandas_6000_linhas.csv")

    print("--- ARQUIVOS LIDOS ---")

    return vendas, clientes, produtos, base_bruta

def main():

    vendas, cliete, produtos, base_bruta = extracao()
    print("\nExtração realizada!\n")
    

if __name__ == "__main__":
    main()
