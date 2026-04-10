nota1 = input("Digite a nota 1: ")
nota1 = float(nota1)

nota2 = input("Digite a nota 2: ")
nota2 = float(nota2)

nota3 = input("Digite a nota 3: ")
nota3 = float(nota3)

soma = nota1 + nota2 + nota3
media = soma / 3
# media = (nota1 + nota2 + nota3) / 3
print("A média é:", media)
# a letra f antes aspas significa formatação
# ou seja, estamos informando que queremos
# formatar um valor
print(f"A média é: {media:.2f}")





