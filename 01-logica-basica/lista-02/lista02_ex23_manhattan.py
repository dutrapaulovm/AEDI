# Exercício 23: Distância de Manhattan
# Objetivo: Calcular soma das distâncias absolutas.

x1 = input("x1: ")
x1 = float(x1)
y1 = input("y1: ")
y1 = float(y1)
x2 = input("x2: ")
x2 = float(x2)
y2 = input("y2: ")
y2 = float(y2)

d = abs(x2 - x1) + abs(y2 - y1)

print(f"Distância de Manhattan: {d:.2f}")
