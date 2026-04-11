# Exercício 34: SAC
# Objetivo: Amortização Constante.

V = input("Valor do empréstimo: ")
V = float(V)
i_anual = input("Taxa de juros anual (em %, ex: 12): ")
i_anual = float(i_anual) / 100
n = input("Número de meses: ")
n = int(n)

A = V / n
saldo = V
i_mensal = i_anual / 12  # Ou pode usar o anual direto dependendo da regra financeira

for mes in range(1, n + 1):
    J = saldo * i_anual / 12  # A fórmula do PDF usa i/12
    P = J + A
    saldo -= A
    print(f"Mês {mes}: Juros = {J:.2f}, Amortização = {A:.2f}, Parcela = {P:.2f}")
