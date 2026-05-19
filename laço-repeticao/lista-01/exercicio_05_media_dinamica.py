# Exercício 5: Média Aritmética Dinâmica
# Objetivo: Calcular a média de n números que serão lidos do teclado (sem guardá-los em lista).

# Passo 1: Leitura da quantidade total de números n
n = input("Quantos números deseja digitar? ")
n = int(n)

# Passo 2: Inicialização da soma acumuladora
soma_total = 0.0

# Passo 3: Laço de repetição para ler e somar os n números
for i in range(1, n + 1):
    valor_atual = input(f"Digite o {i}º número: ")
    valor_atual = float(valor_atual)
    soma_total = soma_total + valor_atual

# Passo 4: Cálculo da média
media = soma_total / n

# Passo 5: Exibição do resultado
print(f"A média aritmética dos {n} números é: {media:.2f}")
