# Exercício 14: Soma de Potências e Frações
# Objetivo: Calcular a soma das frações de potências dos números de 1 até n (1 / i^i).

# Passo 1: Leitura do número inteiro positivo n
n = input("Insira um número inteiro positivo: ")
n = int(n)

# Passo 2: Inicialização da soma acumuladora
soma = 0.0

# Passo 3: Laço de repetição de 1 até n
for i in range(1, n + 1):
    # Passo 3.1: Cálculo manual de i elevado a i (sem usar ** ou pow)
    potencia_ii = 1
    for _ in range(i):
        potencia_ii = potencia_ii * i
        
    # Passo 3.2: Acumula a fração 1 / i^i na soma total
    soma = soma + (1.0 / potencia_ii)

# Passo 4: Exibição do resultado
print(f"Soma das potências e frações: {soma}")
