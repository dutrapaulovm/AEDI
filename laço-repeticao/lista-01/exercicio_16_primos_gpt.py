# Exercício 16: Primos e GPT
# Objetivo: Imprimir números de 1 a 100, substituindo primos por "Prime" e múltiplos de 7 por "GPT".

# Passo 1: Laço de repetição de 1 a 100
for i in range(1, 101):
    # Passo 2: Verifica se é múltiplo de 7 primeiro
    if i % 7 == 0:
        print("GPT")
    else:
        # Passo 3: Verifica se o número é primo
        eh_primo = True
        if i <= 1:
            eh_primo = False
        else:
            for divisor in range(2, i):
                if i % divisor == 0:
                    eh_primo = False
                    break
        
        # Passo 4: Exibe o resultado de acordo com a condição
        if eh_primo:
            print("Prime")
        else:
            print(i)
