# Importa da biblioteca matemática somente 
# a função sqrt
# from math import sqrt
# Importa todas as funções da biblioteca
# from math import *

# Segunda forma de importação
# Nesta segunda forma, você consegue utilizar todas
# as funções da biblioteca math
import math as mt

numero = input("Digite um valor: ")
numero = int(numero)

if numero >= 0:    
    print(f"O valor da raiz quadrada é: {mt.sqrt(numero)}")
else:
    # pow(numero, 2)
    # numero * numero
    print(f"O valor da potência é: {numero ** 2}")
                                