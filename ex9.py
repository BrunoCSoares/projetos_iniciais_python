# · Um estacionamento cobra R$ 5,00 por hora. Escreva um algoritmo que pergunte ao usuário qual foi o período de permanência em horas e calcule o total a pagar.

horas = int(input("Iforme o total de horas que esteve no estacionamento: "))

conta = float(horas * 5)

print(f"sua conta é de R${conta}")