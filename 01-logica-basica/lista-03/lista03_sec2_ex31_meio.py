# Exercício 31: O número Intermediário
# Objetivo: Achar o "do meio"

# Passo 1
a = input("Num A: ")
a = float(a)
b = input("Num B: ")
b = float(b)
c = input("Num C: ")
c = float(c)

# Passo 2: Achar as pontas
maior = a
if b > maior: maior = b
if c > maior: maior = c

menor = a
if b < menor: menor = b
if c < menor: menor = c

# Passo 3: Subtração do total
intermediario = (a + b + c) - maior - menor
print(f"Maior = {maior}, Menor = {menor}, Intermediário = {intermediario}")
