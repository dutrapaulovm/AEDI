# Exercício 6: Volume do Tronco de Cone
# Objetivo: Obter volume de um tronco de cone circular reto.
import math

R = input("Raio da base maior: ")
R = float(R)
r = input("Raio da base menor: ")
r = float(r)
h = input("Altura: ")
h = float(h)

V = (1/3) * math.pi * h * (R**2 + R*r + r**2)

print(f"Volume do tronco: {V:.2f}")
