# Exercício 28: Frações de Pares e Raízes Cúbicas de Ímpares (Soma)
# (Seção 2, Exercício 22 da Lista)
# Objetivo: Calcular a soma das frações dos números pares de 1 até n, e a soma das raízes cúbicas dos números ímpares, exibindo os resultados individuais e totais.

# Passo 1: Leitura do número inteiro positivo n
n = input("Insira um número inteiro positivo: ")
n = int(n)

# Passo 2: Inicialização das somas acumuladoras
soma_pares = 0.0
soma_impares = 0.0

# Passo 3: Laço de repetição de 1 até n
for i in range(1, n + 1):
    if i % 2 == 0:
        # Para números pares: soma a fração 1/i
        soma_pares = soma_pares + (1.0 / i)
    else:
        # Para números ímpares: soma a raiz cúbica (i elevado a 1/3)
        raiz_cubica = i ** (1.0 / 3.0)
        soma_impares = soma_impares + raiz_cubica

# Passo 4: Cálculo da soma total
soma_total = soma_pares + soma_impares

# Passo 5: Exibição dos resultados
print(f"Soma das frações dos números pares: {soma_pares}")
print(f"Soma das raízes cúbicas dos números ímpares: {soma_impares}")
print(f"Soma total: {soma_total}")
