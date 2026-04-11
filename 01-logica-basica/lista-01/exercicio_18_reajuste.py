# Exercício 18: Reajuste Salarial
# Objetivo: Calcular o aumento salarial por faixas de valor existente.

# Passo 1: Entrada do salário atual
salario_antigo = input("Digite o salário atual do funcionário: R$ ")
salario_antigo = float(salario_antigo)

# Passo 2: Condicionais da tabela de percentuais
if salario_antigo <= 1500.00:
    percentual_aumento = 20
elif salario_antigo <= 3000.00:
    percentual_aumento = 15
else:
    percentual_aumento = 10

# Passo 3: Cálculos em cima do percentual decidido
valor_aumento = salario_antigo * (percentual_aumento / 100)
novo_salario = salario_antigo + valor_aumento

# Passo 4: Exibição do relatório de reajuste
print("--- RELATÓRIO DO AUMENTO ---")
print(f"Salário anterior: R$ {salario_antigo:.2f}")
print(f"Percentual aplicado: {percentual_aumento}%")
print(f"Valor do aumento recebido: R$ {valor_aumento:.2f}")
print(f"Novo Salário: R$ {novo_salario:.2f}")
