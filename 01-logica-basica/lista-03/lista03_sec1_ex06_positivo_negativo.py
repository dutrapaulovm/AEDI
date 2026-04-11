# Exercício 6: Positivo, Negativo ou Zero
# Objetivo: Classificar o sinal de um número

# Passo 1: Leitura e conversão
num = input("Digite um número: ")
num = float(num)

# Passo 2: Múltiplas condições
if num > 0:
    # Passo 3a: Estritamente positivo
    print("O número é POSITIVO")
elif num < 0:
    # Passo 3b: Estritamente negativo
    print("O número é NEGATIVO")
else:
    # Passo 3c: Caso neutro
    print("O número é ZERO")
