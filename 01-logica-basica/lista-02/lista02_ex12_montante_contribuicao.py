# Exercício 12: Montante com Contribuições
# Objetivo: Juros e aportes regulares.

P = input("Montante inicial: ")
P = float(P)
PMT = input("Pagamento periódico: ")
PMT = float(PMT)
r = input("Taxa de juros por período (decimal): ")
r = float(r)
n = input("Número de períodos: ")
n = int(n)

M = P * (1 + r)**n + PMT * (((1 + r)**n - 1) / r)

print(f"Montante final: R$ {M:.2f}")
