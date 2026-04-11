# Exercício 24: Workflow Bancário Simulador
# Objetivo: Validar cheque especial

# Passo 1: Leitura
saldo = input("Saldo Atual: ")
saldo = float(saldo)
limite = input("Limite Especial Pessoal: ")
limite = float(limite)
saque = input("Valor para sacar: ")
saque = float(saque)

# Passo 2: Avaliação bancária
if saque <= saldo:
    print("Saque permitido com saldo")
elif saque <= (saldo + limite):
    print("Saque permitido com limite especial")
else:
    print("Saque negado. Faltaram fundos totais.")
