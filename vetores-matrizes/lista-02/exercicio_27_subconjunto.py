# Exercício 27: Verificação de Subconjunto Matemático (A ⊆ B)
# Objetivo: Definir conjuntos A (tamanho N) e B (tamanho M), receber elementos positivos, e verificar com laços aninhados se A é subconjunto de B.

# Passo 1: Leitura de N e M com validação (> 0)
print("--- Verificador de Subconjuntos ---")
n_valido = False
n = 0
while not n_valido:
    n = input("Digite o tamanho N do Conjunto A: ")
    n = int(n)
    if n > 0:
        n_valido = True
    else:
        print("Erro: O tamanho N deve ser positivo.")

m_valido = False
m = 0
while not m_valido:
    m = input("Digite o tamanho M do Conjunto B: ")
    m = int(m)
    if m > 0:
        m_valido = True
    else:
        print("Erro: O tamanho M deve ser positivo.")

# Passo 2: Inicialização dos vetores A e B
vetor_a = [0] * n
vetor_b = [0] * m

# Passo 3: Preenchimento de A e B com inteiros positivos
print(f"\n--- Cadastro do Conjunto A (tamanho {n}) ---")
for i in range(n):
    valido = False
    while not valido:
        val = input(f"  A[{i}]: ")
        val = int(val)
        if val > 0:
            vetor_a[i] = val
            valido = True
        else:
            print("    Erro: Insira um número inteiro positivo.")

print(f"\n--- Cadastro do Conjunto B (tamanho {m}) ---")
for i in range(m):
    valido = False
    while not valido:
        val = input(f"  B[{i}]: ")
        val = int(val)
        if val > 0:
            vetor_b[i] = val
            valido = True
        else:
            print("    Erro: Insira um número inteiro positivo.")

# Passo 4: Verificação se A é subconjunto de B (todos os elementos de A devem estar em B)
eh_subconjunto = True
elementos_faltantes = []

for i in range(n):
    elem_a = vetor_a[i]
    
    # Procura elem_a no vetor B
    encontrado = False
    for j in range(m):
        if vetor_b[j] == elem_a:
            encontrado = True
            break
            
    if not encontrado:
        eh_subconjunto = False
        elementos_faltantes.append(elem_a)

# Passo 5: Exibição dos resultados
print("\n--- ANÁLISE DE RELAÇÃO DE CONJUNTOS ---")
print(f"Conjunto A: {vetor_a}")
print(f"Conjunto B: {vetor_b}")

if eh_subconjunto:
    print("\nResultado: O Conjunto A É SUBCONJUNTO do Conjunto B! (A ⊆ B)")
else:
    print("\nResultado: O Conjunto A NÃO É SUBCONJUNTO do Conjunto B! (A ⊈ B)")
    print(f"  Razão: O(s) elemento(s) {elementos_faltantes} de A não pertence(m) ao conjunto B.")
