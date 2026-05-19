# Exercício 7: Monitoramento Meteorológico (Matriz 3x2)
# Objetivo: Registrar temperaturas de 3 cidades em 2 horários, validando contra falhas de hardware, alertando geadas, e encontrando a temperatura máxima.

# Passo 1: Inicialização da matriz 3x2 e status
temp = [
    [0.0, 0.0],
    [0.0, 0.0],
    [0.0, 0.0]
]
cadastrado = False
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- SISTEMA METEOROLÓGICO (MATRIZ 3x2) ---")
    print("1. Cadastrar Temperaturas")
    print("2. Consultar Relatório e Alertas")
    print("3. Atualizar Temperatura Específica")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema meteorológico encerrado.")
        
    elif opcao == 1:
        # Passo 3: Cadastro inicial com validação de limites físicos (-50°C a 60°C)
        print("\n--- Cadastro de Temperaturas (Períodos: 1-Manhã, 2-Tarde) ---")
        for i in range(3):
            print(f"Cidade {i+1}:")
            for j in range(2):
                valido = False
                while not valido:
                    t_val = input(f"  Digite a temperatura do Período {j+1} (em °C): ")
                    t_val = float(t_val)
                    if -50.0 <= t_val <= 60.0:
                        temp[i][j] = t_val
                        valido = True
                    else:
                        print("  Erro de hardware: Temperaturas fora do intervalo [-50°C, 60°C]. Tente novamente.")
        cadastrado = True
        print("Temperaturas salvas com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Geração de relatórios, médias de cidade, alertas de geada e temperatura máxima geral
        if not cadastrado:
            print("Erro: Cadastre as temperaturas primeiro (Opção 1).")
        else:
            print("\n--- RELATÓRIO DE TEMPERATURAS ---")
            maxima_geral = temp[0][0]
            
            for i in range(3):
                soma = 0.0
                for j in range(2):
                    soma = soma + temp[i][j]
                    if temp[i][j] > maxima_geral:
                        maxima_geral = temp[i][j]
                        
                media_cidade = soma / 2.0
                print(f"Cidade {i+1} - Manhã: {temp[i][0]}°C | Tarde: {temp[i][1]}°C | Média: {media_cidade:.2f}°C")
                
                # Alerta Risco de Geada: se a temperatura da manhã for < 0
                if temp[i][0] < 0.0:
                    print("  [ALERT] Cidade com Risco de Geada! Temperatura matinal abaixo de 0°C.")
                    
            print(f"\nMaior temperatura registrada no sistema: {maxima_geral:.2f}°C")
            
    elif opcao == 3:
        # Passo 5: Atualização de uma coordenada específica informando índices
        if not cadastrado:
            print("Erro: Cadastre as temperaturas primeiro (Opção 1).")
        else:
            print("\n--- Atualização de Registro ---")
            
            # Validação do índice da cidade (1 a 3)
            cidade_valida = False
            while not cidade_valida:
                c_idx = input("Digite o número da cidade (1 a 3): ")
                c_idx = int(c_idx)
                if 1 <= c_idx <= 3:
                    c_idx = c_idx - 1
                    cidade_valida = True
                else:
                    print("Erro: Cidade inválida. Escolha 1, 2 ou 3.")
                    
            # Validação do período (1-Manhã, 2-Tarde)
            periodo_valido = False
            while not periodo_valido:
                p_idx = input("Digite o período (1 para Manhã ou 2 para Tarde): ")
                p_idx = int(p_idx)
                if 1 <= p_idx <= 2:
                    p_idx = p_idx - 1
                    periodo_valido = True
                else:
                    print("Erro: Período inválido. Escolha 1 ou 2.")
                    
            # Leitura e validação da nova temperatura
            valido = False
            while not valido:
                t_nova = input("Digite a nova temperatura (em °C): ")
                t_nova = float(t_nova)
                if -50.0 <= t_nova <= 60.0:
                    temp[c_idx][p_idx] = t_nova
                    valido = True
                    print("Temperatura atualizada com sucesso!")
                else:
                    print("Erro de hardware: Temperaturas fora do intervalo [-50°C, 60°C]. Tente novamente.")
    else:
        print("Erro: Opção inválida.")
