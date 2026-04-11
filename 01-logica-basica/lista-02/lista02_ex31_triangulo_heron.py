# Exercício 31: Triângulo (Heron)
# Objetivo: Outra versão Heron.
import math

a = input("Lado a: ")
a = float(a)
b = input("Lado b: ")
b = float(b)
c = input("Lado c: ")
c = float(c)

s = (a + b + c) / 2
A = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"Área (Heron): {A:.2f}")
