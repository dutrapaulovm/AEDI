# Exercício 5: Lei de Ohm - Tensão
# Objetivo: Calcular a tensão de um circuito.
import math

P = input("Potência (Watts): ")
P = float(P)
R = input("Resistência (Ohms): ")
R = float(R)

V = math.sqrt(P * R)

print(f"A tensão é: {V:.2f} V")
