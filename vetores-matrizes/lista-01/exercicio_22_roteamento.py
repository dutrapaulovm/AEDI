# Exercício 22: Tabela de Roteamento de Roteadores (Matriz 4x4)
# Objetivo: Representar latências entre 4 roteadores, identificando o roteador com melhor tempo médio de entrega e permitindo atualizações de rotas específicas.

# Passo 1: Inicialização da matriz 4x4 com zeros e status de cadastro
rede = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
cadastrado = False
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- GESTÃO DE ROTEAMENTO DE REDE (MATRIZ 4x4) ---")
    print("1. Cadastrar Tabela de Latência de Rede")
    print("2. Analisar Roteador com Melhor Latência Média")
    print("3. Atualizar Latência de uma Rota")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Tabela de roteamento encerrada.")
        
    elif opcao == 1:
        # Passo 3: Inserir custos de latência (validação: positivo, diagonal = 0)
        print("\n--- Cadastro de Latências (em milissegundos) ---")
        for i in range(4):
            print(f"Origem: Roteador {i+1}:")
            for j in range(4):
                if i == j:
                    rede[i][j] = 0  # Latência de um roteador para ele mesmo é 0
                    print(f"  Para Roteador {j+1}: 0 ms (Automático - si mesmo)")
                else:
                    valido = False
                    while not valido:
                        lat = input(f"  Para Roteador {j+1}: ")
                        lat = int(lat)
                        if lat > 0:
                            rede[i][j] = lat
                            valido = True
                        else:
                            print("    Erro: A latência deve ser estritamente positiva.")
        cadastrado = True
        print("Tabela de latência cadastrada com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Encontrar qual roteador possui a menor latência média (ignorando diagonal de zeros)
        if not cadastrado:
            print("Erro: Cadastre as latências primeiro (Opção 1).")
        else:
            print("\n--- ANÁLISE DE ROTAS E LATÊNCIAS MÉDIAS ---")
            melhor_roteador_num = -1
            melhor_media_latencia = 999999.0
            
            for i in range(4):
                soma_latencia = 0
                cont_conexoes = 0
                for j in range(4):
                    if i != j:  # Ignora si mesmo (conexão com latência 0)
                        soma_latencia = soma_latencia + rede[i][j]
                        cont_conexoes = cont_conexoes + 1
                        
                media_lat = soma_latencia / float(cont_conexoes)
                print(f"  Roteador {i+1} - Latência Média para os outros: {media_lat:.1f} ms")
                
                if media_lat < melhor_media_latencia:
                    melhor_media_latencia = media_lat
                    melhor_roteador_num = i + 1
                    
            print(f"\nO Roteador com menor latência média é o Roteador {melhor_roteador_num} ({melhor_media_latencia:.1f} ms).")
            
    elif opcao == 3:
        # Passo 5: Atualizar latência por rota individual
        if not cadastrado:
            print("Erro: Cadastre as latências primeiro (Opção 1).")
        else:
            print("\n--- Atualização de Rota Individual ---")
            
            # Validação do roteador de origem (1 a 4)
            orig_valida = False
            while not orig_valida:
                origem = input("Digite o Roteador de Origem (1 a 4): ")
                origem = int(origem)
                if 1 <= origem <= 4:
                    origem_idx = origem - 1
                    orig_valida = True
                else:
                    print("Erro: Origem inválida.")
                    
            # Validação do roteador de destino (1 a 4)
            dest_valido = False
            while not dest_valido:
                destino = input("Digite o Roteador de Destino (1 a 4): ")
                destino = int(destino)
                if 1 <= destino <= 4:
                    destino_idx = destino - 1
                    dest_valido = True
                else:
                    print("Erro: Destino inválido.")
                    
            if origem_idx == destino_idx:
                print("Erro: Não é permitido atualizar a latência para si mesmo (sempre 0 ms).")
            else:
                # Leitura da nova latência
                valido = False
                while not valido:
                    nova_lat = input(f"Digite a nova latência de R{origem} para R{destino} (ms): ")
                    nova_lat = int(nova_lat)
                    if nova_lat > 0:
                        rede[origem_idx][destino_idx] = nova_lat
                        valido = True
                        print("Rota de rede atualizada com sucesso!")
                    else:
                        print("Erro: A latência deve ser positiva.")
    else:
        print("Erro: Opção inválida.")
