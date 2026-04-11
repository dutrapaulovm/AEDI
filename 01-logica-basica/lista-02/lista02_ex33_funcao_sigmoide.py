# Exercício 33: Função Sigmoide
# Objetivo: Redes neurais, ativação.
import math

x = input("Entrada (x): ")
x = float(x)
saida = 1 / (1 + math.exp(-x))

print(f"Saída sigmoide: {saida:.4f}")
