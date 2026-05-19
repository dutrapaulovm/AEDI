# Exercício 25: Análise de Progressão Aritmética (Verificação de Vetor)
# Objetivo: Cadastrar 5 valores reais em um vetor e verificar se os termos formam uma PA, identificando a razão se aplicável.

# Passo 1: Inicialização do vetor de 5 elementos
vetor = [0.0] * 5

# Passo 2: Leitura dos 5 elementos reais
print("--- Analisador de Progressão Aritmética (PA) ---")
for i in range(5):
    val = input(f"Digite o {i+1}º termo real: ")
    val = float(val)
    vetor[i] = val

# Passo 3: Verificação de PA
# Uma sequência é PA se a diferença entre termos consecutivos for constante: V[i+1] - V[i] = Razão
eh_pa = True
razao = vetor[1] - vetor[0]

for i in range(1, 4):
    diferenca_atual = vetor[i + 1] - vetor[i]
    # Usamos tolerância a pequenas imprecisões de ponto flutuante
    if abs(diferenca_atual - razao) > 0.00001:
        eh_pa = False
        break

# Passo 4: Exibição dos resultados
print("\n--- RESULTADO DA ANÁLISE ---")
print(f"Vetor Informado: {vetor}")
if eh_pa:
    print("Resultado: A sequência informada REPRESENTA uma Progressão Aritmética (PA)!")
    print(f"Razão (r): {razao:.4f}")
else:
    print("Resultado: A sequência informada NÃO representa uma Progressão Aritmética (PA). A razão não é constante entre os termos.")
