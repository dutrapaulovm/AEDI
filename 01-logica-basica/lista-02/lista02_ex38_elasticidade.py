# Exercício 38: Elasticidade
# Objetivo: Elasticidade preço da demanda.

p0 = input("Preço inicial: ")
p0 = float(p0)
q0 = input("Quantidade inicial: ")
q0 = float(q0)
p1 = input("Novo preço: ")
p1 = float(p1)
q1 = input("Nova quantidade: ")
q1 = float(q1)

var_q = ((q1 - q0) / q0) * 100
var_p = ((p1 - p0) / p0) * 100

elasticidade = var_q / var_p

print(f"Elasticidade: {elasticidade:.2f}")
