# Exercício 26: Volatilidade Histórica
# Objetivo: Desvio padrão amostral de 3 retornos.
import math

r1 = input("Retorno dia 1: ")
r1 = float(r1)
r2 = input("Retorno dia 2: ")
r2 = float(r2)
r3 = input("Retorno dia 3: ")
r3 = float(r3)

media = (r1 + r2 + r3) / 3
soma_quadrados = (r1 - media)**2 + (r2 - media)**2 + (r3 - media)**2
volatilidade = math.sqrt(soma_quadrados / (3 - 1))

print(f"Volatilidade histórica: {volatilidade:.4f}")
