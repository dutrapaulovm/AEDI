# Exercício 23: Armazenamento de Sequência de Fibonacci em Vetor
# Objetivo: Receber tamanho N (N >= 2), preencher um vetor com os primeiros N números de Fibonacci e exibir a sequência resultante.

# Passo 1: Leitura do tamanho N do vetor com validação (N >= 2)
print("--- Gerador de Fibonacci ---")
n_valido = False
n = 0
while not n_valido:
    n = input("Digite a quantidade de termos N de Fibonacci a gerar (N >= 2): ")
    n = int(n)
    if n >= 2:
        n_valido = True
    else:
        print("Erro: O tamanho do vetor deve ser de pelo menos 2 elementos.")

# Passo 2: Inicialização do vetor de tamanho N
fib = [0] * n

# Passo 3: Geração dos termos da sequência de Fibonacci
# F0 = 0, F1 = 1, Fn = Fn-1 + Fn-2
fib[0] = 0
fib[1] = 1

for i in range(2, n):
    fib[i] = fib[i - 1] + fib[i - 2]

# Passo 4: Exibição da sequência armazenada no vetor
print("\n--- SEQUÊNCIA DE FIBONACCI GERADA ---")
print(f"Quantidade de Termos (N): {n}")
print(f"Vetor Fibonacci: {fib}")

# Exibe o termo a termo
for i in range(n):
    print(f"  Termo F({i:2d}): {fib[i]}")
