# Exercício 20: IMC Avançado
# Objetivo: Recriar IMC com lógicas duplas `and`

# Passo 1: Entrada e cálculo
peso = input("Peso: ")
peso = float(peso)
altura = input("Altura (m): ")
altura = float(altura)

imc = peso / (altura * altura)

# Passo 2: Classificação
if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Peso normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")
