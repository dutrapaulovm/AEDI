# Exercício 20: Potência e Raiz (Substituição)
# Objetivo: Imprimir de 1 a 100, substituindo potências de 2 por "Potência" e números com raiz quadrada inteira por "Raiz".

# Passo 1: Laço de repetição de 1 a 100
for i in range(1, 101):
    # Passo 2: Verifica se é potência de 2
    # Um número é potência de 2 se, ao dividirmos sucessivamente por 2, o resultado final for 1.
    eh_potencia_de_2 = False
    if i > 0:
        temp = i
        while temp % 2 == 0:
            temp = temp // 2
        if temp == 1:
            eh_potencia_de_2 = True
            
    # Passo 3: Verifica se a raiz quadrada é inteira
    raiz = i ** 0.5
    eh_raiz_inteira = (raiz == int(raiz))
    
    # Passo 4: Substituições conforme regras
    if eh_potencia_de_2:
        print("Potência")
    elif eh_raiz_inteira:
        print("Raiz")
    else:
        print(i)
