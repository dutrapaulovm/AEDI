# Exercício 11: Múltiplos e Substituições
# Objetivo: Imprimir os números de 1 a 100, substituindo os múltiplos de 7 de forma cíclica por "OpenAI", "GPT" e "IA".

# Passo 1: Laço de repetição de 1 a 100
for i in range(1, 101):
    # Passo 2: Verifica se o número é múltiplo de 7
    if i % 7 == 0:
        # Determina a posição no ciclo (7 -> 1, 14 -> 2, 21 -> 3, 28 -> 4, etc.)
        posicao = i // 7
        
        # Passo 3: Escolhe a palavra de acordo com a posição cíclica
        if posicao % 3 == 1:
            print("OpenAI")
        elif posicao % 3 == 2:
            print("GPT")
        else:
            print("IA")
    else:
        # Passo 4: Caso não seja múltiplo de 7, imprime o próprio número
        print(i)
