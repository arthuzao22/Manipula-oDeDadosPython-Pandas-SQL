import pandas as pd
from sqlalchemy import create_engine
import pyodbc

# String de conexão com SQL Server
conn_str = (
    "mssql+pyodbc:///?odbc_connect="
    "DRIVER={ODBC Driver 17 for SQL Server};" 
    "SERVER=DESKTOP-0T24SC8;"
    "DATABASE=BANCO_TESTE;"
    "Trusted_Connection=yes;"
)

# Caminho para o arquivo CSV
csv_file = 'C:/Users/arthu/Downloads/dados5 (1).csv'

# Nome da tabela no SQL Server
table_name = 'AuE'

# Lendo o CSV com pandas
df = pd.read_csv(csv_file)

# Verificando os tipos de dados das colunas do DataFrame
print("Tipos de dados do DataFrame:")
print(df.dtypes)

# Corrija os tipos de dados, se necessário
# Exemplo: df['some_column'] = df['some_column'].astype('str')

# Criando a conexão com o banco de dados SQL Server
engine = create_engine(conn_str)

# Testando a conexão
try:
    with engine.connect() as conn:
        print("Conexão ao banco de dados estabelecida com sucesso.")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

# Criando uma tabela temporária para verificar se o problema persiste
temp_table_name = 'TempTable'

try:
    df.head(10).to_sql(temp_table_name, con=engine, if_exists='replace', index=False)
    print(f"Dados inseridos na tabela temporária {temp_table_name} com sucesso!")
except Exception as e:
    print(f"Erro ao inserir dados na tabela temporária: {e}")

# Tentando inserir os dados na tabela principal
try:
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print("Dados inseridos com sucesso na tabela principal!")
except Exception as e:
    print(f"Erro ao inserir dados na tabela principal: {e}")
