# Exercício 1: Progressão Aritmética (Soma Simples)
# Objetivo: Calcular a soma de todos os números inteiros de 1 até n.

# Passo 1: Leitura do limite superior n
n = input("Digite o limite superior (n): ")
n = int(n)

# Passo 2: Inicialização da variável acumuladora (soma)
soma = 0

# Passo 3: Laço de repetição de 1 até n para acumular a soma
for i in range(1, n + 1):
    soma = soma + i

# Passo 4: Exibição do resultado
print(f"A soma de 1 até {n} é: {soma}")
