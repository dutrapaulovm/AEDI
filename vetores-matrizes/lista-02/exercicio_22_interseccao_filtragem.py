# Exercício 22: Intersecção de Vetores com Filtragem (> 10)
# Objetivo: Definir tamanho N, receber vetores X e Y (apenas valores maiores que 10), e calcular o vetor Z contendo a intersecção (elementos em comum).

# Passo 1: Leitura de N com validação (> 0)
print("--- Intersecção de Vetores Filtrados ---")
n_valido = False
n = 0
while not n_valido:
    n = input("Digite o tamanho N dos vetores: ")
    n = int(n)
    if n > 0:
        n_valido = True
    else:
        print("Erro: O tamanho N deve ser positivo.")

# Passo 2: Inicialização dos vetores
vetor_x = [0] * n
vetor_y = [0] * n

# Passo 3: Cadastro do Vetor X com validação (> 10)
print(f"\n--- Cadastro de X (N = {n}) ---")
for i in range(n):
    valido = False
    while not valido:
        val = input(f"  X[{i}] (deve ser > 10): ")
        val = int(val)
        if val > 10:
            vetor_x[i] = val
            valido = True
        else:
            print("    Erro: O valor deve ser maior que 10.")

# Passo 4: Cadastro do Vetor Y com validação (> 10)
print(f"\n--- Cadastro de Y (N = {n}) ---")
for i in range(n):
    valido = False
    while not valido:
        val = input(f"  Y[{i}] (deve ser > 10): ")
        val = int(val)
        if val > 10:
            vetor_y[i] = val
            valido = True
        else:
            print("    Erro: O valor deve ser maior que 10.")

# Passo 5: Operação de intersecção com laços aninhados (sem duplicatas)
interseccao_temp = [0] * n
cont_inter = 0

for i in range(n):
    elem = vetor_x[i]
    
    # Verifica se elem existe em Y
    no_y = False
    for j in range(n):
        if vetor_y[j] == elem:
            no_y = True
            break
            
    if no_y:
        # Verifica se já está na nossa intersecção para evitar duplicidade
        ja_na_inter = False
        for j in range(cont_inter):
            if interseccao_temp[j] == elem:
                ja_na_inter = True
                break
                
        if not ja_na_inter:
            interseccao_temp[cont_inter] = elem
            cont_inter = cont_inter + 1

# Ajusta vetor para o tamanho exato dos elementos comuns
vetor_z = [0] * cont_inter
for i in range(cont_inter):
    vetor_z[i] = interseccao_temp[i]

# Passo 6: Exibição dos resultados
print("\n--- RESULTADO DA INTERSECÇÃO FILTRADA ---")
print(f"Vetor X: {vetor_x}")
print(f"Vetor Y: {vetor_y}")
print(f"Vetor Z (X ∩ Y) - Qtd: {cont_inter}: {vetor_z}")
