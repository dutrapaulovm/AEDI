# Exercício 26: Sub-nichos de Mercado
# Objetivo: Barato, médio, caro

# Passo 1
p = input("Valor do bem: R$ ")
preco = float(p)

# Passo 2
if preco >= 1000:
    print("Caro")
elif preco >= 500 and preco <= 999:
    print("Médio")
else:
    print("Barato")
