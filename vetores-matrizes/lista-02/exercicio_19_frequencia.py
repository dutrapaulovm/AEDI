# Exercício 19: Frequência de Ocorrência de Elementos em Vetor
# Objetivo: Cadastrar 8 valores inteiros em um vetor, calcular a frequência (contagem de ocorrência) de cada um com laço aninhado e prevenir duplicidade na exibição.

# Passo 1: Inicialização do vetor de 8 posições
vetor = [0] * 8
# Vetor auxiliar para rastrear se o elemento na posição i já teve sua frequência exibida
ja_processado = [False] * 8

# Passo 2: Leitura dos 8 inteiros
print("--- Cadastro de 8 Elementos Inteiros ---")
for i in range(8):
    val = input(f"Digite o {i+1}º valor inteiro: ")
    val = int(val)
    vetor[i] = val

# Passo 3: Laço aninhado para contagem e verificação
print("\n--- ANÁLISE DE FREQUÊNCIA DOS ELEMENTOS ---")
print(f"Vetor Cadastrado: {vetor}\n")

for i in range(8):
    # Se o elemento nesta posição i já foi contabilizado anteriormente, ignora
    if not ja_processado[i]:
        valor_atual = vetor[i]
        frequencia = 0
        
        # Laço interno para contar quantas vezes o valor_atual aparece no vetor inteiro
        for j in range(8):
            if vetor[j] == valor_atual:
                frequencia = frequencia + 1
                # Marca todos os índices onde o mesmo valor foi encontrado como já processados
                ja_processado[j] = True
                
        # Exibe a frequência do elemento
        percentual = (frequencia / 8.0) * 100.0
        print(f"  Elemento '{valor_atual}' : Ocorre {frequencia} vez(es) | Percentual: {percentual:.1f}%")
