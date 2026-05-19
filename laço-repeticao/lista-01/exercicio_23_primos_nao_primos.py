# Exercício 23: Primos e Não Primos (Soma)
# Objetivo: Calcular a soma das frações dos números primos de 1 a n, e a soma das raízes quadradas dos não primos, exibindo os resultados individuais e totais.

# Passo 1: Leitura do limite superior n
n = input("Insira um número inteiro positivo: ")
n = int(n)

# Passo 2: Inicialização das somas acumuladoras
soma_primos = 0.0
soma_nao_primos = 0.0

# Passo 3: Laço de repetição de 1 até n para classificar e somar
for i in range(1, n + 1):
    # Verificação se o número i é primo
    eh_primo = True
    if i <= 1:
        eh_primo = False
    else:
        for divisor in range(2, i):
            if i % divisor == 0:
                eh_primo = False
                break
                
    # Acumula nas respectivas variáveis de acordo com a classificação
    if eh_primo:
        soma_primos = soma_primos + (1.0 / i)
    else:
        soma_nao_primos = soma_nao_primos + (i ** 0.5)

# Passo 4: Cálculo da soma total
soma_total = soma_primos + soma_nao_primos

# Passo 5: Exibição dos resultados
print(f"Soma das frações dos números primos: {soma_primos}")
print(f"Soma das raízes quadradas dos não primos: {soma_nao_primos}")
print(f"Soma total: {soma_total}")
