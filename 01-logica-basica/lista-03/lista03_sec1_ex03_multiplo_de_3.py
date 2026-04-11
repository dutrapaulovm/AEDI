# Exercício 3: Múltiplo de 3
# Objetivo: Verificar divisibilidade por 3

# Passo 1: Leitura e conversão
n = input("Digite um número inteiro: ")
n = int(n)

# Passo 2: Lógica de divisibilidade usando o resto (%)
if n % 3 == 0:
    # Passo 3a: O resto é 0, então é múltiplo
    print("É múltiplo de 3")
else:
    # Passo 3b: O resto não é 0
    print("Não é múltiplo de 3")
