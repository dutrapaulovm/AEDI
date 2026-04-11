# Exercício 24: Equação do Segundo Grau
# Objetivo: Bhaskara.
import math

a = input("A: ")
a = float(a)
b = input("B: ")
b = float(b)
c = input("C: ")
c = float(c)

delta = b**2 - 4*a*c

if delta < 0:
    print("A equação não possui raízes reais.")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Raiz 1 (x1): {x1:.2f}")
    print(f"Raiz 2 (x2): {x2:.2f}")
