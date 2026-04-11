# Exercício 4: Par ou Ímpar
# Objetivo: Indicar paridade do número

# Passo 1: Leitura e conversão
num = input("Digite um número inteiro: ")
num = int(num)

# Passo 2: Verificação de resto para paridade
if num % 2 == 0:
    # Passo 3a: Resto por 2 igual a zero
    print("O número é PAR")
else:
    # Passo 3b: Resto diferente de zero
    print("O número é ÍMPAR")
