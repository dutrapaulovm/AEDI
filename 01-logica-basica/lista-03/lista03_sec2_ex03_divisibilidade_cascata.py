# Exercício 3: Divisível por 10, 5 ou 2
# Objetivo: Chechar múltiplos sucessivos

# Passo 1: Leitura e conversão
n = input("Digite um número inteiro: ")
n = int(n)

# Passo 2: Validações do maior limitador ao menor
if n % 10 == 0:
    # Passo 3a: Divisível por 10 (consequentemente por 5 e 2)
    print("Divisível por 10")
elif n % 5 == 0:
    # Passo 3b: Apenas divisível por 5 (e não por 10)
    print("Divisível por 5")
elif n % 2 == 0:
    # Passo 3c: Apenas divisível por 2 (e não por 10)
    print("Divisível por 2")
else:
    # Passo 3d: Restante
    print("Não divisível")
