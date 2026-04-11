# Exercício 27: Volume do Cilindro
# Objetivo: Volume.
import math

r = input("Raio da base: ")
r = float(r)
h = input("Altura: ")
h = float(h)

V = math.pi * r**2 * h

print(f"Volume do cilindro: {V:.2f}")
