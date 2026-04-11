# Exercício 1: Soma maior que 10
# Objetivo: Calcular soma e exibir apenas se for maior que 10

# Passo 1: Leitura das entradas
a = input("Digite o valor de a: ")
a = int(a)
b = input("Digite o valor de b: ")
b = int(b)

# Passo 2: Cálculo da soma
soma = a + b

# Passo 3: Verificação condicional e saída
if soma > 10:
    print(f"O resultado da soma é: {soma}")
