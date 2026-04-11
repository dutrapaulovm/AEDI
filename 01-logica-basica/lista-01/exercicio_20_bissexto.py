# Exercício 20: Verificador de Ano Bissexto
# Objetivo: Usar conjunções Lógicas complexas para validar um ano Bissexto.

# Passo 1: Informação do ano a ser checado
ano = input("Que ano deseja verificar? ")
ano = int(ano)

# Passo 2: Regra do Ano Bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    # Passo 3: Confirmação condicional verdadeira
    print(f"O ano {ano} É um ano BISSEXTO.")
else:
    print(f"O ano {ano} NÃO É um ano bissexto.")
