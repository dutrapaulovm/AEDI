# Exercício 30: Cálculo de Variância e Desvio Padrão Populacional
# Objetivo: Cadastrar 10 valores reais positivos em um vetor, calcular a média, a variância populacional (divisor N) e o desvio padrão populacional.

# Passo 1: Inicialização do vetor de 10 elementos
vetor = [0.0] * 10

# Passo 2: Leitura com validação (> 0)
print("--- Estatística Populacional - Variância e Desvio Padrão ---")
for i in range(10):
    valido = False
    while not valido:
        val = input(f"Digite o {i+1}º valor real positivo: ")
        val = float(val)
        if val > 0.0:
            vetor[i] = val
            valido = True
        else:
            print("Erro: O valor deve ser positivo e maior que zero.")

# Passo 3: Cálculo da média aritmética simples
soma = 0.0
for i in range(10):
    soma = soma + vetor[i]
media = soma / 10.0

# Passo 4: Cálculo da variância populacional (divisor N = 10)
# Formula: σ² = sum_{i=0..9} (xi - x̄)^2 / 10
soma_quadrados_diferencas = 0.0
for i in range(10):
    diferenca = vetor[i] - media
    soma_quadrados_diferencas = soma_quadrados_diferencas + (diferenca * diferenca)
    
variancia_populacional = soma_quadrados_diferencas / 10.0

# Passo 5: Cálculo do desvio padrão populacional (raiz quadrada da variância populacional)
# σ = sqrt(σ²)
desvio_padrao_populacional = variancia_populacional ** 0.5

# Passo 6: Exibição dos resultados estatísticos
print("\n--- RELATÓRIO ESTATÍSTICO POPULACIONAL ---")
print(f"Vetor de Amostras: {vetor}")
print(f"Média Aritmética (x̄):           {media:.4f}")
print(f"Variância Populacional (σ²):     {variancia_populacional:.4f}")
print(f"Desvio Padrão Populacional (σ): {desvio_padrao_populacional:.4f}")
