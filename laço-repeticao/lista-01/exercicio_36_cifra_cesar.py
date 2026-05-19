# Exercício 36: Cifra de César
# (Seção 3, Exercício 1 da Lista)
# Objetivo: Realizar a encriptação de uma mensagem contendo apenas letras maiúsculas utilizando a Cifra de César com deslocamento k.

# Passo 1: Leitura da mensagem e da chave de deslocamento
mensagem = input("Digite a mensagem a ser criptografada (letras maiúsculas): ")
k = input("Digite o valor de deslocamento (chave k): ")
k = int(k)

# Passo 2: Inicialização da string resultante criptografada
resultado = ""

# Passo 3: Laço de repetição para percorrer cada caractere da mensagem
for caractere in mensagem:
    # Verifica se o caractere é uma letra maiúscula
    if "A" <= caractere <= "Z":
        # Encontra a posição da letra de 0 (A) a 25 (Z)
        posicao = ord(caractere) - ord("A")
        
        # Aplica a fórmula da Cifra de César com aritmética modular (mod 26)
        nova_posicao = (posicao + k) % 26
        
        # Converte de volta para caractere
        novo_caractere = chr(nova_posicao + ord("A"))
        resultado = resultado + novo_caractere
    else:
        # Mantém espaços ou outros caracteres intactos
        resultado = resultado + caractere

# Passo 4: Exibição do resultado
print(f"Mensagem Criptografada: {resultado}")
