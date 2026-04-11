# Exercício 3: Repartição de Salas Alfabético
# Objetivo: Opcionais relacionais em strings.

# Passo 1
nome = input("Digite o nome: ")

if len(nome) > 0:
    # Passo 2: Pega inicial pura e limpa
    inicial = nome[0].upper()
    
    # Passo 3: Avaliação alfabética em Python (A < B < C...)
    if inicial >= "A" and inicial <= "I":
        print("Sala F1")
    elif inicial >= "J" and inicial <= "R":
        print("Sala F2")
    elif inicial >= "S" and inicial <= "Z":
        print("Sala F3")
    else:
        print("Letra fora dos parâmetros")
