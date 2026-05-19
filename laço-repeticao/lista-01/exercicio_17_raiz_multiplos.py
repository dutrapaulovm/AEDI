# Exercício 17: Raiz e Múltiplos
# Objetivo: Imprimir os números de 1 a 100, substituindo por "Raiz" se a raiz for inteira, por "Múltiplos" se for múltiplo de 5, ou mantendo o número.

# Passo 1: Laço de repetição de 1 a 100
for i in range(1, 101):
    # Calcula a raiz quadrada do número atual
    raiz = i ** 0.5
    
    # Passo 2: Verifica se a raiz quadrada é um número inteiro
    if raiz == int(raiz):
        print("Raiz")
    # Passo 3: Verifica se o número é múltiplo de 5
    elif i % 5 == 0:
        print("Múltiplos")
    else:
        # Passo 4: Caso contrário, imprime o próprio número
        print(i)
