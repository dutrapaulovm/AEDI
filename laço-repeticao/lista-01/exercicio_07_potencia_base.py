# Exercício 7: Potência de Base e Expoente
# Objetivo: Calcular a potência de um número base b elevado a um expoente inteiro positivo n.

# Passo 1: Leitura da base b
b = input("Digite o valor da base (b): ")
b = float(b)

# Passo 2: Leitura do expoente n
n = input("Digite o valor do expoente inteiro positivo (n): ")
n = int(n)

# Passo 3: Inicialização da variável acumuladora
potencia = 1.0

# Passo 4: Laço de repetição de 1 até n para multiplicar a base
for i in range(1, n + 1):
    potencia = potencia * b

# Passo 5: Exibição do resultado
print(f"O resultado de {b} elevado a {n} é: {potencia}")
