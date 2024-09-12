import pandas as pd
from tabulate import tabulate
import pyodbc

# Define a string de conexão
conn_str = (
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-0T24SC8;"
    "DATABASE=BANCO_TESTE;"
    "Trusted_Connection=yes;"
)

# Estabelece a conexão e executa a consulta dentro do gerenciador de contexto
try:
    with pyodbc.connect(conn_str) as conn:
        # Consulta principal
        QueryPrincipal = "SELECT NOME, IDADE, GENERO, PESO_KG, ALTURA_CM FROM PESSOA"
        resultados = pd.read_sql(QueryPrincipal, conn)

        def CalculoIMC(row):
            alturaCm = float(row['ALTURA_CM']) if row['ALTURA_CM'] else 0
            pesoKg = float(row['PESO_KG']) if row['PESO_KG'] else 0

            if pesoKg > 0 and alturaCm > 0:
                alturaM = alturaCm / 100  # Convertendo altura de cm para metros
                IMC = pesoKg / (alturaM * alturaM)
                return IMC
            return 0

        # Aplicando a função CalculoIMC a cada linha do DataFrame
        resultados['IMC'] = resultados.apply(CalculoIMC, axis=1)

        def Imc(row):
            imc = row['IMC']
            if imc > 0:
                if imc < 18.5:
                    return "Abaixo de peso"
                elif imc >= 18.5 and imc <= 24.9:
                    return "Peso normal"
                elif imc >= 25 and imc <= 29.9:
                    return "Sobrepeso"
                else:
                    return "Obesidade"
            return ""

        resultados['Resultado'] = resultados.apply(Imc, axis=1)

        # Configuração para exibir todas as linhas e colunas no console
        pd.set_option('display.max_rows', 50000)
        pd.set_option('display.max_columns', None)

        # Gera um relatório no console
        cabecalhos = resultados.columns.tolist()
        print(tabulate(resultados, headers=cabecalhos, tablefmt="fancy_grid"))

        # Opcional: gerar um relatório Excel
        # resultados.to_excel('ArquivosXLSX/IMC.xlsx', index=False)

except pyodbc.Error as e:
    print("Erro ao conectar ao banco de dados:", e)
