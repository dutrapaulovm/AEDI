# Exercício 22: Triângulo Total
# Objetivo: Validação prévia + classificação

# Passo 1: Leitura e conversão
a = input("Lado A: ")
a = float(a)
b = input("Lado B: ")
b = float(b)
c = input("Lado C: ")
c = float(c)

# Passo 2: O teorema de desigualdade geométrica
pode_ser_triangulo = (a < b + c) and (b < a + c) and (c < a + b)

if pode_ser_triangulo:
    # Passo 3: Classificação correta
    if a == b and b == c:
        print("Equilátero")
    elif a == b or b == c or a == c:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("As arestas não conectam em um triângulo válido")
