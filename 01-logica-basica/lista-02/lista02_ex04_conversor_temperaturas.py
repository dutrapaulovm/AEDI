# Exercício 4: Conversão de Temperaturas
# Objetivo: Converter Celsius para Kelvin e Fahrenheit.

C = input("Digite a temperatura em Celsius: ")
C = float(C)

K = C + 273.15
F = (9/5) * C + 32

print(f"Kelvin: {K:.2f} K")
print(f"Fahrenheit: {F:.2f} °F")
