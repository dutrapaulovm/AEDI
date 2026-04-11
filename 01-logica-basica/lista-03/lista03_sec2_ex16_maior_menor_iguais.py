# Exercício 16: Maior, Menor e Igualdade em Três Valores
# Objetivo: Identificar as extremidades e se existe overlap

# Passo 1
a = input("Valor a: ")
a = float(a)
b = input("Valor b: ")
b = float(b)
c = input("Valor c: ")
c = float(c)

# Passo 2: Avaliar igualdade global ou parcial
if a == b and b == c:
    print("Todos os valores são iguais")
else:
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
        
    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c
        
    # Passo 3: Exibir e Avaliar igualdades parciais
    print(f"Maior = {maior}, Menor = {menor}")
    if a == b or b == c or a == c:
        print("Há valores iguais no meio conjunto")
