# Exercício 29: Graus para Radianos
# Objetivo: Conversão.
import math

graus = input("Ângulo em graus: ")
graus = float(graus)
radianos = graus * math.pi / 180

print(f"Em radianos: {radianos:.4f}")
