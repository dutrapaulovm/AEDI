# Exercício 2: Conversor de Medidas
# Objetivo: Converter um valor de metros para centímetros e milímetros.

# Passo 1: Entrada do valor em metros
metros = input("Digite o valor em metros: ")
metros = float(metros)

# Passo 2: Processamento e conversões
# 1 metro = 100 centímetros
centimetros = metros * 100
# 1 metro = 1000 milímetros
milimetros = metros * 1000

# Passo 3: Exibição dos três valores
print(f"Valor original: {metros}m")
print(f"Em centímetros: {centimetros}cm")
print(f"Em milímetros: {milimetros}mm")
