# Exercício 34: Verificador de Números Primos
# (Seção 2, Exercício 28 da Lista)
# Objetivo: Receber um número inteiro positivo X e determinar se ele é primo ou não, imprimindo a resposta apenas uma única vez ao final.

# Passo 1: Leitura do número X
x = input("Digite um número inteiro positivo (X): ")
x = int(x)

# Passo 2: Inicialização da flag de controle eh_primo
eh_primo = True

# Passo 3: Verificação de casos especiais (menores ou iguais a 1)
if x <= 1:
    eh_primo = False
else:
    # Passo 4: Laço de repetição de 2 até X-1 para encontrar possíveis divisores
    for divisor in range(2, x):
        if x % divisor == 0:
            eh_primo = False
            break  # Interrompe o laço assim que encontra o primeiro divisor

# Passo 5: Exibição única do resultado ao final
if eh_primo:
    print("É primo")
else:
    print("Não é primo")
