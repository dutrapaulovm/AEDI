# Exercício 15: Volume da Esfera
# Objetivo: Calcular o volume fornecendo o raio.
import math

r = input("Raio da esfera: ")
r = float(r)

V = (4/3) * math.pi * r**3

print(f"Volume da esfera: {V:.2f}")
