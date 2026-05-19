# Exercício 24: Crivo de Eratóstenes para Números Primos
# Objetivo: Localizar todos os números primos até N (entre 2 e 100) utilizando a técnica clássica de Crivo de Eratóstenes com vetor de status booleanos.

# Passo 1: Leitura do limite N com validação [2, 100]
print("--- Algoritmo Crivo de Eratóstenes ---")
n_valido = False
n = 0
while not n_valido:
    n = input("Digite o limite superior N para a busca de primos (2 a 100): ")
    n = int(n)
    if 2 <= n <= 100:
        n_valido = True
    else:
        print("Erro: O limite N deve estar no intervalo [2, 100].")

# Passo 2: Inicialização do vetor booleano de tamanho N + 1
# Índice representa o número. Todos iniciam como True (1), exceto 0 e 1 que não são primos
crivo = [1] * (n + 1)
crivo[0] = 0
crivo[1] = 0

# Passo 3: Laço principal do algoritmo Crivo de Eratóstenes
# Percorre de 2 até o limite (podendo otimizar até a raiz de N)
for i in range(2, n + 1):
    if crivo[i] == 1:
        # Se 'i' é primo, marca todos os seus múltiplos a partir de i*2 (ou i*i) como não primos (0)
        multiplo = i * 2
        while multiplo <= n:
            crivo[multiplo] = 0
            multiplo = multiplo + i

# Passo 4: Extrair e armazenar os números primos localizados
primos = []
for i in range(2, n + 1):
    if crivo[i] == 1:
        primos.append(i)

# Passo 5: Exibição dos resultados
print("\n--- RESULTADO DO CRIVO ---")
print(f"Limite N: {n}")
print(f"Vetor de Booleanos (Crivo): {crivo}")
print(f"\nNúmeros primos identificados até {n}: {primos}")
print(f"Total de números primos encontrados: {len(primos)}")
