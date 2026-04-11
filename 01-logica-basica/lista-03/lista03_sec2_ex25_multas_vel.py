# Exercício 25: Radar Avançado
# Objetivo: Múltiplas faixas

# Passo 1
vel = input("Velocidade (km): ")
v = float(vel)

# Passo 2: Checagens por ordem de grandeza
if v <= 60:
    print("OK - Radar livre")
elif v >= 61 and v <= 80:
    print("Multa Leve")
elif v >= 81 and v <= 100:
    print("Multa Média")
else:
    print("Multa Grave")
