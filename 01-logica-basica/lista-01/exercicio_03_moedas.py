# Exercício 3: Conversor de Moedas
# Objetivo: Informar quantos dólares podem ser comprados com o saldo em reais.

# Parâmetro de cotação atual (conforme enunciado)
COTACAO_DOLAR = 5.00

# Passo 1: Leitura do valor em reais na carteira
reais = input("Quantos reais você tem na carteira? R$ ")
reais = float(reais)

# Passo 2: Cálculo da quantidade de dólares
dolares = reais / COTACAO_DOLAR

# Passo 3: Exibição do valor em dólares
print(f"Com R${reais:.2f}, você pode comprar US${dolares:.2f}.")
