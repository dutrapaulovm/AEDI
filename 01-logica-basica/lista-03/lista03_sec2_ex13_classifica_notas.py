# Exercício 13: Conceitos Finais
# Objetivo: Desempenho letivo.

# Passo 1: Leitura e formatação real
nota = input("Nota de 0 a 10: ")
nota = float(nota)

# Passo 2: Validação de escopo principal e ramificações
if nota < 0 or nota > 10:
    print("Nota inválida.")
else:
    # Passo 3: Avaliar categorias de score
    if nota >= 9:
        print("Excelente")
    elif nota >= 7 and nota < 9:
        print("Bom")
    elif nota >= 5 and nota < 7:
        print("Regular")
    else:
        print("Ruim")
