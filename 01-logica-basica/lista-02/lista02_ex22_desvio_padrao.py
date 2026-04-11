# Exercício 22: Desvio Padrão
# Objetivo: Calcular desvio padrão de 3 notas.
import math

n1 = input("Nota 1: ")
n1 = float(n1)
n2 = input("Nota 2: ")
n2 = float(n2)
n3 = input("Nota 3: ")
n3 = float(n3)

media = (n1 + n2 + n3) / 3
variancia = ((n1 - media)**2 + (n2 - media)**2 + (n3 - media)**2) / 3
desvio = math.sqrt(variancia)

print(f"Desvio padrão: {desvio:.4f}")
