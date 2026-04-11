# Exercício 30: Margem de Contribuição
# Objetivo: Calcular margem e lucro.

preco_venda = input("Preço de venda: ")
preco_venda = float(preco_venda)
custos = input("Custos variáveis por unidade: ")
custos = float(custos)
vendidas = input("Unidades vendidas: ")
vendidas = int(vendidas)

margem = preco_venda - custos
lucro = margem * vendidas

print(f"Margem de Contribuição: {margem:.2f}")
print(f"Lucro Total: {lucro:.2f}")
