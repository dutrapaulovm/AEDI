# Exercício 17: Média Ponderada
# Objetivo: Média com pesos.

n1 = input("Nota 1: ")
n1 = float(n1)
p1 = input("Peso 1: ")
p1 = float(p1)
n2 = input("Nota 2: ")
n2 = float(n2)
p2 = input("Peso 2: ")
p2 = float(p2)
n3 = input("Nota 3: ")
n3 = float(n3)
p3 = input("Peso 3: ")
p3 = float(p3)

media = (n1*p1 + n2*p2 + n3*p3) / (p1 + p2 + p3)

print(f"Média ponderada: {media:.2f}")
