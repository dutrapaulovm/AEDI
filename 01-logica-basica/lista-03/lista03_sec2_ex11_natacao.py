# Exercício 11: Categorias Natação
# Objetivo: Disjuntos definidos de idades

# Passo 1: Leitura e casting
idade = input("Qual a idade do nadador? ")
idade = int(idade)

# Passo 2: Classificação e retorno individual
if idade < 5:
    print("O nadador não se enquadra em nenhuma categoria")
elif idade >= 5 and idade <= 7:
    print("Infantil A")
elif idade >= 8 and idade <= 10:
    print("Infantil B")
elif idade >= 11 and idade <= 13:
    print("Juvenil A")
elif idade >= 14 and idade <= 17:
    print("Juvenil B")
else:
    print("Adulto")
