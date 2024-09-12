import pandas as pd

# Importando a base de dados a partir de um arquivo Excel
tabela_vendas = pd.read_excel('Vendas.xlsx')

#VISUALIZAR RESULTADOS
pd.set_option('display.max_columns', None)

#FATURAMENTO POR LOJA
#print(tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum())

#QTDE DE PRODUTOS POR LOJA
#print(tabela_vendas[['ID Loja', 'Produto']].groupby('ID Loja').count())

#TICKET MEDIO POR LOJA
valor_final = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
qtde_vendido = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

result = (valor_final['Valor Final'] / qtde_vendido['Quantidade']).to_frame()
print(result)

#MANDAR POR E-MAIL
import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'arthurreisgonc@gmail.com'
mail.Subject = 'Tabela com Valor médio'
mail.Body = 'Tabelas'
mail.HTMLBody = '''
Prezados, <br>

Segue o relatorio de vendas por cada loja.<br>

Ticket médio por cada loja:<br>
{}

att,<br>
Arthur dos Reis Gonçalves<br>
'''
# To attach a file to the email (optional):
attachment  = "Path to the attachment"
mail.Attachments.Add(attachment)

mail.Send()
print("Email enviado")