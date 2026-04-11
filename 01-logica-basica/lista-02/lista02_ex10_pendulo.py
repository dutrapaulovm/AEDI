# Exercício 10: Período do Pêndulo
# Objetivo: Calcular o período de um pêndulo simples.
import math

L = input("Comprimento do fio (m): ")
L = float(L)
g = 9.81

T = 2 * math.pi * math.sqrt(L / g)

print(f"Período do pêndulo: {T:.2f} s")
