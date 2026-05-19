# Exercício 14: Separação de Números Primos e Compostos
# Objetivo: Receber N números em um vetor original, verificar a primalidade de cada um com laço aninhado, e distribuí-los em dois vetores (Primos e Compostos) com redimensionamento lógico.

# Passo 1: Leitura de N com validação (> 0)
print("--- Divisor de Primos e Compostos ---")
n_valido = False
n = 0
while not n_valido:
    n = input("Digite o tamanho N do vetor: ")
    n = int(n)
    if n > 0:
        n_valido = True
    else:
        print("Erro: O tamanho N deve ser positivo.")

# Passo 2: Inicialização dos vetores
vetor_original = [0] * n
# Como não sabemos quantos primos/compostos haverá, alocamos o tamanho máximo N e usamos contadores lógicos
primos = [0] * n
compostos = [0] * n

cont_primos = 0
cont_compostos = 0
cadastrado = False

# Passo 3: Cadastro com validação de números (> 1)
print(f"\n--- Cadastro de {n} Inteiros Maiores que 1 ---")
for i in range(n):
    valido = False
    while not valido:
        val = input(f"Digite o {i+1}º número: ")
        val = int(val)
        if val > 1:
            vetor_original[i] = val
            valido = True
        else:
            print("  Erro: O número deve ser estritamente maior que 1. Digite novamente.")
cadastrado = True

# Passo 4: Processamento de Primos e Compostos em laço aninhado
# O laço externo percorre o vetor original
for i in range(n):
    num = vetor_original[i]
    
    # O laço interno verifica a primalidade de 'num'
    eh_primo = True
    for divisor in range(2, num):
        if num % divisor == 0:
            eh_primo = False
            break  # Encontrou divisor, então não é primo
            
    # Passo 5: Distribuição nos vetores correspondentes com redimensionamento lógico
    if eh_primo:
        primos[cont_primos] = num
        cont_primos = cont_primos + 1
    else:
        compostos[cont_compostos] = num
        cont_compostos = cont_compostos + 1

# Passo 6: Exibição dos resultados (cortando os vetores no tamanho lógico)
# Criamos fatias manuais usando loops simples para não usar métodos avançados
vetor_primos_final = [0] * cont_primos
for i in range(cont_primos):
    vetor_primos_final[i] = primos[i]
    
vetor_compostos_final = [0] * cont_compostos
for i in range(cont_compostos):
    vetor_compostos_final[i] = compostos[i]

print("\n--- RESULTADO DA ANÁLISE ---")
print(f"Vetor Original: {vetor_original}")
print(f"Números Primos  (Qtd: {cont_primos}): {vetor_primos_final}")
print(f"Números Compostos (Qtd: {cont_compostos}): {vetor_compostos_final}")
