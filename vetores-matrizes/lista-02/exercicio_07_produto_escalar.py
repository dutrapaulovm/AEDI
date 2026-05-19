# Exercício 7: Cálculo de Produto Escalar de Subvetores
# Objetivo: Receber 10 números reais em um vetor e calcular o produto escalar entre a primeira metade (primeiros 5) e a segunda metade (últimos 5).

# Passo 1: Inicialização do vetor de 10 posições
vetor = [0.0] * 10

# Passo 2: Leitura dos 10 valores reais
print("--- Cadastro de 10 Valores Reais ---")
for i in range(10):
    val = input(f"Digite o {i+1}º valor real do vetor: ")
    val = float(val)
    vetor[i] = val

# Passo 3: Cálculo do produto escalar entre a 1ª metade (0 a 4) e a 2ª metade (5 a 9)
# A formula é: Produto Escalar = sum_{i=0..4} (V[i] * V[i + 5])
produto_escalar = 0.0
for i in range(5):
    primeiro_termo = vetor[i]
    segundo_termo = vetor[i + 5]
    produto_escalar = produto_escalar + (primeiro_termo * segundo_termo)

# Passo 4: Exibição dos dados e do resultado
print("\n--- RESULTADOS DO PRODUTO ESCALAR ---")
print("Subvetor A (Primeiros 5):", [vetor[i] for i in range(5)])
print("Subvetor B (Últimos 5):  ", [vetor[i+5] for i in range(5)])
print(f"\nProduto Escalar Calculado: {produto_escalar:.4f}")
