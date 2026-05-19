# Exercício 8: Soma dos Erros Absolutos (SEA)
# Objetivo: Ler n valores reais e calcular a soma dos seus valores absolutos (módulo).

# Passo 1: Leitura da quantidade total de valores n
n = input("Digite a quantidade de erros a serem lidos (n): ")
n = int(n)

# Passo 2: Inicialização da soma acumuladora dos erros absolutos
sea = 0.0

# Passo 3: Laço de repetição para ler cada um dos n valores e acumular seu módulo
for i in range(1, n + 1):
    x = input(f"Digite o {i}º erro: ")
    x = float(x)
    
    # Obtém o valor absoluto (módulo) do valor digitado
    modulo_x = abs(x)
    
    # Acumula o valor absoluto
    sea = sea + modulo_x

# Passo 4: Exibição do resultado final
print(f"A Soma dos Erros Absolutos (SEA) é: {sea:.4f}")
