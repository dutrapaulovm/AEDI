# Exercício 16: Valor Futuro da Anuidade
# Objetivo: Aportes regulares.

P = input("Pagamento periódico (P): ")
P = float(P)
r = input("Taxa de juros por período (em decimal): ")
r = float(r)
n = input("Total de períodos: ")
n = int(n)

FV = P * (((1 + r)**n - 1) / r)

print(f"Valor futuro: R$ {FV:.2f}")
