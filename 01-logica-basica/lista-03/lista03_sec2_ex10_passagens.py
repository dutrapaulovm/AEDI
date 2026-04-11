# Exercício 10: Tabela de Preços Aéreo
# Objetivo: Matriz condicional aninhada

# Passo 1: Leitura e parser
destino = input("Destino (Norte, Nordeste, Centro-Oeste, Sul): ")
destino = destino.capitalize()
tipo = input("Tipo (1 - Ida | 2 - Ida e Volta): ")
tipo = int(tipo)

# Passo 2: Validações para tabela
if destino == "Norte":
    if tipo == 1:
        preco = 500.00
    else:
        preco = 900.00
elif destino == "Nordeste":
    if tipo == 1:
        preco = 350.00
    else:
        preco = 650.00
elif destino == "Centro-oeste":
    if tipo == 1:
        preco = 350.00
    else:
        preco = 600.00
elif destino == "Sul":
    if tipo == 1:
        preco = 300.00
    else:
        preco = 550.00
else:
    # Passo Extra: Lidar com erros
    preco = 0.00
    print("Destino inválido!")

if preco > 0:
    # Passo 3: Exposição
    print(f"O valor da passagem é: R$ {preco:.2f}")
