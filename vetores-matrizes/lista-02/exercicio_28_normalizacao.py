# Exercício 28: Normalização Min-Max de Vetor de Dados
# Objetivo: Receber 8 valores reais positivos em um vetor, localizar o mínimo e máximo e aplicar a normalização Min-Max para redimensionar todos no intervalo [0, 1].

# Passo 1: Inicialização do vetor de 8 elementos
vetor = [0.0] * 8
vetor_normalizado = [0.0] * 8

# Passo 2: Leitura com validação (> 0)
print("--- Normalizador de Dados Min-Max (Intervalo [0, 1]) ---")
for i in range(8):
    valido = False
    while not valido:
        val = input(f"Digite o {i+1}º valor real positivo: ")
        val = float(val)
        if val > 0.0:
            vetor[i] = val
            valido = True
        else:
            print("Erro: O valor deve ser positivo e maior que zero.")

# Passo 3: Localizar o valor mínimo e máximo usando loops simples
valor_minimo = vetor[0]
valor_maximo = vetor[0]

for i in range(1, 8):
    if vetor[i] < valor_minimo:
        valor_minimo = vetor[i]
    if vetor[i] > valor_maximo:
        valor_maximo = vetor[i]

# Passo 4: Aplicar a fórmula de normalização Min-Max
# x_norm = (x - x_min) / (x_max - x_min)
intervalo = valor_maximo - valor_minimo

if intervalo == 0.0:
    # Evita divisão por zero se todos os elementos forem iguais
    for i in range(8):
        vetor_normalizado[i] = 0.0
else:
    for i in range(8):
        vetor_normalizado[i] = (vetor[i] - valor_minimo) / intervalo

# Passo 5: Exibição dos resultados
print("\n--- RESULTADO DA NORMALIZAÇÃO ---")
print(f"Valor Mínimo Identificado: {valor_minimo}")
print(f"Valor Máximo Identificado: {valor_maximo}")
print(f"Vetor Original:            {vetor}")
print(f"Vetor Normalizado [0, 1]:  {vetor_normalizado}")
