# Exercício 4: Área de uma Parede e Tinta
# Objetivo: Calcular a área de uma parede e a tinta necessária para pintar.

# Passo 1: Entrada das dimensões da parede
largura = input("Digite a largura da parede em metros: ")
largura = float(largura)

altura = input("Digite a altura da parede em metros: ")
altura = float(altura)

# Passo 2: Cálculo da área (largura x altura)
area = largura * altura

# Passo 3: Cálculo da quantidade de tinta (1 litro pinta 2 metros quadrados)
tinta_necessaria = area / 2

# Passo 4: Exibição dos resultados
print(f"A área da sua parede é de {area:.2f} m².")
print(f"Você precisará de {tinta_necessaria:.2f} litros de tinta para pintá-la.")
