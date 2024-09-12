IF OBJECT_ID('tempdb..#DATASsEPARADAS') IS NOT NULL DROP TABLE #DATASsEPARADAS;
SELECT 
	YEAR([Data Operação]) AS Ano,
	MONTH([Data Operação]) AS MES,
	DAY([Data Operação]) AS DIA,
	*
INTO #DATASsEPARADAS
FROM CAIXA

/*SOMA TOTAL POR ANO ARRECADADA*/
SELECT [Ano], SUM([Valor Total]) as SOMA_TOTAL FROM
#DATASsEPARADAS
GROUP BY [Ano]

/*SOMA ARRECADA POR MES E ANO*/
IF OBJECT_ID('tempdb..#AnoMes') IS NOT NULL DROP TABLE #AnoMes;

-- Criação da tabela temporária
SELECT 
	CONCAT(Ano, '-', RIGHT('0' + CAST(MES AS VARCHAR(2)), 2)) AS DATAAM, 
	*
INTO #AnoMes
FROM #DATASsEPARADAS;

-- Consulta para sumarizar os valores
SELECT     
	DATAAM,
	SUM([Valor Total]) AS SOMA_TOTAL 
FROM #AnoMes
GROUP BY DATAAM
ORDER BY DATAAM


SELECT * FROM [dbo].[Cartões Crédito]

SELECT * FROM [dbo].[MovimentacaoDia]

SELECT * FROM [dbo].[Produto]

SELECT * FROM [dbo].[NFe]

SELECT * FROM [dbo].[Loja_Usuario]

SELECT [Nome Produto], SUM(PREÇO) AS PRECO
FROM [dbo].[Produto]
GROUP BY [Nome Produto]
ORDER BY PRECO DESC