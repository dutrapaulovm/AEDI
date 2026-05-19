# Exercício 20: Magnitude de Vetores e Ângulo Relativo (Geometria Vetorial 2D)
# Objetivo: Armazenar componentes de dois vetores 2D (U e V) em vetores de tamanho 2, computar suas magnitudes, o produto escalar e o ângulo relativo entre eles (em graus).

import math

# Passo 1: Inicialização dos componentes dos vetores U e V (tamanho 2)
# Índice 0: Componente X, Índice 1: Componente Y
vetor_u = [0.0, 0.0]
vetor_v = [0.0, 0.0]

# Passo 2: Leitura das coordenadas de U e V
print("--- Geometria Vetorial 2D ---")
print("Vetor U:")
vetor_u[0] = float(input("  Digite a componente X de U: "))
vetor_u[1] = float(input("  Digite a componente Y de U: "))

print("\nVetor V:")
vetor_v[0] = float(input("  Digite a componente X de V: "))
vetor_v[1] = float(input("  Digite a componente Y de V: "))

# Passo 3: Cálculo das magnitudes (normas euclidianas)
# ||U|| = sqrt(Ux^2 + Uy^2)
magnitude_u = (vetor_u[0]**2 + vetor_u[1]**2) ** 0.5
magnitude_v = (vetor_v[0]**2 + vetor_v[1]**2) ** 0.5

# Passo 4: Cálculo do produto escalar U . V
# U . V = Ux*Vx + Uy*Vy
produto_escalar = (vetor_u[0] * vetor_v[0]) + (vetor_u[1] * vetor_v[1])

# Passo 5: Cálculo do ângulo entre os dois vetores
# cos(theta) = (U . V) / (||U|| * ||V||)
if magnitude_u == 0.0 or magnitude_v == 0.0:
    print("\nErro: Um dos vetores informados é o vetor nulo. O ângulo e a direção não podem ser determinados.")
else:
    cos_theta = produto_escalar / (magnitude_u * magnitude_v)
    
    # Validação do cos(theta) para evitar pequenos erros de precisão flutuante que saem do intervalo [-1, 1]
    if cos_theta > 1.0:
        cos_theta = 1.0
    elif cos_theta < -1.0:
        cos_theta = -1.0
        
    # Obtém o ângulo em radianos e converte para graus
    angulo_rad = math.acos(cos_theta)
    angulo_graus = math.degrees(angulo_rad)
    
    # Passo 6: Exibição dos resultados geométricos
    print("\n--- ANÁLISE GEOMÉTRICA DOS VETORES ---")
    print(f"Vetor U: ({vetor_u[0]:.2f}, {vetor_u[1]:.2f})")
    print(f"Vetor V: ({vetor_v[0]:.2f}, {vetor_v[1]:.2f})")
    print(f"Magnitude de U (||U||): {magnitude_u:.4f}")
    print(f"Magnitude de V (||V||): {magnitude_v:.4f}")
    print(f"Produto Escalar (U · V): {produto_escalar:.4f}")
    print(f"Cosseno de teta (cos θ):  {cos_theta:.4f}")
    print(f"Ângulo entre U e V:     {angulo_graus:.2f}º (ou {angulo_rad:.4f} rad)")
