# Exercício 17: Avaliação de Polinômio por Vetor de Coeficientes
# Objetivo: Armazenar 5 coeficientes de um polinômio de 4º grau em um vetor [a0, a1, a2, a3, a4], ler um valor x, e calcular P(x) = a4*x^4 + a3*x^3 + a2*x^2 + a1*x + a0.

# Passo 1: Inicialização do vetor de 5 coeficientes
# O índice i corresponde ao termo a_i (coeficiente de x^i)
coeficientes = [0.0] * 5

# Passo 2: Leitura dos coeficientes (a0 até a4)
print("--- Cadastro de Coeficientes do Polinômio de 4º Grau P(x) ---")
for i in range(5):
    coef = input(f"Digite o coeficiente a{i} (termo associado a x^{i}): ")
    coef = float(coef)
    coeficientes[i] = coef

# Passo 3: Leitura do valor de x
print("\n--- Ponto de Avaliação ---")
x = input("Digite o valor de x para avaliar o polinômio P(x): ")
x = float(x)

# Passo 4: Cálculo de P(x) usando loop simples e o operador de exponenciação **
valor_polinomio = 0.0
print("\nProcessamento termo a termo:")

for i in range(5):
    coef = coeficientes[i]
    # Termo = coef * x^i
    termo = coef * (x ** i)
    valor_polinomio = valor_polinomio + termo
    print(f"  Termo a{i}*x^{i} : {coef:.2f} * ({x:.2f}^{i}) = {termo:.4f}")

# Passo 5: Exibição do polinômio formatado e do resultado final
print(f"\nPolinômio: P(x) = ({coeficientes[4]:.2f})*x^4 + ({coeficientes[3]:.2f})*x^3 + ({coeficientes[2]:.2f})*x^2 + ({coeficientes[1]:.2f})*x^1 + ({coeficientes[0]:.2f})")
print(f"Resultado final: P({x}) = {valor_polinomio:.4f}")
