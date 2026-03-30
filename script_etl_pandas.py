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

    print("\nTratamento de nulos:\n")


    '''fillna preenche valores nulos.
    Foi feita a escolha pela mediana.
    status_pedido foi preenchido como desconhecido para não ficar vazio.
    O nome do cliente foi removido já que é uma informação de identificação'''

    df["quantidade"] = df["quantidade"].fillna(df["quantidade"].median())
    df["valor_unitario"] = df["valor_unitario"].fillna(df["valor_unitario"].median())
    df["status_pedido"] = df["status_pedido"].fillna("desconhecido")
    df = df.dropna(subset=["nome_cliente"]) #remove linhas em que 'nome_cliente' é nulo

    #aqui só pra testar se diminuem os nulos

    df["desconto_pct"] = df["desconto_pct"].fillna(0)


    print("\nValores nulos depois do tratamento: ")
    print(df.isna().sum())
    print("\nShape após tratamento: ")
    print(df.shape)

    print("\nCriação de colunas derivadas:\n")

    df["valor_total_bruto"] = df["quantidade"] * df["valor_unitario"] #multiplica quantidade pelo valor unitário
    df["valor_desconto"] = df["valor_total_bruto"] * df["desconto_pct"] #calcula o desconto
    df["valor_final"] = df["valor_total_bruto"] - df["valor_desconto"] #subtrai o desconto do valor bruto

    print(df[["valor_total_bruto", "valor_desconto", "valor_final"]].head(10))

    


    print("\nAmostra após padronização:\n")
    
    #print(df[["nome_cliente", "estado", "cidade"]].head(10))
    
    print(df[["data_venda", "valor_unitario"]].head(40))

    #return df

    print("Criação da faixa_valor com apply:\n")

    #apply aplica uma função a cada valor d euma coluna
    #para cada valor de uma coluna x, a função decide qual o valor terá

    def categoria_valor(v):
        if v < 500:
            return "baixo"
        elif v < 2000:
            return "médio"
        else:
            return "alto"
    df["faixa_valor"] = df["valor_final"].apply(categoria_valor)

    print(df["faixa_valor"])


    print("Gera resumo por categoria:\n")
    #groupby agrupa as linhas por categoria
    #agg faz várias agregações ao mesmo tempo

    resumo_categoria = (df.groupby("categoria").agg(
        faturamento_total = ("valor_final", "sum"), #na coluna valor_final, soma tudo
        quantidade_total_vendida = ("quantidade", "sum"), #na coluna quantidade, soma tudo
        ticket_medio_pedido = ("valor_final", "mean") #na coluna valor final, faz a média
    ).reset_index()) #transforma o índice em uma coluna de novo(sem ele, não aparece o índice)

    print(resumo_categoria)
    
    return df, resumo_categoria

def transformacao_merge(vendas, clientes, produtos):
    print("\n --- Fase de integração com merge --- \n")

    #fazendo cópias para não alterar os dfs originais e fazer besteira
    vendas_df = vendas.copy()
    clientes_df = clientes.copy()
    produtos_df = produtos.copy()

    print("\nShape das bases:\n")
    print("vendas:", vendas_df.shape)
    print("clientes:", clientes_df.shape)
    print("produtos:", produtos_df.shape)

    #primeiro merge: vendas com clientes
    base_enriquecida = vendas_df.merge(clientes_df, on = "id_cliente", how = "left")
    #juntou dois df's pela chave 'id_cliente' e mantém todas as linhas do df da esquerda, que aqui é o vendas_df

    print("\nShape após merge entre vendas e cleintes:\n")
    print(base_enriquecida.shape)
    print(base_enriquecida.head())

    #segundo merge: resultado com produtos
    base_enriquecida = base_enriquecida.merge(produtos_df, on="id_produto", how = "left")

    print("\nShape após merge entre resultados e produtos:\n")
    print(base_enriquecida.shape)
    print(base_enriquecida.head())

    print("\nColunas após o merge:\n")
    #pra mostrar o nome das colunas após o merge
    #útil pra saber se os nomes são como esperado
    print(base_enriquecida.columns)

    #cria uma lista de colunas que serão mantidas
    colunas_merge = [
        "id_venda",
        "data_venda",
        "estado",
        "produto",
        "categoria",
        "quantidade",
        "valor_final"
    ]

    #seleciona apenas essas colunas passadas no argumento
    base_enriquecida = base_enriquecida[colunas_merge]

    print("\nBase enriquecida:\n")
    print(base_enriquecida.head(10)) 

    return base_enriquecida
 

def main():

    vendas, clientes, produtos, base_bruta = extracao()
    df_tratado, resumo_categoria= transformacao(base_bruta)
    base_enriquecida = transformacao_merge(vendas, clientes, produtos)
    print("\nExtração realizada!\n")

    #df = transformacao(base_bruta)
    
    

if __name__ == "__main__":
    main()
