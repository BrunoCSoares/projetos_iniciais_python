# · Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.

salarioFixo = float(input("Informe o salário fixo do vendedor: "))
numCarros = int(input("Informe o número de carros vendidos por ele: "))
comissao = float(input("Informe a comissão por carro vendido: "))
valorVendas = float(input("Informe o valor de suas vendas: "))

totSalario = salarioFixo + numCarros*comissao + valorVendas*0.05

print("O salário final do vendedor será de R$", totSalario)