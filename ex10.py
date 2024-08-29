# · Escreva um algoritmo para calcular a média aritmética de 3 avaliações que deverão ser informadas. Por fim, exiba o valor da média.

checkpoint1 = float(input("digite a nota no checkpoint 1: "))
checkpoint2 = float(input("digite a nota no checkpoint 2: "))
checkpoint3 = float(input("digite a nota no checkpoint 3: "))
media = (checkpoint1+checkpoint2+checkpoint3)/3

print(f"a média do aluno é {media:.2f}")