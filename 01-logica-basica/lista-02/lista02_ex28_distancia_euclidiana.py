# Exercício 28: Distância Euclidiana
# Objetivo: Distância comum.
import math

x1 = input("x1: ")
x1 = float(x1)
y1 = input("y1: ")
y1 = float(y1)
x2 = input("x2: ")
x2 = float(x2)
y2 = input("y2: ")
y2 = float(y2)

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"Distância euclidiana: {d:.2f}")
