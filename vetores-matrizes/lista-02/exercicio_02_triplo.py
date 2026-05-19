# Exercício 2: Multiplicação Condicional de Vetor (Vetor B = 3 * A)
# Objetivo: Ler 5 valores para o Vetor A, gerar o Vetor B aplicando a condição: se A[i] > 10 e múltiplo de 3, B[i] = 3 * A[i], senão 0.

# Passo 1: Inicialização dos vetores para 5 elementos
vetor_a = [0.0] * 5
vetor_b = [0.0] * 5

# Passo 2: Leitura dos 5 valores reais de A com validação (não aceita zero)
print("--- Cadastro de 5 Valores Numéricos Reais (não nulos) ---")
for i in range(5):
    valido = False
    while not valido:
        val = input(f"Digite o {i+1}º valor real para o Vetor A: ")
        val = float(val)
        if val != 0.0:
            vetor_a[i] = val
            valido = True
        else:
            print("Erro: O valor não pode ser zero. Digite novamente.")

# Passo 3: Cálculo do vetor B aplicando a definição matemática
for i in range(5):
    val_a = vetor_a[i]
    # Condição: maior que 10 E múltiplo de 3 (resto da divisão por 3.0 é zero)
    if val_a > 10.0 and (val_a % 3.0 == 0.0):
        vetor_b[i] = 3.0 * val_a
    else:
        vetor_b[i] = 0.0

# Passo 4: Exibição dos resultados
print("\n--- RESULTADO DA CONVERSÃO ---")
print(f"Vetor A: {vetor_a}")
print(f"Vetor B: {vetor_b}")
