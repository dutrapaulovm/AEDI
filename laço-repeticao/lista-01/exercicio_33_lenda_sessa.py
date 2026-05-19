# Exercício 33: A Lenda de Sessa (O Tabuleiro de Xadrez)
# (Seção 2, Exercício 27 da Lista)
# Objetivo: Calcular a quantidade de grãos em uma casa específica n do xadrez e o total acumulado até ela, dobrando a cada casa e sem usar funções prontas de potência.

# Passo 1: Leitura da casa do xadrez n (1 a 64)
n = input("Digite a casa do tabuleiro de xadrez desejada (1 a 64): ")
n = int(n)

# Passo 2: Inicialização das variáveis de controle
graos_casa_atual = 1
total_acumulado = 0

# Passo 3: Laço de repetição para percorrer as casas de 1 até n
for casa in range(1, n + 1):
    # Se for a casa atual de interesse (casa == n), guardamos o valor individual
    if casa == n:
        graos_na_casa_n = graos_casa_atual
        
    # Acumula no total geral
    total_acumulado = total_acumulado + graos_casa_atual
    
    # Dobra a quantidade de grãos para a próxima casa (2 * anterior)
    graos_casa_atual = graos_casa_atual * 2

# Passo 4: Exibição dos resultados
print(f"Quantidade de grãos de trigo na casa {n}: {graos_na_casa_n}")
print(f"Total de grãos acumulados de 1 até a casa {n}: {total_acumulado}")
