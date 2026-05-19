# Exercício 6: Área do Triângulo
# Objetivo: Calcular a área de um triângulo a partir das coordenadas de seus 3 vértices utilizando fórmula de somatório.

# Passo 1: Leitura das coordenadas do Vértice 1
x1 = input("Vértice 1 - Digite x1: ")
x1 = float(x1)
y1 = input("Vértice 1 - Digite y1: ")
y1 = float(y1)

# Passo 2: Leitura das coordenadas do Vértice 2
x2 = input("Vértice 2 - Digite x2: ")
x2 = float(x2)
y2 = input("Vértice 2 - Digite y2: ")
y2 = float(y2)

# Passo 3: Leitura das coordenadas do Vértice 3
x3 = input("Vértice 3 - Digite x3: ")
x3 = float(x3)
y3 = input("Vértice 3 - Digite y3: ")
y3 = float(y3)

# Passo 4: Cálculo dos termos do somatório para a área
# Considerando o fechamento da figura (x4 = x1 e y4 = y1)
termo1 = x1 * y2 - x2 * y1
termo2 = x2 * y3 - x3 * y2
termo3 = x3 * y1 - x1 * y3

# Passo 5: Cálculo do valor absoluto da soma e da área final
soma = termo1 + termo2 + termo3
area = 0.5 * abs(soma)

# Passo 6: Exibição do resultado
print(f"A área do triângulo é: {area:.4f}")
