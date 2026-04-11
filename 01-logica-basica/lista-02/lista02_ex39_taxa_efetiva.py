# Exercício 39: Taxa Efetiva
# Objetivo: Juros compostos.

r = input("Taxa nominal (decimal): ")
r = float(r)
n = input("Vezes de composição no ano: ")
n = float(n)

ieff = (1 + r/n)**n - 1

print(f"Taxa efetiva: {ieff:.4f}")
