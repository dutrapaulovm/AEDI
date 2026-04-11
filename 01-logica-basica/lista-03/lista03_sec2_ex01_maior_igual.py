# Exercício 1: Maior ou Igual
# Objetivo: Identificar o maior de dois números

# Passo 1: Leitura e conversão
a = input("Digite o primeiro número: ")
a = int(a)
b = input("Digite o segundo número: ")
b = int(b)

# Passo 2: Comparação
if a > b:
    # Passo 3a: A é o maior
    print(f"O número {a} é o maior")
elif b > a:
    # Passo 3b: B é o maior
    print(f"O número {b} é o maior")
else:
    # Passo 3c: Ocorreu empate
    print("Os números são iguais")
