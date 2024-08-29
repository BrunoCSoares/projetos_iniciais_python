# · Tendo como base o valor da cotação do dólar (em reais) do dia, faça a conversão de um valor em dólares para reais.

cotacao = float(input("Informe a cotação atual do dolar: "))
dolar = float(input("Informe quantos dolares deseja calcular: "))

reais = dolar * cotacao

print("vc tem R$", reais, "em dolares")