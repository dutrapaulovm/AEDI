# Exercício 16: Cálculo de IMC
# Objetivo: Calcular e classificar o Índice de Massa Corporal.

# Passo 1: Leitura do peso e altura
peso = input("Qual é o seu peso? (Kg) ")
peso = float(peso)

altura = input("Qual é a sua altura? (m) ")
altura = float(altura)

# Passo 2: Fórmula do IMC (Peso em Kg / Altura² em Metros)
imc = peso / (altura ** 2)

print(f"O seu IMC é: {imc:.1f}")

# Passo 3: Aninhamento de Condicionais para encontrar a categoria exata
if imc < 18.5:
    print("Categoria: Abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("Categoria: Peso normal.")
elif imc >= 25 and imc < 30:
    print("Categoria: Sobrepeso.")
else:
    print("Categoria: Obesidade.")
