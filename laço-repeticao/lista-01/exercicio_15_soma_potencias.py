# Exercício 15: Soma de Potências
# Objetivo: Calcular a soma das potências (quadrados) de 1 até n (1^2 + 2^2 + ... + n^2).

# Passo 1: Leitura do número inteiro positivo n
n = input("Insira um número inteiro positivo: ")
n = int(n)

# Passo 2: Inicialização da soma acumuladora
soma = 0

# Passo 3: Laço de repetição de 1 até n
for i in range(1, n + 1):
    # Calcula i^2 manualmente (i * i) e acumula
    quadrado = i * i
    soma = soma + quadrado

# Passo 4: Exibição do resultado
print(f"Soma das potências: {soma}")
