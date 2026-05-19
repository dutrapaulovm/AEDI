# Exercício 9: Verificação de Ordenação Crescente de Vetor
# Objetivo: Receber 10 números inteiros em um vetor e verificar se o vetor está em ordem crescente (V[i] <= V[i+1]).

# Passo 1: Inicialização do vetor de 10 posições
vetor = [0] * 10

# Passo 2: Leitura dos 10 inteiros
print("--- Cadastro de 10 Números Inteiros ---")
for i in range(10):
    val = input(f"Digite o {i+1}º número inteiro: ")
    val = int(val)
    vetor[i] = val

# Passo 3: Verificação de ordenação crescente (se V[i] <= V[i+1] para todo i de 0 a 8)
esta_ordenado = True
for i in range(9):
    if vetor[i] > vetor[i + 1]:
        esta_ordenado = False
        break

# Passo 4: Exibição dos resultados
print("\n--- ANÁLISE DE ORDENAÇÃO ---")
print(f"Vetor: {vetor}")
if esta_ordenado:
    print("Resultado: Ordenado")
else:
    print("Resultado: Não Ordenado")
