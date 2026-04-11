# Exercício 8: Área de Superfície do Cilindro
# Objetivo: Calcular área do cilindro.
import math

r = input("Raio da base: ")
r = float(r)
h = input("Altura do cilindro: ")
h = float(h)

A = 2 * math.pi * r * (r + h)

print(f"Área de superfície: {A:.2f}")
