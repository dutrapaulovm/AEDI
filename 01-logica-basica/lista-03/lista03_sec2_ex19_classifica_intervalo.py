# Exercício 19: Intervalos Extremos
# Objetivo: 3 faixas delimitadoras fixas

# Passo 1: Entrada
num = input("Número: ")
num = float(num)

# Passo 2: Verificadores
if num < 0 or num >= 100:
    print("Extremo")
elif num >= 10 and num <= 50:
    print("Dentro do intervalo (10-50)")
else:
    print("Fora do intervalo")
