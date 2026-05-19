# Exercício 30: Série de Gregory-Leibniz
# (Seção 2, Exercício 24 da Lista)
# Objetivo: Calcular o valor aproximado de pi/4 e pi através da soma dos primeiros n termos da série de Gregory-Leibniz.

# Passo 1: Leitura da quantidade de termos n
n = input("Digite a quantidade de termos a serem somados (n): ")
n = int(n)

# Passo 2: Inicialização das variáveis de controle
soma = 0.0
denominador = 1
sinal = 1

# Passo 3: Laço de repetição de 0 até n-1
for i in range(n):
    # Calcula o termo atual da série
    termo = sinal * (1.0 / denominador)
    soma = soma + termo
    
    # Exibe informações do termo para o teste de mesa
    print(f"Termo {i}: Denominador={denominador}, Sinal={sinal}, Operação na Soma={termo:+.6f}")
    
    # Alterna o sinal para a próxima iteração
    sinal = sinal * -1
    # Incrementa o denominador em 2
    denominador = denominador + 2

# Passo 4: Cálculo da aproximação de pi (multiplicando a soma por 4)
pi_aproximado = soma * 4.0

# Passo 5: Exibição do resultado final
print(f"\nSoma total da série (S) = pi/4 = {soma:.6f}")
print(f"Valor aproximado de pi = {pi_aproximado:.6f}")
