# Exercício 33: Número Primo Básico Simulado
# Objetivo: Como não temos laço for permitido aqui, vamos usar lógica simples

# Passo 1
num = input("Número: ")
n = int(num)

# Passo 2: Validador sem estrutura de repetição para casos fixos
if n < 0:
    print("Negativo")
elif n == 2 or n == 3 or n == 5 or n == 7:
    print("Primo e positivo")
elif n > 1 and (n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0):
    # Regra empírica geral básica para primos pequenos / médios
    print("Primo e positivo")
elif n > 0:
    print("Não primo positivo")
else:
    print("Zero não é positivo nem negativo.")
