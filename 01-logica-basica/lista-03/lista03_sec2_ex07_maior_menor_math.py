# Exercício 7: Mínimo e Máximo Condicionado
# Objetivo: Quadrado do menor, raiz do maior.
import math

# Passo 1: Leitura e conversão
a = input("Digite o primeiro número: ")
a = float(a)
b = input("Digite o segundo número: ")
b = float(b)

# Passo 2: Identificar menor e maior
if a < b:
    menor = a
    maior = b
else:
    menor = b
    maior = a

print(f"O menor valor é {menor} e o maior é {maior}")

# Passo 3: Operação no Menor
quadrado_menor = menor ** 2
print(f"O quadrado do menor é: {quadrado_menor:.2f}")

# Passo 4: Operação no Maior (apenas se positivo)
if maior >= 0:
    raiz_maior = math.sqrt(maior)
    print(f"A raiz do maior é: {raiz_maior:.2f}")
else:
    print("O maior valor é negativo, então não calcularemos a raiz real.")
