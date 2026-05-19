# Exercício 3: Série de Leibniz para pi
# Objetivo: Aproxime o valor de pi usando a série de Leibniz alternada.

# Passo 1: Leitura do limite superior n
n = input("Digite o limite superior (n): ")
n = int(n)

# Passo 2: Inicialização do acumulador da série
soma_serie = 0.0

# Passo 3: Laço de repetição de 0 até n para calcular a série alternada
for i in range(n + 1):
    # Determina o sinal alternado (-1)^i
    if i % 2 == 0:
        sinal = 1.0
    else:
        sinal = -1.0
        
    # Calcula o termo correspondente e acumula
    termo = sinal / (2 * i + 1)
    soma_serie = soma_serie + termo

# Passo 4: Multiplica por 4 para obter a aproximação de pi
pi_aproximado = 4.0 * soma_serie

# Passo 5: Exibição do resultado
print(f"O valor de pi aproximado até n={n} é: {pi_aproximado:.10f}")
