# Exercício 29: Geração do Triângulo de Pascal
# Objetivo: Receber quantidade N de linhas (de 1 a 10) e construir de forma procedural o Triângulo de Pascal usando matrizes/vetores aninhados.

# Passo 1: Leitura do número de linhas N com validação [1, 10]
print("--- Gerador do Triângulo de Pascal ---")
n_valido = False
n = 0
while not n_valido:
    n = input("Digite o número de linhas N a gerar (1 a 10): ")
    n = int(n)
    if 1 <= n <= 10:
        n_valido = True
    else:
        print("Erro: O número de linhas deve estar contido no intervalo [1, 10].")

# Passo 2: Inicialização do triângulo (lista de listas/vetores para representação da matriz triangular)
triangulo = []

# Passo 3: Geração das linhas do Triângulo de Pascal em laço aninhado
# C(linha, coluna) = C(linha-1, coluna-1) + C(linha-1, coluna)
for i in range(n):
    # Cria uma nova linha cheia de zeros
    linha = [0] * (i + 1)
    
    # As extremidades de cada linha são sempre 1
    linha[0] = 1
    linha[i] = 1
    
    # Preenche os termos internos da linha
    for j in range(1, i):
        linha[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
        
    triangulo.append(linha)

# Passo 4: Exibição estruturada e centralizada
print("\n--- TRIÂNGULO DE PASCAL ---")
for i in range(n):
    # Lógica de espaçamento manual para centralização
    espacamento = "   " * (n - i - 1)
    
    # Constrói a linha com termos formatados
    linha_txt = ""
    for termo in triangulo[i]:
        linha_txt = linha_txt + f"{termo:5d} "
        
    print(espacamento + linha_txt)
