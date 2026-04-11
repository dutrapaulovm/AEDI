# Exercício 19: Calculadora de Multa
# Objetivo: Multar caso velocidade exceda 80Km/h e taxar R$7,00 por Km excedente.

LIMITE_VELOCIDADE = 80
TAXA_MULTA_KM = 7.00

# Passo 1: Obter velocidade do monitor de trânsito
velocidade = input("Qual a velocidade do carro (km/h)? ")
velocidade = float(velocidade)

# Passo 2: Decisão condicional (Se for multado)
if velocidade > LIMITE_VELOCIDADE:
    km_acima = velocidade - LIMITE_VELOCIDADE
    valor_multa = km_acima * TAXA_MULTA_KM
    
    # Passo 3: Dar a má notícia e exibir o painel do valor
    print(f"VOCÊ FOI MULTADO! Foi registrado trafegando {km_acima:.1f} km/h acima do limite estipulado.")
    print(f"Valor da Multa: R$ {valor_multa:.2f}")
else:
    # Passo 3: Passagem permitida
    print("Está dentro do limite permitido. Tenha um bom dia e dirija com segurança.")
