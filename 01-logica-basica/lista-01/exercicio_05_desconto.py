# Exercício 5: Cálculo de Desconto
# Objetivo: Calcular o novo preço de um produto com 5% de desconto.

# Passo 1: Leitura do preço original
preco_original = input("Digite o preço do produto: R$ ")
preco_original = float(preco_original)

# Passo 2: Cálculo do valor do desconto (5% = 0.05)
valor_desconto = preco_original * 0.05

# Passo 3: Cálculo do preço final com o desconto aplicado
preco_final = preco_original - valor_desconto

# Passo 4: Exibição detalhada do processo
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Valor descontado (5%): R$ {valor_desconto:.2f}")
print(f"Preço final a pagar: R$ {preco_final:.2f}")
