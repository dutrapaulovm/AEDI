# Exercício 41: Área Triângulo por Coordenadas
# Objetivo: Área com 3 pontos.

x1 = input("x1: ")
x1 = float(x1)
y1 = input("y1: ")
y1 = float(y1)
x2 = input("x2: ")
x2 = float(x2)
y2 = input("y2: ")
y2 = float(y2)
x3 = input("x3: ")
x3 = float(x3)
y3 = input("y3: ")
y3 = float(y3)

A = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

print(f"Área do triângulo: {A:.2f}")
