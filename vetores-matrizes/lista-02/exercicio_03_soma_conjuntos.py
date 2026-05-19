# Exercício 3: Soma de Dois Conjuntos Numéricos (Vetor Z = X + Y)
# Objetivo: Somar elementos de dois vetores X e Y de tamanho 5, validando valores no intervalo [1, 100] e acumulando a soma dos termos de Z.

# Passo 1: Inicialização dos vetores X, Y e Z
vetor_x = [0] * 5
vetor_y = [0] * 5
vetor_z = [0] * 5

# Passo 2: Leitura do Vetor X com validação [1, 100]
print("--- Cadastro do Vetor X (5 elementos) ---")
for i in range(5):
    valido = False
    while not valido:
        val = input(f"  Digite o {i+1}º valor para X (entre 1 e 100): ")
        val = int(val)
        if 1 <= val <= 100:
            vetor_x[i] = val
            valido = True
        else:
            print("    Erro: O valor deve estar no intervalo [1, 100].")

# Passo 3: Leitura do Vetor Y com validação [1, 100]
print("\n--- Cadastro do Vetor Y (5 elementos) ---")
for i in range(5):
    valido = False
    while not valido:
        val = input(f"  Digite o {i+1}º valor para Y (entre 1 e 100): ")
        val = int(val)
        if 1 <= val <= 100:
            vetor_y[i] = val
            valido = True
        else:
            print("    Erro: O valor deve estar no intervalo [1, 100].")

# Passo 4: Operação de soma Z[i] = X[i] + Y[i] e acumulação total em loop
soma_total_z = 0
for i in range(5):
    vetor_z[i] = vetor_x[i] + vetor_y[i]
    soma_total_z = soma_total_z + vetor_z[i]

# Passo 5: Exibição dos resultados
print("\n--- RESULTADO DAS OPERAÇÕES ---")
print(f"Vetor X: {vetor_x}")
print(f"Vetor Y: {vetor_y}")
print(f"Vetor Z (Soma X + Y): {vetor_z}")
print(f"Soma acumulada de todos os elementos de Z: {soma_total_z}")
