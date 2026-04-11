# Exercício 14: Maior de Dois Números
# Objetivo: Indicar qual dos dois números digitados é o maior ou se são iguais.

# Passo 1: Coletar os valores
numero1 = input("Digite o 1º número: ")
numero1 = float(numero1)

numero2 = input("Digite o 2º número: ")
numero2 = float(numero2)

# Passo 2 e 3: Processamento e Saída conjunta usando If/Elif/Else
if numero1 > numero2:
    print(f"O maior número é {numero1}.")
elif numero2 > numero1:
    print(f"O maior número é {numero2}.")
else:
    # Tratativa do desafio extra: números iguais
    print("Os dois números são iguais (possuem o mesmo valor).")
