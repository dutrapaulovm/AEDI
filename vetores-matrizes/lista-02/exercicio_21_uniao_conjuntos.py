# Exercício 21: União de Dois Conjuntos Numéricos (Vetor Z = X ∪ Y)
# Objetivo: Definir tamanho N, receber os vetores X e Y, e construir o vetor Z representando a União Matemática (X ∪ Y) sem duplicatas.

# Passo 1: Leitura de N com validação (> 0)
print("--- União de Conjuntos Matemáticos ---")
n_valido = False
n = 0
while not n_valido:
    n = input("Digite o tamanho N dos conjuntos: ")
    n = int(n)
    if n > 0:
        n_valido = True
    else:
        print("Erro: O tamanho deve ser maior que zero.")

# Passo 2: Inicialização dos vetores
vetor_x = [0] * n
vetor_y = [0] * n

# Passo 3: Cadastro do Vetor X
print(f"\n--- Cadastro de X (N = {n}) ---")
for i in range(n):
    valido = False
    while not valido:
        val = input(f"  X[{i}]: ")
        val = int(val)
        if val > 0:
            vetor_x[i] = val
            valido = True
        else:
            print("    Erro: Digite um número positivo.")

# Passo 4: Cadastro do Vetor Y
print(f"\n--- Cadastro de Y (N = {n}) ---")
for i in range(n):
    valido = False
    while not valido:
        val = input(f"  Y[{i}]: ")
        val = int(val)
        if val > 0:
            vetor_y[i] = val
            valido = True
        else:
            print("    Erro: Digite um número positivo.")

# Passo 5: Geração da União (X ∪ Y) em Z
# O vetor Z de união conterá no máximo 2*N elementos
uniao_temp = [0] * (2 * n)
cont_uniao = 0

# Adiciona todos os elementos de X à união (prevenindo duplicatas internas de X)
for i in range(n):
    elem = vetor_x[i]
    
    # Verifica se já está na união
    ja_na_uniao = False
    for j in range(cont_uniao):
        if uniao_temp[j] == elem:
            ja_na_uniao = True
            break
            
    if not ja_na_uniao:
        uniao_temp[cont_uniao] = elem
        cont_uniao = cont_uniao + 1

# Adiciona elementos de Y que não estão na união
for i in range(n):
    elem = vetor_y[i]
    
    # Verifica se já está na união
    ja_na_uniao = False
    for j in range(cont_uniao):
        if uniao_temp[j] == elem:
            ja_na_uniao = True
            break
            
    if not ja_na_uniao:
        uniao_temp[cont_uniao] = elem
        cont_uniao = cont_uniao + 1

# Recorta a lista temporária para o tamanho lógico exato do conjunto união
vetor_z = [0] * cont_uniao
for i in range(cont_uniao):
    vetor_z[i] = uniao_temp[i]

# Passo 6: Exibição dos resultados
print("\n--- RESULTADO DA UNIÃO ---")
print(f"Conjunto X: {vetor_x}")
print(f"Conjunto Y: {vetor_y}")
print(f"Conjunto Z (X ∪ Y) - Qtd: {cont_uniao}: {vetor_z}")
