# Exercício 4: Detecção de Elementos Duplicados em Vetor
# Objetivo: Ler 5 números inteiros não negativos em um vetor, e verificar usando laços aninhados se existe ao menos um par de elementos iguais.

# Passo 1: Inicialização do vetor de 5 elementos
vetor = [0] * 5

# Passo 2: Leitura dos 5 elementos (validação: evitar negativos)
print("--- Cadastro de 5 Inteiros Não Negativos ---")
for i in range(5):
    valido = False
    while not valido:
        val = input(f"Digite o {i+1}º número (>= 0): ")
        val = int(val)
        if val >= 0:
            vetor[i] = val
            valido = True
        else:
            print("Erro: O número não pode ser negativo. Tente novamente.")

# Passo 3: Laço aninhado para procurar duplicatas (índices i != j com V[i] == V[j])
tem_duplicata = False
indice_dupl1 = -1
indice_dupl2 = -1

for i in range(5):
    for j in range(i + 1, 5):
        if vetor[i] == vetor[j]:
            tem_duplicata = True
            indice_dupl1 = i
            indice_dupl2 = j
            break
    if tem_duplicata:
        break

# Passo 4: Exibição do resultado
print("\n--- ANÁLISE DE CONJUNTO ---")
print(f"Conjunto de Entrada: {vetor}")
if tem_duplicata:
    print(f"Resultado: Existem elementos duplicados no conjunto! (Exemplo: Valor {vetor[indice_dupl1]} nas posições {indice_dupl1} e {indice_dupl2}).")
else:
    print("Resultado: Não existem elementos duplicados. Todos os elementos são distintos.")
