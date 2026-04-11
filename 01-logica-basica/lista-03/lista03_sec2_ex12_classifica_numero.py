# Exercício 12: Classificador de Número Múltiplo
# Objetivo: Teste complexo lógico

# Passo 1: Leitura e casting
num = input("Número inteiro: ")
num = int(num)

# Passo 2: Encadeamento descritivo da lógica pedida no enunciado
if num > 0 and num % 2 == 0:
    print("Positivo e par")
elif num > 0 and num % 2 != 0:
    print("Positivo e ímpar")
elif num < 0:
    print("Negativo")
else:
    # A única possibilidade extra lógica
    print("Zero")
