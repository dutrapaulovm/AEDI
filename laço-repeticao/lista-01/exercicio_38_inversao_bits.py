# Exercício 38: Inversão de Bits (Complemento de Um)
# (Seção 3, Exercício 3 da Lista)
# Objetivo: Receber um número inteiro, aplicar o operador bitwise NOT (inversão de bits) e exibir a saída.

# Passo 1: Leitura do número inteiro x
x = input("Digite um número inteiro (x): ")
x = int(x)

# Passo 2: Execução da inversão de bits (operador bitwise NOT: ~)
resultado = ~x

# Passo 3: Exibição dos resultados
print(f"Número de entrada (x): {x}")
print(f"Representação binária de x: {bin(x)}")
print(f"Resultado da inversão (~x): {resultado}")
print(f"Representação binária do resultado: {bin(resultado)}")
print("\nNota explicativa: Em computação, a inversão de bits altera todos os bits do número.")
print("Como os números com sinal usam complemento de dois, a inversão (~x) equivale a: -(x + 1).")
