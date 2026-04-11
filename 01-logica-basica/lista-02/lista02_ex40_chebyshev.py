# Exercício 40: Distância de Chebyshev
# Objetivo: Distância máxima.

x1 = input("x1: ")
x1 = float(x1)
y1 = input("y1: ")
y1 = float(y1)
x2 = input("x2: ")
x2 = float(x2)
y2 = input("y2: ")
y2 = float(y2)

d = max(abs(x2 - x1), abs(y2 - y1))

print(f"Distância de Chebyshev: {d:.2f}")
