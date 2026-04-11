# Exercício 2: Caixa Eletrônico
# Objetivo: Simular saque com menor quantidade de notas.

V = input("Digite o valor do saque: R$ ")
V = int(V)

# Notas de 100
n100 = V // 100
V = V % 100

# Notas de 50
n50 = V // 50
V = V % 50

# Notas de 20
n20 = V // 20
V = V % 20

# Notas de 10
n10 = V // 10
V = V % 10

print("Notas entregues:")
print(f"100: {n100}")
print(f"50: {n50}")
print(f"20: {n20}")
print(f"10: {n10}")
if V > 0:
    print(f"Valor restante impossível de sacar com as notas disponíveis: R$ {V}")
