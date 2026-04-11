# Exercício 1 (Seção Strings): Letra central é vogal
# Objetivo: Tamanho, indexação e busca.

# Passo 1
palavra = input("Digite a palavra: ")

# Passo 2
tamanho = len(palavra)

if tamanho % 2 == 0:
    # Passo 3a
    print("Tamanho par -> Não possui letra central única")
else:
    # Passo 3b: Acha o meio (divisão inteira)
    meio = tamanho // 2
    letra_central = palavra[meio].lower()
    
    if letra_central in "aeiou":
        print("A letra central é vogal")
    else:
        print("Não é vogal")
