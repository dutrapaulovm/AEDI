# Exercício 11: Sucessor e Antecessor
# Objetivo: Imprimir o número anterior e posterior a um número digitado.

# Passo 1: Entrada do número limitando a inteiros
numero = input("Digite um número: ")
numero = int(numero)

# Passo 2: Cálculo do antecessor (número - 1) e sucessor (número + 1)
antecessor = numero - 1
sucessor = numero + 1

# Passo 3: Exibição
print(f"O antecessor de {numero} é: {antecessor}")
print(f"O sucessor de {numero} é: {sucessor}")
