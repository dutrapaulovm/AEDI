# Exercício 18: Compactação de Vetores Esparsos (Compressão Baseada em Zeros)
# Objetivo: Receber 10 inteiros em um vetor, contar os zeros e, se atingir pelo menos 60% (6 ou mais zeros), gerar dois vetores de compactação (Valores e Índices originais).

# Passo 1: Inicialização do vetor original de 10 posições
vetor = [0] * 10

# Passo 2: Leitura dos 10 valores inteiros
print("--- Cadastro de 10 Valores Inteiros (Vetores Esparsos) ---")
for i in range(10):
    val = input(f"Digite o {i+1}º número inteiro: ")
    val = int(val)
    vetor[i] = val

# Passo 3: Contar a quantidade de elementos que são zero
cont_zeros = 0
for i in range(10):
    if vetor[i] == 0:
        cont_zeros = cont_zeros + 1
        
print(f"\nEstatística do vetor:")
print(f"  Elementos iguais a zero: {cont_zeros} de 10 ({cont_zeros * 10}% de esparsidade)")

# Passo 4: Verificar se a compactação é eficiente (mínimo 6 zeros / 60%)
if cont_zeros >= 6:
    print("Resultado: Compactação EFICIENTE!")
    
    # Número de elementos não nulos
    n_nulos = 10 - cont_zeros
    
    # Passo 5: Gerar dois novos vetores compactados (Valores e Índices originais)
    valores_compactados = [0] * n_nulos
    indices_originais = [0] * n_nulos
    
    idx_compactado = 0
    for i in range(10):
        if vetor[i] != 0:
            valores_compactados[idx_compactado] = vetor[i]
            indices_originais[idx_compactado] = i
            idx_compactado = idx_compactado + 1
            
    print("\n--- DADOS COMPACTADOS ---")
    print(f"Vetor Original: {vetor}")
    print(f"Vetor de Valores Não Nulos: {valores_compactados}")
    print(f"Vetor de Índices Originais:  {indices_originais}")
else:
    print("Resultado: Compactação INEFICIENTE! A quantidade de zeros é inferior a 60%. Dados mantidos em formato original.")
    print(f"Vetor Original: {vetor}")
