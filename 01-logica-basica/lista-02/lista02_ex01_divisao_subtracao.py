# Exercício 1: Divisão com Subtração
# Objetivo: Realizar a divisão inteira de dois números usando apenas subtração.

A = input("Digite o valor de A (dividendo): ")
A = int(A)
B = input("Digite o valor de B (divisor): ")
B = int(B)

contador = 0
resto = A

while resto >= B:
    resto -= B
    contador += 1

print(f"Quociente da divisão: {contador}")
print(f"Resto da divisão: {resto}")
