# Exercício 1: Classificação Par/Ímpar de Vetor
# Objetivo: Receber 10 inteiros positivos, classificá-los em um segundo vetor de strings, e exibir ambos lado a lado.

# Passo 1: Inicialização dos vetores para 10 elementos
vetor_a = [0] * 10
classificacoes = [""] * 10

# Passo 2: Leitura dos 10 inteiros com validação (deve ser positivo > 0)
print("--- Cadastro de 10 Números Inteiros Positivos ---")
for i in range(10):
    valido = False
    while not valido:
        num = input(f"Digite o {i+1}º número inteiro positivo: ")
        num = int(num)
        if num > 0:
            vetor_a[i] = num
            valido = True
        else:
            print("Erro: O número deve ser positivo e maior que zero. Tente novamente.")

# Passo 3: Classificação dos elementos no vetor de strings
for i in range(10):
    if vetor_a[i] % 2 == 0:
        classificacoes[i] = "Par"
    else:
        classificacoes[i] = "Ímpar"

# Passo 4: Exibição dos dois vetores lado a lado
print("\n--- RESULTADO DA CLASSIFICAÇÃO ---")
print("Índice | Vetor A | Classificação")
print("-------|---------|---------------")
for i in range(10):
    print(f"   {i}   |   {vetor_a[i]:3d}   | {classificacoes[i]}")
