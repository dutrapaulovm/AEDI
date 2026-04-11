# Exercício 12: Média Ponderada
# Objetivo: Calcular a média ponderada de 4 números com pesos 1, 2, 3 e 4.

# Passo 1: Leitura das 4 notas
nota1 = input("Digite a 1ª nota (peso 1): ")
nota1 = float(nota1)

nota2 = input("Digite a 2ª nota (peso 2): ")
nota2 = float(nota2)

nota3 = input("Digite a 3ª nota (peso 3): ")
nota3 = float(nota3)

nota4 = input("Digite a 4ª nota (peso 4): ")
nota4 = float(nota4)

# Passo 2: Cálculo da pontuação com os respectivos pesos
peso_total = 1 + 2 + 3 + 4
soma_ponderada = (nota1 * 1) + (nota2 * 2) + (nota3 * 3) + (nota4 * 4)

# Passo 3: Divisão da soma pelo peso total da fórmula
media_ponderada = soma_ponderada / peso_total

# Passo 4: Exibição
print(f"A sua média ponderada final é: {media_ponderada:.1f}")
