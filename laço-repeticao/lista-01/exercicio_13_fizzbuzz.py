# Exercício 13: FizzBuzz
# Objetivo: Imprimir os números de 1 a 100, substituindo múltiplos de 3 por "Fizz", de 5 por "Buzz" e de ambos por "FizzBuzz".

# Passo 1: Laço de repetição de 1 a 100
for i in range(1, 101):
    # Passo 2: Verifica se é múltiplo de ambos (3 e 5)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Passo 3: Verifica se é múltiplo de 3 apenas
    elif i % 3 == 0:
        print("Fizz")
    # Passo 4: Verifica se é múltiplo de 5 apenas
    elif i % 5 == 0:
        print("Buzz")
    else:
        # Passo 5: Caso contrário, imprime o número
        print(i)
