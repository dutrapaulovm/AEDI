# Exercício 15: Classificação de Triângulos
# Objetivo: Verificar se formam um triângulo e classificá-lo.

# Passo 1: Leitura dos 3 lados
lado_a = input("Primeiro lado: ")
lado_a = float(lado_a)

lado_b = input("Segundo lado: ")
lado_b = float(lado_b)

lado_c = input("Terceiro lado: ")
lado_c = float(lado_c)

# Passo 2: Condição de existência do triângulo
pode_formar_triangulo = (lado_a < lado_b + lado_c) and \
                        (lado_b < lado_a + lado_c) and \
                        (lado_c < lado_a + lado_b)

if pode_formar_triangulo:
    # Passo 3: Classificação Geométrica
    if lado_a == lado_b == lado_c:
        print("Os lados informados formam um Triângulo EQUILÁTERO.")
    elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
        print("Os lados informados formam um Triângulo ISÓSCELES.")
    else:
        print("Os lados informados formam um Triângulo ESCALENO.")
else:
    print("ERRO: Os valores informados NÃO FORMAM um triângulo compatível.")
