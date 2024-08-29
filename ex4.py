# · Sabendo o peso e a altura de uma pessoa, calcule o IMC (índice de massa corpórea) por meio da fórmula: IMC = peso/altura*altura.

peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))

imc = peso/altura**2

print(f"o seu imc é {imc}")