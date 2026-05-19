# Exercício 5: Análise de Inteiros Positivos e Negativos
# Objetivo: Armazenar 8 inteiros em um vetor, contar positivos e negativos, e calcular a média aritmética simples apenas dos números positivos.

# Passo 1: Inicialização do vetor de 8 elementos
vetor = [0] * 8

# Passo 2: Leitura dos 8 inteiros (podem ser positivos ou negativos, mas não zero)
print("--- Cadastro de 8 Inteiros ---")
for i in range(8):
    valido = False
    while not valido:
        val = input(f"Digite o {i+1}º número (positivo ou negativo, exceto zero): ")
        val = int(val)
        if val != 0:
            vetor[i] = val
            valido = True
        else:
            print("Erro: O número não pode ser zero. Digite novamente.")

# Passo 3: Contagem de positivos, negativos e acumulação dos positivos
cont_positivos = 0
cont_negativos = 0
soma_positivos = 0

for i in range(8):
    if vetor[i] > 0:
        cont_positivos = cont_positivos + 1
        soma_positivos = soma_positivos + vetor[i]
    else:
        cont_negativos = cont_negativos + 1

# Passo 4: Exibição dos resultados
print("\n--- RELATÓRIO DO VETOR ---")
print(f"Vetor de Entrada: {vetor}")
print(f"Total de números positivos: {cont_positivos}")
print(f"Total de números negativos: {cont_negativos}")

if cont_positivos > 0:
    media_positivos = soma_positivos / cont_positivos
    print(f"Média aritmética simples dos números positivos: {media_positivos:.2f}")
else:
    print("Média aritmética simples dos números positivos: Não aplicável (zero positivos cadastrados)")
