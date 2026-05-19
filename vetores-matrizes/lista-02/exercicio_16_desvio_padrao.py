# Exercício 16: Cálculo de Desvio Padrão Amostral
# Objetivo: Cadastrar 8 valores reais positivos em um vetor, calcular a média, a variância amostral e o desvio padrão final (usando expoente 0.5 para raiz quadrada).

# Passo 1: Inicialização do vetor de 8 elementos
vetor = [0.0] * 8

# Passo 2: Leitura dos 8 valores reais com validação (> 0)
print("--- Analisador Estatístico - Desvio Padrão ---")
for i in range(8):
    valido = False
    while not valido:
        val = input(f"Digite o {i+1}º valor real positivo: ")
        val = float(val)
        if val > 0.0:
            vetor[i] = val
            valido = True
        else:
            print("Erro: Apenas valores maiores que zero são aceitos.")

# Passo 3: Cálculo da média aritmética simples
soma = 0.0
for i in range(8):
    soma = soma + vetor[i]
media = soma / 8.0

# Passo 4: Cálculo da variância amostral (soma de (xi - media)^2 / (N - 1))
soma_quadrados_diferencas = 0.0
for i in range(8):
    diferenca = vetor[i] - media
    quadrado_diferenca = diferenca * diferenca
    soma_quadrados_diferencas = soma_quadrados_diferencas + quadrado_diferenca
    
variancia = soma_quadrados_diferencas / 7.0  # N - 1 = 7

# Passo 5: Cálculo do desvio padrão (raiz quadrada da variância)
desvio_padrao = variancia ** 0.5

# Passo 6: Exibição dos resultados estatísticos
print("\n--- RELATÓRIO ESTATÍSTICO COMPLETO ---")
print(f"Vetor de Amostras: {vetor}")
print(f"Média Aritmética (x̄): {media:.4f}")
print(f"Variância Amostral (s²): {variancia:.4f}")
print(f"Desvio Padrão Amostral (s): {desvio_padrao:.4f}")
