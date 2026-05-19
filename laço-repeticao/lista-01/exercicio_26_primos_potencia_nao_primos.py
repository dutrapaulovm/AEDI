# Exercício 26: Primos com Potência e Não Primos (Soma)
# Objetivo: Calcular a soma das frações dos números primos de 1 a n (com cada primo elevado a si mesmo) e a soma das raízes quadradas dos não primos.

# Passo 1: Leitura do número inteiro positivo n
n = input("Insira um número inteiro positivo: ")
n = int(n)

# Passo 2: Inicialização das somas acumuladoras
soma_primos = 0.0
soma_nao_primos = 0.0

# Passo 3: Laço de repetição de 1 até n
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
                
    # Passo 4: Acumulação baseada na classificação de primo/não-primo
    if eh_primo:
        # Calcula a potência i^i manualmente
        potencia_ii = 1
        for _ in range(i):
            potencia_ii = potencia_ii * i
            
        # Acumula a fração 1 / i^i
        soma_primos = soma_primos + (1.0 / potencia_ii)
    else:
        # Acumula a raiz quadrada do número não primo
        soma_nao_primos = soma_nao_primos + (i ** 0.5)

# Passo 5: Cálculo da soma total e exibição dos resultados
soma_total = soma_primos + soma_nao_primos

print(f"Soma das frações dos números primos (potência de si mesmo): {soma_primos}")
print(f"Soma das raízes quadradas dos não primos: {soma_nao_primos}")
print(f"Soma total: {soma_total}")
