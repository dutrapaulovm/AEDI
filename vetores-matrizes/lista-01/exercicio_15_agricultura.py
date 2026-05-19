# Exercício 15: Agricultura Inteligente (Matriz 4x4)
# Objetivo: Controlar percentuais de umidade em um grid 4x4 de sensores, sugerindo coordenadas de irrigação para áreas secas (< 30%) e calculando médias dos 4 quadrantes.

# Passo 1: Inicialização da matriz do solo com zeros
solo = [
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0]
]
cadastrado = False
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- SISTEMA AGRICULTURA INTELIGENTE (4x4) ---")
    print("1. Cadastrar Leitura de Umidade dos Sensores")
    print("2. Mapa de Irrigação (Áreas Secas < 30%)")
    print("3. Analisar Médias por Quadrante")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema agrícola inteligente encerrado.")
        
    elif opcao == 1:
        # Passo 3: Cadastrar e validar umidade (deve ser entre 0 e 100)
        print("\n--- Cadastro de Leitura de Sensores ---")
        for i in range(4):
            print(f"Linha {i+1} do solo:")
            for j in range(4):
                valido = False
                while not valido:
                    umidade = input(f"  Umidade do Sensor [{i+1}][{j+1}] (%): ")
                    umidade = float(umidade)
                    if 0.0 <= umidade <= 100.0:
                        solo[i][j] = umidade
                        valido = True
                    else:
                        print("  Erro: O percentual de umidade deve estar entre 0.0 e 100.0. Digite novamente.")
        cadastrado = True
        print("Registros de umidade salvos!")
        
    elif opcao == 2:
        # Passo 4: Identificar áreas secas (< 30%) e sugerir irrigação nas coordenadas exatas
        if not cadastrado:
            print("Erro: Faça o cadastro das umidades primeiro (Opção 1).")
        else:
            print("\n--- MAPA DE NECESSIDADE DE IRRIGAÇÃO ---")
            necessita_irrigar = False
            
            for i in range(4):
                linha_status = ""
                for j in range(4):
                    if solo[i][j] < 30.0:
                        linha_status = linha_status + f"[SECO: {solo[i][j]:.1f}%] "
                        necessita_irrigar = True
                    else:
                        linha_status = linha_status + f"[ OK : {solo[i][j]:.1f}%] "
                print(f"Linha {i+1}: {linha_status}")
                
            if necessita_irrigar:
                print("\nSugestões de Ativação de Irrigação (Coordenadas recomendadas):")
                for i in range(4):
                    for j in range(4):
                        if solo[i][j] < 30.0:
                            print(f"  -> Ativar bico na coordenada Linha {i+1}, Coluna {j+1}")
            else:
                print("\nSolo perfeitamente umedecido. Nenhuma irrigação necessária.")
                
    elif opcao == 3:
        # Passo 5: Cálculo da umidade média de cada um dos 4 quadrantes da matriz 4x4
        if not cadastrado:
            print("Erro: Faça o cadastro das umidades primeiro (Opção 1).")
        else:
            print("\n--- ANÁLISE DE UMIDADE POR QUADRANTE ---")
            
            # Quadrante 1 (Noroeste): Linhas 0-1, Colunas 0-1
            q1_soma = solo[0][0] + solo[0][1] + solo[1][0] + solo[1][1]
            q1_media = q1_soma / 4.0
            
            # Quadrante 2 (Nordeste): Linhas 0-1, Colunas 2-3
            q2_soma = solo[0][2] + solo[0][3] + solo[1][2] + solo[1][3]
            q2_media = q2_soma / 4.0
            
            # Quadrante 3 (Sudoeste): Linhas 2-3, Colunas 0-1
            q3_soma = solo[2][0] + solo[2][1] + solo[3][0] + solo[3][1]
            q3_media = q3_soma / 4.0
            
            # Quadrante 4 (Sudeste): Linhas 2-3, Colunas 2-3
            q4_soma = solo[2][2] + solo[2][3] + solo[3][2] + solo[3][3]
            q4_media = q4_soma / 4.0
            
            print(f"Quadrante 1 (Superior-Esquerdo): Média de {q1_media:.1f}%")
            print(f"Quadrante 2 (Superior-Direito):  Média de {q2_media:.1f}%")
            print(f"Quadrante 3 (Inferior-Esquerdo): Média de {q3_media:.1f}%")
            print(f"Quadrante 4 (Inferior-Direito):  Média de {q4_media:.1f}%")
    else:
        print("Erro: Opção inválida.")
