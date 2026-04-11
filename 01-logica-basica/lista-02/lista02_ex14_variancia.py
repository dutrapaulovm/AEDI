# Exercício 14: Variância
# Objetivo: Calcular variância de 3 notas.

n1 = input("Nota 1: ")
n1 = float(n1)
n2 = input("Nota 2: ")
n2 = float(n2)
n3 = input("Nota 3: ")
n3 = float(n3)

media = (n1 + n2 + n3) / 3

variancia = ((n1 - media)**2 + (n2 - media)**2 + (n3 - media)**2) / 3

print(f"Variância: {variancia:.4f}")
