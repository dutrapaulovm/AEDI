# Exercício 8: Quantidade Salários
# Objetivo: Calcular quantos salários mínimos uma pessoa ganha.

# Passo 1: Leitura do valor atual do salário mínimo e do salário da pessoa
salario_minimo = input("Digite o valor do salário mínimo atual: R$ ")
salario_minimo = float(salario_minimo)

salario_pessoa = input("Digite o valor do seu salário: R$ ")
salario_pessoa = float(salario_pessoa)

# Passo 2: Cálculo da proporção
# Quantos salários mínimos cabem dentro do salário da pessoa
quantidade_salarios = salario_pessoa / salario_minimo

# Passo 3: Saída do resultado formatado
print(f"Com o salário de R$ {salario_pessoa:.2f}, você ganha o equivalente a {quantidade_salarios:.1f} salários mínimos.")
