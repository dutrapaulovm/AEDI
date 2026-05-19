# Exercício 18: Bissexto e Copa do Mundo
# Objetivo: Solicitar 5 anos e verificar se cada um é bissexto e/ou ano de Copa do Mundo.

# Passo 1: Laço de repetição para solicitar e verificar 5 anos
for vez in range(1, 6):
    ano = input(f"Digite o {vez}º ano: ")
    ano = int(ano)
    
    # Passo 2: Verificação de ano Bissexto
    eh_bissexto = False
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        eh_bissexto = True
        
    # Passo 3: Verificação de ano de Copa do Mundo
    # Ocorre de 4 em 4 anos a partir de 1930, excluindo anos divisíveis por 100
    eh_copa = False
    if ano >= 1930 and (ano - 1930) % 4 == 0 and ano % 100 != 0:
        eh_copa = True
        
    # Passo 4: Exibição dos resultados para o ano
    if eh_bissexto and eh_copa:
        print(f"O ano {ano} é bissexto E é ano de Copa do Mundo.")
    elif eh_bissexto:
        print(f"O ano {ano} é bissexto, mas NÃO é ano de Copa do Mundo.")
    elif eh_copa:
        print(f"O ano {ano} NÃO é bissexto, mas É ano de Copa do Mundo.")
    else:
        print(f"O ano {ano} NÃO é bissexto E NÃO é ano de Copa do Mundo.")
