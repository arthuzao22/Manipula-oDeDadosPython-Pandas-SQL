import pandas as pd
from displayfunction import display
from tabulate import tabulate
import pyodbc

# Define a string de conexão
conn_str = (
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-0T24SC8;"
    "DATABASE=BANCO_TESTE;"
    "Trusted_Connection=yes;"
)
# Estabelece a conexão
conn = pyodbc.connect(conn_str)
# Cria um cursor para executar consultas
cursor = conn.cursor()
#TIRA O LIMITADOR DE LINHAS E COLUNAS
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#--------------------------------------------------------------------------------

# Exemplo de consulta
queryTemp = """
                IF OBJECT_ID('tempdb..#CASADOsc') IS NOT NULL
                    DROP TABLE #CASADOsc;

                SELECT ID, NOME, IDADE, ALTURA_CM, ESTADO_CIVIL
                INTO #CASADOsc
                FROM PESSOA
"""
cursor.execute(queryTemp)

# Consulta para ler os dados da tabela temporária
ListarUs = "SELECT * FROM #CASADOsc"
df = pd.read_sql(ListarUs, conn)

# Multiplicação da IDADE x ALTURA_CM
df['IDADE_X_ALTURA'] = df['IDADE'] * df['ALTURA_CM']

# Verifica se a pessoa está casada ou não
df['SITUACAO'] = df['ESTADO_CIVIL']

def atualizar_situacao(valor):
    if valor == "Divorciado":
        return 'xxxx'
    else:
        return valor

df['SITUACAO'] = df['SITUACAO'].apply(atualizar_situacao)
#df.to_excel('dados.xlsx', index=False)

#-------------------------------------------------------

def Criar_update(row):
    if row['SITUACAO'] == 'xxxx':
        return f"UPDATE Pessoa SET ESTADO_CIVIL = '{row['ESTADO_CIVIL']}' WHERE ID = {row['ID']}"
    else:
        return ""

df['UPDTE'] = df.apply(Criar_update, axis=1)

updateFinal = df['UPDTE'].value_counts()

# Define os cabeçalhos
cabecalhos = df.columns.tolist()

# Imprime a tabela formatada
print(tabulate(df, headers=cabecalhos, tablefmt="pretty"))

# Fecha a conexão
conn.close()
