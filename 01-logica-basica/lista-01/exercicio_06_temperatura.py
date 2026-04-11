# Exercício 6: Conversor de Temperatura
# Objetivo: Converter graus Celsius para Fahrenheit.

# Passo 1: Entrada da temperatura em graus Celsius
celsius = input("Digite a temperatura em graus Celsius (°C): ")
celsius = float(celsius)

# Passo 2: Aplicação da fórmula de conversão para Fahrenheit
# Fórmula: F = (9 * C / 5) + 32
fahrenheit = (9 * celsius / 5) + 32

# Passo 3: Exibição do resultado
print(f"A temperatura de {celsius:.1f}°C equivale a {fahrenheit:.1f}°F.")
