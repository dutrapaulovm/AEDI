# Exercício 8: Geração de Progressão Aritmética (PA) em Vetor
# Objetivo: Criar e armazenar em um vetor de 10 posições uma PA gerada a partir do primeiro termo (a1) e da razão (r) informada (razão não nula).

# Passo 1: Inicialização do vetor de 10 posições
pa = [0.0] * 10

# Passo 2: Leitura do primeiro termo e da razão com validação (razão != 0)
print("--- Gerador de Progressão Aritmética (PA) ---")
a1 = input("Digite o primeiro termo da PA (a1): ")
a1 = float(a1)

r_valida = False
r = 0.0
while not r_valida:
    r = input("Digite a razão da PA (r) (deve ser diferente de zero): ")
    r = float(r)
    if r != 0.0:
        r_valida = True
    else:
        print("Erro: A razão não pode ser zero. Digite novamente.")

# Passo 3: Geração dos termos e armazenamento no vetor (10 termos)
# Fórmula geral: an = a1 + (n - 1) * r
for n in range(1, 11):
    termo = a1 + (n - 1) * r
    pa[n - 1] = termo

# Passo 4: Exibição dos resultados
print("\n--- RESULTADO DA PA ---")
print(f"Primeiro Termo (a1): {a1}")
print(f"Razão (r):           {r}")
print(f"Vetor PA Gerado:     {pa}")
