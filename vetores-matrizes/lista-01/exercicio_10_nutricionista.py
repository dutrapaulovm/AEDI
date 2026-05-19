# Exercício 10: Registro e Monitoramento de Calorias (Matriz 3x4)
# Objetivo: Acompanhar o consumo calórico de 3 pacientes ao longo de 4 refeições principais, validando limites e elegendo a refeição mais calórica.

# Passo 1: Inicialização da matriz 3x4 de consumo e status
consumo = [
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0]
]
cadastrado = False
limite_diario = 2000.0
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- SISTEMA DE NUTRIÇÃO - CALORIAS DIÁRIAS ---")
    print("1. Cadastrar Consumos e Limite Diário")
    print("2. Gerar Relatório de Pacientes (Metas de Dieta)")
    print("3. Identificar Refeição Mais Calórica Geral")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema de nutrição encerrado.")
        
    elif opcao == 1:
        # Passo 3: Cadastrar consumos de calorias por refeição/paciente (validação > 0)
        print("\n--- Cadastro de Consumos ---")
        
        lim_valido = False
        while not lim_valido:
            limite_diario = input("Digite o limite calórico diário recomendado (kcal): ")
            limite_diario = float(limite_diario)
            if limite_diario > 0.0:
                lim_valido = True
            else:
                print("Erro: O limite calórico deve ser maior que zero.")
                
        refeicoes_nome = ["Café da Manhã", "Almoço", "Café da Tarde", "Jantar"]
        for i in range(3):
            print(f"Paciente {i+1}:")
            for j in range(4):
                valido = False
                while not valido:
                    kcal = input(f"  Calorias da refeição '{refeicoes_nome[j]}' (kcal): ")
                    kcal = float(kcal)
                    if kcal > 0.0:
                        consumo[i][j] = kcal
                        valido = True
                    else:
                        print("  Erro: As calorias devem ser um valor maior que zero.")
        cadastrado = True
        print("Registros calóricos salvos com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Somar consumo total de cada paciente e comparar com o limite
        if not cadastrado:
            print("Erro: Cadastre os consumos primeiro (Opção 1).")
        else:
            print(f"\n--- RELATÓRIO DE PACIENTES (Limite Recomendado: {limite_diario:.0f} kcal) ---")
            for i in range(3):
                soma_paciente = 0.0
                for j in range(4):
                    soma_paciente = soma_paciente + consumo[i][j]
                    
                if soma_paciente <= limite_diario:
                    status = "Dieta OK"
                else:
                    status = "Excesso de Calorias!"
                    
                print(f"Paciente {i+1} - Consumo Total: {soma_paciente:.1f} kcal | Status: {status}")
                
    elif opcao == 3:
        # Passo 5: Identificar qual foi a refeição mais calórica na média (coluna com maior soma)
        if not cadastrado:
            print("Erro: Cadastre os consumos primeiro (Opção 1).")
        else:
            print("\n--- ANÁLISE DE REFEIÇÃO MAIS CALÓRICA (Média Geral) ---")
            refeicoes_nome = ["Café da Manhã", "Almoço", "Café da Tarde", "Jantar"]
            
            maior_soma_coluna = -1.0
            coluna_mais_calorica = -1
            
            for j in range(4):
                soma_coluna = 0.0
                for i in range(3):
                    soma_coluna = soma_coluna + consumo[i][j]
                
                media_refeicao = soma_coluna / 3.0
                print(f"Refeição '{refeicoes_nome[j]}' - Consumo Médio Geral: {media_refeicao:.1f} kcal")
                
                if soma_coluna > maior_soma_coluna:
                    maior_soma_coluna = soma_coluna
                    coluna_mais_calorica = j
                    
            print(f"\nA refeição mais calórica na média é '{refeicoes_nome[coluna_mais_calorica]}' com consumo médio de {maior_soma_coluna/3.0:.1f} kcal.")
    else:
        print("Erro: Opção inválida.")
