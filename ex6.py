# · Crie um algoritmo que solicite ao usuário seu consumo de energia elétrica (em kWh), que deve ser uma variável real. O algoritmo deve, então, calcular o total da conta, considerando que cada kWh custa R$ 0,20.

consumo = float(input("Informe seu consumo elétrico em kWh: "))

conta = consumo * 0.20

print("sua conta de energia será", conta)