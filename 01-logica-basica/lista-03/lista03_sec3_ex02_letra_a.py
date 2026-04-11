# Exercício 2: Iniciar com a
# Objetivo: Acesso direto posição [0]

# Passo 1
palavra = input("Digite uma palavra: ")

if len(palavra) > 0:
    # Passo 2: Comparação de caractere inicial
    if palavra[0] == "a" or palavra[0] == "A":
        print("Inicia com a letra a")
    else:
        print("Não inicia com a letra a")
else:
    print("Palavra vazia")
