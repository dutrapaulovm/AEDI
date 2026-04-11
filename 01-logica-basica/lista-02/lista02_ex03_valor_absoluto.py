# Exercício 3: Valor Absoluto
# Objetivo: Calcular o módulo absoluto de um número sem "abs".

x = input("Digite um número: ")
x = float(x)

if x >= 0:
    absoluto = x
else:
    absoluto = -x

print(f"O valor absoluto é: {absoluto}")
