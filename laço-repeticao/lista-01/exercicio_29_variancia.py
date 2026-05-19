# Exercício 29: Variância de Notas
# (Seção 2, Exercício 23 da Lista)
# Objetivo: Solicitar 3 notas de alunos, calcular a média aritmética e a variância das notas.

# Passo 1: Leitura das 3 notas dos alunos
nota1 = input("Digite a primeira nota: ")
nota1 = float(nota1)

nota2 = input("Digite a segunda nota: ")
nota2 = float(nota2)

# Correção na leitura da nota3
nota3 = input("Digite a terceira nota: ")
nota3 = float(nota3)

# Passo 2: Cálculo da média das notas
media = (nota1 + nota2 + nota3) / 3.0

# Passo 3: Cálculo das diferenças ao quadrado em relação à média
diff1_quad = (nota1 - media) ** 2
diff2_quad = (nota2 - media) ** 2
diff3_quad = (nota3 - media) ** 2

# Passo 4: Cálculo da variância (média das diferenças ao quadrado)
soma_diffs = diff1_quad + diff2_quad + diff3_quad
variancia = soma_diffs / 3.0

# Passo 5: Exibição dos resultados
print(f"Média das notas: {media:.2f}")
print(f"Variância das notas: {variancia:.4f}")
