# Exercício 13: Par ou Ímpar
# Objetivo: Validar se um número inteiro é par ou ímpar utilizando desvio condicional.

# Passo 1: Leitura do número
numero = input("Digite um número inteiro: ")
numero = int(numero)

# Passo 2: Lógica com o operador MOD (%)
# A divisão por 2 de um número par sempre tem resto 0.
resto = numero % 2

if resto == 0:
    # Passo 3.1: Confirmação condicional
    print(f"O número {numero} é PAR.")
else:
    # Passo 3.2: O que não é par, obrigatoriamente é ímpar
    print(f"O número {numero} é ÍMPAR.")
