numero = input("Digite um número: ")
numero = int(numero)
# Calcula o resto da divisão
resto = numero % 2
# Verificando se número é Par ou Impar
if resto == 0:
    print(f"O número {numero} é par")
else: #caso contrário
    print(f"O número {numero} é impar")


