# Exercício 19: Área do Triângulo (Heron)
# Objetivo: Área com 3 lados.
import math

a = input("Lado a: ")
a = float(a)
b = input("Lado b: ")
b = float(b)
c = input("Lado c: ")
c = float(c)

s = (a + b + c) / 2
A = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"Área do triângulo: {A:.2f}")
