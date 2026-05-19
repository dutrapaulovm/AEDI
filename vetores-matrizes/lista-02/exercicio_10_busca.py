# Exercício 10: Busca Sequencial de Elemento em Vetor
# Objetivo: Cadastrar 10 valores em um vetor e realizar a busca de um valor X, exibindo a primeira posição onde foi localizado ou informando sua ausência.

# Passo 1: Inicialização do vetor de 10 posições
vetor = [0.0] * 10

# Passo 2: Leitura dos 10 valores reais
print("--- Cadastro de 10 Valores Numéricos ---")
for i in range(10):
    val = input(f"Digite o {i+1}º valor real do vetor: ")
    val = float(val)
    vetor[i] = val

# Passo 3: Solicitar o valor X de busca
print("\n--- Pesquisa de Elemento ---")
busca_x = input("Digite o valor X que deseja buscar no vetor: ")
busca_x = float(busca_x)

# Passo 4: Realizar a busca sequencial em loop
posicao_encontrada = -1
for i in range(10):
    if vetor[i] == busca_x:
        posicao_encontrada = i
        break  # Interrompe no primeiro acerto

# Passo 5: Exibição do resultado
print("\n--- RESULTADO DA BUSCA ---")
print(f"Vetor de Dados: {vetor}")
if posicao_encontrada != -1:
    print(f"Valor X ({busca_x}) encontrado na primeira ocorrência na posição: {posicao_encontrada}")
else:
    print(f"Valor X ({busca_x}) não existe no conjunto de elementos do vetor.")
