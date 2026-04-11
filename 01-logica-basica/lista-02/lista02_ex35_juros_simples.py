# Exercício 35: Juros Simples
# Objetivo: Montante.

P = input("Capital inicial: ")
P = float(P)
r = input("Taxa por período (em decimal): ")
r = float(r)
t = input("Tempo: ")
t = float(t)

M = P * (1 + r * t)

print(f"Montante (Juros Simples): {M:.2f}")
