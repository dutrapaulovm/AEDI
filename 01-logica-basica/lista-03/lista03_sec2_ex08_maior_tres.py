# Exercício 8: Maior de três
# Objetivo: Descobrir o topo entre três variáveis

# Passo 1: Leitura e conversão
a = input("a: ")
a = float(a)
b = input("b: ")
b = float(b)
c = input("c: ")
c = float(c)

# Passo 2: Verificações e asserções diretas num único escopo
if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
else:
    # Se 'a' e 'b' não atingiram o topo, logo é 'c'
    maior = c

# Passo 3: Resultado
print(f"Maior = {maior}")
