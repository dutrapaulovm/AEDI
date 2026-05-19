# Exercício 32: Média Ponderada com Validação de Pesos
# (Seção 2, Exercício 26 da Lista)
# Objetivo: Calcular a média ponderada de 3 notas, validando se a soma dos pesos fornecidos é exatamente igual a 100%.

# Passo 1: Leitura das notas e seus respectivos pesos
nota1 = input("Digite a Nota 1: ")
nota1 = float(nota1)
peso1 = input("Digite o Peso 1 (em %): ")
peso1 = float(peso1)

nota2 = input("Digite a Nota 2: ")
nota2 = float(nota2)
peso2 = input("Digite o Peso 2 (em %): ")
peso2 = float(peso2)

nota3 = input("Digite a Nota 3: ")
nota3 = float(nota3)
peso3 = input("Digite o Peso 3 (em %): ")
peso3 = float(peso3)

# Passo 2: Cálculo da soma dos pesos
soma_pesos = peso1 + peso2 + peso3
print(f"Soma dos pesos: {soma_pesos}%")

# Passo 3: Validação de integridade dos pesos
if soma_pesos != 100.0:
    print("Erro: A soma dos pesos deve ser exatamente 100%.")
else:
    # Passo 4: Cálculo da média ponderada
    media_final = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / soma_pesos
    print(f"Média Final: {media_final:.2f}")
