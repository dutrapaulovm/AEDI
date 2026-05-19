# Exercício 26: Geração de Progressão Geométrica (PG) em Vetor
# Objetivo: Armazenar em um vetor de 10 posições uma PG a partir do primeiro termo (a1) e da razão (q) informada (ambos não nulos).

# Passo 1: Inicialização do vetor de 10 posições
pg = [0.0] * 10

# Passo 2: Leitura do primeiro termo com validação (!= 0)
print("--- Gerador de Progressão Geométrica (PG) ---")
a1_valido = False
a1 = 0.0
while not a1_valido:
    a1 = input("Digite o primeiro termo da PG (a1) (diferente de zero): ")
    a1 = float(a1)
    if a1 != 0.0:
        a1_valido = True
    else:
        print("Erro: O primeiro termo não pode ser zero.")

# Leitura da razão com validação (!= 0)
q_valida = False
q = 0.0
while not q_valida:
    q = input("Digite a razão da PG (q) (diferente de zero): ")
    q = float(q)
    if q != 0.0:
        q_valida = True
    else:
        print("Erro: A razão não pode ser zero.")

# Passo 3: Geração dos termos da PG e inserção no vetor
# Fórmula geral: an = a1 * q**(n-1)
for n in range(1, 11):
    termo = a1 * (q ** (n - 1))
    pg[n - 1] = termo

# Passo 4: Exibição dos resultados
print("\n--- RESULTADO DA PG ---")
print(f"Primeiro Termo (a1): {a1}")
print(f"Razão (q):           {q}")
print(f"Vetor PG Gerado:     {pg}")
