# Exercício 25: Número Deficiente
# Objetivo: Ler um número inteiro positivo e verificar se ele é um número deficiente.

# Passo 1: Leitura do número
numero = input("Digite um número inteiro positivo: ")
numero = int(numero)

# Passo 2: Soma dos divisores próprios (excluindo ele mesmo)
soma_divisores = 0

# Laço para testar todos os possíveis divisores de 1 até numero - 1
for i in range(1, numero):
    if numero % i == 0:
        soma_divisores = soma_divisores + i

# Passo 3: Verificação e exibição do resultado
if soma_divisores < numero:
    print(f"O número {numero} é um número deficiente (soma dos divisores = {soma_divisores}).")
else:
    print(f"O número {numero} NÃO é um número deficiente (soma dos divisores = {soma_divisores}).")
