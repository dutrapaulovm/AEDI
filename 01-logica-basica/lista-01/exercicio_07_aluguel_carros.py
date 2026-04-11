# Exercício 7: Aluguel de Carros
# Objetivo: Calcular o valor total a pagar por um carro alugado considerando dias e km.

# Preços definidos pela locadora
CUSTO_DIA = 60.00
CUSTO_KM = 0.15

# Passo 1: Coleta dos dados do aluguel
dias_alugados = input("Por quantos dias o carro foi alugado? ")
dias_alugados = int(dias_alugados)

km_percorridos = input("Quantos Km foram percorridos? ")
km_percorridos = float(km_percorridos)

# Passo 2: Cálculo dos valores parciais e total
total_dias = dias_alugados * CUSTO_DIA
total_km = km_percorridos * CUSTO_KM
valor_total_pagar = total_dias + total_km

# Passo 3: Exibição do orçamento final
print(f"Custo pelos {dias_alugados} dias: R$ {total_dias:.2f}")
print(f"Custo pelos {km_percorridos} km: R$ {total_km:.2f}")
print(f"Total a pagar pelo aluguel: R$ {valor_total_pagar:.2f}")
