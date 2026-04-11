# Exercício 11: Pagamento de Empréstimo
# Objetivo: Calcular PMT.

P = input("Montante do empréstimo: ")
P = float(P)
r = input("Taxa de juros mensal (decimal): ")
r = float(r)
n = input("Número de meses: ")
n = int(n)

PMT = (P * r * (1 + r)**n) / ((1 + r)**n - 1)

print(f"Pagamento mensal (PMT): R$ {PMT:.2f}")
