# Exercício 2: Aproximação do Número de Euler (e)
# Objetivo: Aproximar o número de Euler através da soma dos inversos dos fatoriais de 0 até n.

# Passo 1: Leitura do limite superior n
n = input("Digite o limite superior (n): ")
n = int(n)

# Passo 2: Inicialização de acumulador da soma e do fatorial
soma_euler = 0.0
fatorial = 1

# Passo 3: Laço de repetição de 0 até n
for i in range(n + 1):
    # O fatorial de 0 é 1. Para os próximos, multiplicamos pelo número atual.
    if i > 0:
        fatorial = fatorial * i
    
    # Soma o inverso do fatorial atual
    soma_euler = soma_euler + (1.0 / fatorial)

# Passo 4: Exibição do resultado
print(f"O número de Euler aproximado até n={n} é: {soma_euler:.10f}")
