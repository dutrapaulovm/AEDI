# Exercício 35: A Conjectura de Collatz
# (Seção 2, Exercício 29 da Lista)
# Objetivo: Solicitar um número inicial n positivo, imprimir a sequência gerada pela Conjectura de Collatz até chegar a 1 e exibir o número de passos necessários.

# Passo 1: Leitura do número inicial n
n = input("Digite o número inicial (inteiro positivo n): ")
n = int(n)

# Passo 2: Inicialização do contador de passos
passos = 0

# Exibe o termo inicial da sequência
print(n, end="")

# Passo 3: Laço de repetição enquanto o número não chega a 1
while n > 1:
    # Se n for par
    if n % 2 == 0:
        n = n // 2
    # Se n for ímpar
    else:
        n = (n * 3) + 1
        
    # Incrementa o número de passos
    passos = passos + 1
    
    # Imprime o próximo termo
    print(f" -> {n}", end="")

# Passo 4: Exibição da quantidade total de passos ao final
print(f"\nPassos: {passos}")
