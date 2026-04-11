# Exercício 9: Ordem Decrescente
# Objetivo: Ordenar visualmente.

# Passo 1: Leitura / Cast manual
a = input("a: ")
a = float(a)
b = input("b: ")
b = float(b)
c = input("c: ")
c = float(c)

# Passo 2: Testes lógicos de árvore (comparação manual)
if a > b and a > c:
    # A é o maior
    if b > c:
        print(f"{a}, {b}, {c}")
    else:
        print(f"{a}, {c}, {b}")
elif b > a and b > c:
    # B é o maior
    if a > c:
        print(f"{b}, {a}, {c}")
    else:
        print(f"{b}, {c}, {a}")
else:
    # C é o maior
    if a > b:
        print(f"{c}, {a}, {b}")
    else:
        print(f"{c}, {b}, {a}")
