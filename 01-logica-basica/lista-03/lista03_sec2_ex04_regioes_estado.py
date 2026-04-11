# Exercício 4: Região do Estado
# Objetivo: Mapa de sigla para Região

# Passo 1: Leitura e ajuste
sigla = input("Digite a sigla do estado: ")
sigla = sigla.upper()

# Passo 2: Avaliação com lógica 'ou' sintática (in / or)
if sigla == "SP" or sigla == "RJ" or sigla == "MG" or sigla == "ES":
    print("Sudeste")
elif sigla == "PR" or sigla == "SC" or sigla == "RS":
    print("Sul")
elif sigla == "BA" or sigla == "PE" or sigla == "CE" or sigla == "RN":
    print("Nordeste")
else:
    print("Outras regiões")
