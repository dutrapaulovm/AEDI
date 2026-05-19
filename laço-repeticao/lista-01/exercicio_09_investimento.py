# Exercício 9: Evolução de Investimento com Aportes Constantes
# Objetivo: Calcular a evolução mensal de um investimento com aportes constantes durante n meses.

# Passo 1: Leitura das entradas do usuário
P = input("Digite o capital inicial (P): ")
P = float(P)

i = input("Digite a taxa de juros mensal em decimal (ex: 0.01 para 1%): ")
i = float(i)

PMT = input("Digite o valor do aporte mensal constante (PMT): ")
PMT = float(PMT)

n = input("Digite o período total em meses (n): ")
n = int(n)

# Passo 2: Inicialização do montante acumulador com o capital inicial
saldo = P

# Passo 3: Laço de repetição para calcular a atualização do saldo mês a mês
for mes in range(1, n + 1):
    # Aplica os juros sobre o saldo anterior e adiciona o aporte mensal (PMT)
    saldo = saldo * (1.0 + i) + PMT
    
    # Imprime o saldo atualizado do mês correspondente
    print(f"Mês {mes}: R$ {saldo:.2f}")

# Passo 4: Exibição do montante final
print(f"Saldo acumulado final: R$ {saldo:.2f}")
