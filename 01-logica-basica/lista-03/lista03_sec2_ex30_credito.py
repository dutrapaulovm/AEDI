# Exercício 30: Condições de Crédito
# Objetivo: Mix de float e score int

# Passo 1: Coleta das finanças
renda = input("Renda: ")
renda = float(renda)
score = input("Score de crédito: ")
score = int(score)
dividas = input("Dívidas ativas: ")
dividas = float(dividas)

# Passo 2: Avaliação bancária fina
if score >= 700 and dividas == 0:
    print("Aprovado")
elif score >= 500 and dividas < renda:
    print("Em análise")
else:
    print("Negado")
