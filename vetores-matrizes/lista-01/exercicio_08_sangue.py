# Exercício 8: Banco de Sangue Multinível (Matriz 2x4)
# Objetivo: Controlar estoque de 4 tipos sanguíneos (A, B, AB, O) em 2 hospitais, listando alertas de estoque crítico e calculando o total do tipo O.

# Passo 1: Inicialização do estoque 2x4 (linhas: Hospitais, colunas: tipos A=0, B=1, AB=2, O=3)
estoque = [
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
cadastrado = False
limite_critico = 10
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- SISTEMA DE BANCO DE SANGUE (2x4) ---")
    print("1. Cadastrar/Reabastecer Estoque Inicial")
    print("2. Gerar Relatório de Alerta Crítico")
    print("3. Visualizar Total de Bolsas Tipo O")
    print("4. Registrar Entrada de Remessa")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema do banco de sangue encerrado.")
        
    elif opcao == 1:
        # Passo 3: Cadastro inicial de bolsas (rejeita negativos)
        print("\n--- Abastecimento do Banco de Sangue ---")
        # Define o limite crítico
        limite_critico = input("Digite o limite mínimo (crítico) para alertas: ")
        limite_critico = int(limite_critico)
        
        tipos_nome = ["A", "B", "AB", "O"]
        for i in range(2):
            print(f"Hospital {i+1}:")
            for j in range(4):
                valido = False
                while not valido:
                    qtd = input(f"  Quantidade de bolsas do tipo {tipos_nome[j]}: ")
                    qtd = int(qtd)
                    if qtd >= 0:
                        estoque[i][j] = qtd
                        valido = True
                    else:
                        print("  Erro: Quantidade de bolsas não pode ser negativa.")
        cadastrado = True
        print("Estoque de bolsas de sangue cadastrado!")
        
    elif opcao == 2:
        # Passo 4: Listar quais hospitais estão abaixo do limite crítico para cada tipo
        if not cadastrado:
            print("Erro: Cadastre o estoque inicial primeiro (Opção 1).")
        else:
            print(f"\n--- ALERTA DE ESTOQUE CRÍTICO (Limite: {limite_critico} bolsas) ---")
            tipos_nome = ["A", "B", "AB", "O"]
            alerta_gerado = False
            
            for j in range(4):
                for i in range(2):
                    if estoque[i][j] < limite_critico:
                        print(f"  [CRÍTICO] Hospital {i+1} está com estoque baixo do tipo {tipos_nome[j]}: {estoque[i][j]} bolsas.")
                        alerta_gerado = True
            if not alerta_gerado:
                print("Todos os estoques estão operando acima do limite crítico.")
                
    elif opcao == 3:
        # Passo 5: Cálculo do total de bolsas do tipo O (índice 3 da matriz)
        if not cadastrado:
            print("Erro: Cadastre o estoque inicial primeiro (Opção 1).")
        else:
            total_tipo_o = estoque[0][3] + estoque[1][3]
            print(f"\n--- CONTROLE TIPO O ---")
            print(f"Hospital 1 (Tipo O): {estoque[0][3]} bolsas")
            print(f"Hospital 2 (Tipo O): {estoque[1][3]} bolsas")
            print(f"Total de bolsas do tipo O na rede: {total_tipo_o} bolsas")
            
    elif opcao == 4:
        # Passo 6: Registrar entrada/reabastecimento de remessa recebida
        if not cadastrado:
            print("Erro: Cadastre o estoque inicial primeiro (Opção 1).")
        else:
            print("\n--- Entrada de Remessa de Sangue ---")
            # Validação do hospital
            h_valido = False
            while not h_valido:
                h_idx = input("Digite o Hospital destinatário (1 ou 2): ")
                h_idx = int(h_idx)
                if 1 <= h_idx <= 2:
                    h_idx = h_idx - 1
                    h_valido = True
                else:
                    print("Erro: Hospital inválido.")
                    
            # Seleção do tipo sanguíneo (A=1, B=2, AB=3, O=4)
            t_valido = False
            tipos_nome = ["A", "B", "AB", "O"]
            while not t_valido:
                print("Tipos: 1-A, 2-B, 3-AB, 4-O")
                t_idx = input("Escolha o tipo sanguíneo (1 a 4): ")
                t_idx = int(t_idx)
                if 1 <= t_idx <= 4:
                    t_idx = t_idx - 1
                    t_valido = True
                else:
                    print("Erro: Opção inválida.")
                    
            # Quantidade a receber
            qtd_valido = False
            while not qtd_valido:
                qtd_remessa = input(f"Digite a quantidade de bolsas de tipo {tipos_nome[t_idx]} recebida: ")
                qtd_remessa = int(qtd_remessa)
                if qtd_remessa > 0:
                    estoque[h_idx][t_idx] = estoque[h_idx][t_idx] + qtd_remessa
                    qtd_valido = True
                    print(f"Sucesso: {qtd_remessa} bolsas adicionadas ao Hospital {h_idx+1}.")
                else:
                    print("Erro: A quantidade deve ser positiva.")
    else:
        print("Erro: Opção inválida.")
