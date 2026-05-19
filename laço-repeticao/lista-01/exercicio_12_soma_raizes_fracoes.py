# Exercício 12: Soma das Raízes Quadradas e Frações
# Objetivo: Calcular a soma das raízes quadradas das frações dos números de 1 até n.

# Passo 1: Leitura do número inteiro positivo n
n = input("Insira um número inteiro positivo: ")
n = int(n)

# Passo 2: Inicialização da soma acumuladora
soma = 0.0

# Passo 3: Laço de repetição de 1 até n para somar a raiz quadrada de 1/i
for i in range(1, n + 1):
    soma = soma + ((1.0 / i) ** 0.5)

# Passo 4: Exibição do resultado
print(f"Soma das raízes quadradas e frações: {soma}")
