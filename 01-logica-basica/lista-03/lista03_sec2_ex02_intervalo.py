# Exercício 2: Intervalo (10, 50)
# Objetivo: Verificar se o número pertence ao intervalo

# Passo 1: Leitura e conversão
n = input("Digite um número: ")
n = float(n)

# Passo 2: Verificador lógico (and)
if n >= 10 and n <= 50:
    # Passo 3a: Satisfaz ambas as lógicas
    print("O número está DENTRO do intervalo entre 10 e 50")
else:
    # Passo 3b: Falha na intersecção
    print("O número está FORA do intervalo entre 10 e 50")
