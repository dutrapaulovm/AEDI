# Exercício 21: Desconto VIP x Comum
# Objetivo: Chechar flag + valor para rateio

# Passo 1: Entrada
tipo = input("Tipo (VIP/COMUM): ")
tipo = tipo.upper()
compra = input("Valor compra: ")
compra = float(compra)

# Passo 2: Avaliação de desconto
if tipo == "VIP" and compra > 100:
    print("Desconto de 20%")
elif tipo == "COMUM" and compra > 100:
    print("Desconto de 10%")
else:
    print("Sem desconto")
