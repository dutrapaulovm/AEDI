# Exercício 14: Análise de Sinais Combinados
# Objetivo: Checar comportamentos parecidos entre A e B.

# Passo 1: Casting e recepção
a = input("A: ")
a = int(a)
b = input("B: ")
b = int(b)

# Passo 2: Condições e avaliações lógicas puras
if a == 0 or b == 0:
    print("Existe um zero, logo os sinais são neutros")
else:
    if a > 0 and b > 0:
        print("Ambos positivos")
    elif a < 0 and b < 0:
        print("Ambos negativos")
    else:
        print("Sinais diferentes")
