# Exercício 4: Letra central composta x simples
# Objetivo: Testes com sub-arrays em python e len

# Passo 1
palavra = input("Digite uma palavra: ")
tamanho = len(palavra)

# Passo 2: Dividir ramificações vitais
if tamanho == 0:
    print("Rejeitado vazio")
elif tamanho % 2 != 0:
    # Passo 3 (Tamanho ímpar)
    meio = tamanho // 2
    letra = palavra[meio]
    
    if letra in "aeiou":
        print("Válido: a central única é vogal")
    else:
        print("Inválido: central única não é vogal")
else:
    # Passo 4 (Tamanho par)
    meio2 = tamanho // 2
    meio1 = meio2 - 1
    
    # Concatenação da fatia de tamanho 2
    letras = palavra[meio1:meio2+1]
    
    if letras == "rr" or letras == "ss":
        print("Válido: centrais compõem rr ou ss")
    else:
        print("Inválido: não compõem rr ou ss")
