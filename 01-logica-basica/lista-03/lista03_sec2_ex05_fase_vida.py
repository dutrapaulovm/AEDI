# Exercício 5: Classificação por Idade
# Objetivo: Categorizar as idades

# Passo 1: Leitura e conversão
idade = input("Digite a idade: ")
idade = int(idade)

# Passo 2: Avaliação dos intervalos restritos
if idade < 0:
    print("Erro: Idade inválida")
elif idade >= 0 and idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
else:
    print("Idoso")
