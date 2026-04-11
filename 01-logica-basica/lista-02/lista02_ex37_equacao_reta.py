# Exercício 37: Equação da Reta
# Objetivo: Passando por 2 pontos.

x1 = input("x1: ")
x1 = float(x1)
y1 = input("y1: ")
y1 = float(y1)
x2 = input("x2: ")
x2 = float(x2)
y2 = input("y2: ")
y2 = float(y2)

if x2 - x1 == 0:
    print(f"Reta vertical: x = {x1}")
else:
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    print(f"Equação da reta: y = {m:.2f}x + ({b:.2f})")
