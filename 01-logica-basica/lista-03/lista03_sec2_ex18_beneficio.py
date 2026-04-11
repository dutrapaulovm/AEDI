# Exercício 18: Idade de Benefício
# Objetivo: Checar múltiplas demografias para governo

# Passo 1: Leitura
idade = input("Idade: ")
idade = int(idade)
sexo = input("Sexo (M/F): ")
sexo = sexo.upper()

# Passo 2: Condições combinadas
if (sexo == "M" and idade >= 65) or (sexo == "F" and idade >= 60):
    print("Elegível para benefício")
else:
    print("Não elegível")
