# · Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

anos = int(input("Informe sua idade em anos: "))
meses = int(input("Informe os meses: "))
dias = int(input("Informe os dias: "))

totDias = anos*365 + meses*30 + dias

print("você tem", totDias, "dias de vida")