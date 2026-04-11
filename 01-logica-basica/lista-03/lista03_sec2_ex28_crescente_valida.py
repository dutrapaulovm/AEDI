# Exercício 28: Verificação de Ordenação
# Objetivo: Prever o estado direcional dos números

# Passo 1
a = input("Num 1: ")
a = float(a)
b = input("Num 2: ")
b = float(b)
c = input("Num 3: ")
c = float(c)

# Passo 2: Verificão puramente relacional múltipla
if a < b and b < c:
    print("Crescente")
elif a > b and b > c:
    print("Decrescente")
else:
    print("Desordenado")
