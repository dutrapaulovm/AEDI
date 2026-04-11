# Exercício 21: Distância de Minkowski
# Objetivo: Calcular a distância de Minkowski entre dois pontos.

x1 = input("x1: ")
x1 = float(x1)
y1 = input("y1: ")
y1 = float(y1)
x2 = input("x2: ")
x2 = float(x2)
y2 = input("y2: ")
y2 = float(y2)
p = input("Parâmetro p: ")
p = float(p)

d = (abs(x2 - x1)**p + abs(y2 - y1)**p)**(1 / p)

print(f"Distância de Minkowski: {d:.4f}")
