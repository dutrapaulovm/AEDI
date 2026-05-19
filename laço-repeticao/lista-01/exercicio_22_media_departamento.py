# Exercício 22: Média Salarial de Departamentos
# Objetivo: Ler 5 códigos de departamento e seus respectivos salários, calculando a soma e média salarial dos departamentos válidos.

# Passo 1: Inicialização das variáveis acumuladoras
soma_salarial = 0.0
total_validos = 0

# Passo 2: Laço de repetição para ler 5 departamentos e salários
for vez in range(1, 6):
    codigo = input(f"Digite o código do {vez}º departamento (1 a 4): ")
    codigo = int(codigo)
    
    salario = input(f"Digite o salário do {vez}º departamento: ")
    salario = float(salario)
    
    # Passo 3: Mapeamento de departamento
    if codigo == 1:
        nome_dept = "Vendas"
    elif codigo == 2:
        nome_dept = "RH"
    elif codigo == 3:
        nome_dept = "TI"
    elif codigo == 4:
        nome_dept = "Marketing"
    else:
        nome_dept = "Desconhecido"
        
    print(f"Departamento: {nome_dept}")
    
    # Passo 4: Acumulação apenas de departamentos conhecidos
    if nome_dept != "Desconhecido":
        soma_salarial = soma_salarial + salario
        total_validos = total_validos + 1

# Passo 5: Cálculo da média e exibição do relatório final
print("\n--- Relatório Final ---")
print(f"Soma total salarial dos departamentos válidos: R$ {soma_salarial:.2f}")

if total_validos > 0:
    media = soma_salarial / total_validos
    print(f"Média salarial dos departamentos válidos: R$ {media:.2f}")
else:
    print("Nenhum departamento válido foi inserido para o cálculo da média.")
