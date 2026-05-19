# Exercício 4: Cálculo de Potência via Produtório
# Objetivo: Calcular x elevado a n (onde n é inteiro e positivo) sem usar operadores/funções prontas de potência.

# Passo 1: Leitura da base x
x = input("Digite o valor da base (x): ")
x = float(x)

# Passo 2: Leitura do expoente n
n = input("Digite o valor do expoente inteiro positivo (n): ")
n = int(n)

# Passo 3: Inicialização do acumulador do produtório
potencia = 1.0

# Passo 4: Laço de repetição para multiplicar a base x, n vezes
for i in range(n):
    potencia = potencia * x

# Passo 5: Exibição do resultado
print(f"O resultado de {x} elevado a {n} é: {potencia}")
