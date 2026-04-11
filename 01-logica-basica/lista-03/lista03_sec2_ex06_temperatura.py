# Exercício 6: Classificação de Temperatura
# Objetivo: Categorizar o clima

# Passo 1: Leitura e conversão
temperatura = input("Digite a temperatura: ")
temperatura = float(temperatura)

# Passo 2: Encadeamento
if temperatura < 10:
    print("Muito frio")
elif temperatura >= 10 and temperatura <= 25:
    print("Agradável")
else:
    print("Quente")
