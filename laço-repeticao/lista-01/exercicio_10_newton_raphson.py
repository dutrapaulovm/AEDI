# Exercício 10: Raiz Quadrada via Newton-Raphson
# Objetivo: Calcular a raiz quadrada aproximada de um número S utilizando o Método de Newton-Raphson, sem usar sqrt().

# Passo 1: Leitura do número S
S = input("Digite o número para calcular a raiz quadrada (S): ")
S = float(S)

# Passo 2: Leitura do número de iterações n
n = input("Digite o número de iterações do método (n): ")
n = int(n)

# Passo 3: Inicialização da estimativa x com S / 2
x = S / 2.0

# Passo 4: Laço de repetição para atualizar a estimativa n vezes
for i in range(1, n + 1):
    x = 0.5 * (x + (S / x))

# Passo 5: Exibição do resultado
print(f"A raiz quadrada aproximada de {S} após {n} iterações é: {x:.10f}")
