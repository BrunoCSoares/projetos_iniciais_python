# · Dada uma temperatura na escala Fahrenheit, faça a conversão e exiba a temperatura equivalente em Celsius. Celsius = 5/9 * (F - 32)

fahrenheit = float(input("Informe a temperatura em graus fahrenheits: "))

celcius = 5/9*(fahrenheit-32)

print(fahrenheit, "° fahrenheit são", celcius, "° celcius")