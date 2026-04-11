# Exercício 7: Regra dos 72
# Objetivo: Calcular tempo para dobrar investimento.

i = input("Taxa de juros anual (em %, ex: 5 para 5%): ")
i = float(i)

t = 72 / i

print(f"Tempo estimado para dobrar o valor: {t:.2f} anos")
