# Exercício 2: Operação baseada no sinal
# Objetivo: Raiz se >= 0, quadrado se < 0
import math

# Passo 1: Leitura e conversão
x = input("Digite um número real: ")
x = float(x)

# Passo 2: Verificação condicional
if x >= 0:
    # Passo 3a: Operação para números não negativos
    resultado = math.sqrt(x)
    print(f"A raiz quadrada de {x} é {resultado:.2f}")
else:
    # Passo 3b: Operação para números negativos
    resultado = x ** 2
    print(f"O quadrado de {x} é {resultado:.2f}")
