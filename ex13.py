# · O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).

fabrica = float(input("Informe o custo de fábrica: "))

custo = fabrica + fabrica*0.28 + fabrica*0.45

print("o custo final do carro é de R$", custo)