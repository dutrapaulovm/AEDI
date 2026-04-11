# Exercício 1: Média Aritmética
# Objetivo: Calcular a média aritmética simples de três notas.

# Passo 1: Leitura das três notas (lendo como texto e depois convertendo)
nota1 = input("Digite a primeira nota: ")
nota1 = float(nota1)

nota2 = input("Digite a segunda nota: ")
nota2 = float(nota2)

nota3 = input("Digite a terceira nota: ")
nota3 = float(nota3)

# Passo 2: Cálculo da média aritmética
# O uso dos parênteses garante que a soma ocorra antes da divisão
media = (nota1 + nota2 + nota3) / 3

# Passo 3: Saída do resultado formatado com 2 casas decimais
print(f"A média aritmética do aluno é: {media:.2f}")
