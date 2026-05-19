# Exercício 19: Mapeamento de Obstáculos para Robô Aspirador (Matriz 5x5)
# Objetivo: Cadastrar o mapa (0: Piso, 1: Obstáculo, 2: Tapete) em um grid 5x5, contar obstáculos, e identificar se o robô ficaria preso (piso rodeado por 4 obstáculos).

# Passo 1: Inicialização da matriz 5x5 e status
grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
cadastrado = False
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- MAPEADOR DE ROBÓTICA E TERRENO (5x5) ---")
    print("1. Cadastrar/Resetar Mapa de Terreno")
    print("2. Exibir Estatísticas do Mapa (Contar Obstáculos)")
    print("3. Analisar Se Robô Ficaria Preso (Armadilhas)")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Mapeador de robótica encerrado.")
        
    elif opcao == 1:
        # Passo 3: Preencher a matriz com validações (apenas 0, 1 ou 2 são aceitos)
        print("\n--- Cadastro do Terreno (0: Piso, 1: Obstáculo, 2: Tapete) ---")
        for i in range(5):
            print(f"Linha {i+1} do Grid:")
            for j in range(5):
                valido = False
                while not valido:
                    celula = input(f"  Célula [{i+1}][{j+1}]: ")
                    celula = int(celula)
                    if celula == 0 or celula == 1 or celula == 2:
                        grid[i][j] = celula
                        valido = True
                    else:
                        print("  Erro: Apenas os valores 0 (Piso), 1 (Obstáculo) ou 2 (Tapete) são válidos.")
        cadastrado = True
        print("Mapa de terreno configurado!")
        
    elif opcao == 2:
        # Passo 4: Contar obstáculos (1)
        if not cadastrado:
            print("Erro: Cadastre o mapa de terreno primeiro (Opção 1).")
        else:
            print("\n--- MAPA DE TERRENO ATUAL ---")
            total_obstaculos = 0
            total_pisos = 0
            total_tapetes = 0
            
            for i in range(5):
                linha_txt = ""
                for j in range(5):
                    if grid[i][j] == 0:
                        linha_txt = linha_txt + " . "  # Piso
                        total_pisos = total_pisos + 1
                    elif grid[i][j] == 1:
                        linha_txt = linha_txt + " # "  # Obstáculo
                        total_obstaculos = total_obstaculos + 1
                    else:
                        linha_txt = linha_txt + " ~ "  # Tapete
                        total_tapetes = total_tapetes + 1
                print(linha_txt)
                
            print(f"\nEstatísticas:")
            print(f"  Pisos Livres (.): {total_pisos}")
            print(f"  Obstáculos (#):  {total_obstaculos}")
            print(f"  Tapetes (~):     {total_tapetes}")
            
    elif opcao == 3:
        # Passo 5: Laço aninhado para identificar pisos (0) cercados por 4 obstáculos (1)
        if not cadastrado:
            print("Erro: Cadastre o mapa de terreno primeiro (Opção 1).")
        else:
            print("\n--- ANÁLISE DE ROTAS BLOQUEADAS (ARMADILHAS) ---")
            armadilha_detectada = False
            
            # Percorre apenas as células internas (linha 1 a 3, coluna 1 a 3), onde há vizinhos nos 4 lados
            for i in range(1, 4):
                for j in range(1, 4):
                    # Verifica se a própria célula é piso (0) e as adjacentes são obstáculos (1)
                    if grid[i][j] == 0:
                        cima = grid[i-1][j]
                        baixo = grid[i+1][j]
                        esquerda = grid[i][j-1]
                        direita = grid[i][j+1]
                        
                        if cima == 1 and baixo == 1 and esquerda == 1 and direita == 1:
                            print(f"  [ARMADILHA] O robô ficaria preso na coordenada Linha {i+1}, Coluna {j+1}!")
                            armadilha_detectada = True
                            
            if not armadilha_detectada:
                print("Nenhuma coordenada de risco (piso livre cercado por 4 obstáculos) encontrada.")
    else:
        print("Erro: Opção inválida.")
