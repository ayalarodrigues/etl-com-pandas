````md
# ETL com Pandas

Projeto desenvolvido em **Python** com **Pandas** para prática de **ETL (Extração, Transformação e Exportação de Dados)** a partir de múltiplas bases em CSV.

## Objetivo

Este projeto tem como objetivo demonstrar, de forma prática, a construção de um pipeline de ETL com operações comuns em análise e tratamento de dados, incluindo:

- leitura de arquivos CSV;
- limpeza e padronização de dados;
- tratamento de valores ausentes;
- conversão de tipos;
- criação de colunas derivadas;
- agrupamentos com `groupby`;
- integração de bases com `merge`;
- geração de tabela dinâmica com `pivot_table`;
- exportação de resultados em CSV e JSON.

## Tecnologias utilizadas

- Python 3
- Pandas

## Estrutura do projeto

```text
etl-com-pandas/
├── data/
│   ├── clientes.csv
│   ├── produtos.csv
│   ├── vendas.csv
│   └── dados_vendas_etl_pandas_6000_linhas.csv
├── docs/
│   └── exercicios_transformacao_exportacao_pandas.docx
├── output/
├── script_etl_pandas.py
├── requirements.txt
├── README.md
└── .gitignore
````

## Bases utilizadas

O projeto trabalha com as seguintes bases de dados:

* `vendas.csv`
* `clientes.csv`
* `produtos.csv`
* `dados_vendas_etl_pandas_6000_linhas.csv`

Esses arquivos ficam armazenados na pasta `data/`.

## Etapas do pipeline

### 1. Extração

Na etapa de extração, o script realiza a leitura dos arquivos CSV utilizando `pandas.read_csv()`.

Exemplo:

```python
df_vendas = pd.read_csv("data/vendas.csv")
```

### 2. Transformação

Na etapa de transformação, são realizadas operações como:

* padronização de textos;
* remoção de espaços extras;
* conversão da coluna de data para formato adequado;
* conversão de colunas numéricas;
* tratamento de valores nulos;
* preenchimento de descontos ausentes;
* remoção de registros problemáticos;
* criação de novas colunas calculadas.

Entre as colunas derivadas, destacam-se:

* `valor_total_bruto`
* `valor_desconto`
* `valor_final`
* `faixa_valor`

### 3. Agrupamento e análise

Após a limpeza e transformação dos dados, o projeto gera resumos analíticos com:

* total faturado por categoria;
* quantidade vendida por categoria;
* ticket médio;
* consolidação por estado e categoria.

Essa etapa utiliza operações como:

* `groupby`
* `agg`
* `pivot_table`

### 4. Integração de bases

O projeto também realiza integração entre diferentes conjuntos de dados por meio de `merge`, enriquecendo a base principal com informações complementares de clientes e produtos.

Exemplo de integração:

* base de vendas
* base de clientes
* base de produtos

### 5. Exportação

Ao final do processo, o script gera arquivos de saída na pasta `output/`.

Arquivos gerados:

* `base_tratada.csv`
* `resumo_categoria.csv`
* `resumo_categoria.json`
* `base_enriquecida.csv`
* `resumo_estado_categoria.csv`
* `resumo_estado_categoria.json`

## Competências demonstradas

Este projeto evidencia conhecimentos e práticas em:

* manipulação de dados com Pandas;
* limpeza e padronização de bases;
* transformação de dados tabulares;
* integração entre múltiplas fontes;
* análise exploratória inicial;
* geração de saídas estruturadas;
* organização de projeto em Python.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/ayalarodrigues/etl-com-pandas.git
cd etl-com-pandas
```

### 2. Criar ambiente virtual

No Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o script

```bash
python script_etl_pandas.py
```

## Organização dos arquivos

* A pasta `data/` contém os arquivos de entrada.
* A pasta `output/` armazena os arquivos gerados pelo processo ETL.
* A pasta `docs/` pode ser utilizada para armazenar enunciados, relatórios ou materiais de apoio.

Essa separação melhora a organização do repositório e deixa o projeto mais adequado para apresentação em portfólio.

## Melhorias futuras

Algumas melhorias que podem ser implementadas futuramente:

* modularização do código em múltiplos arquivos;
* criação de funções mais reutilizáveis;
* tratamento de exceções para leitura e escrita;
* criação de testes automatizados;
* documentação técnica mais detalhada;
* uso de notebooks para análise exploratória complementar.

## Autora

**Ayala Rodrigues Freire**

Projeto acadêmico desenvolvido para prática de ETL com Pandas, com foco em organização, transformação, integração e exportação de dados.

```
```
