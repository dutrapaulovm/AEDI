# Exercício 13: Torneio de E-sports (Matriz 4x3)
# Objetivo: Organizar e analisar pontuações de 4 equipes em 3 partidas, elegendo o campeão, aplicando bônus de 1.1x para quem superar 500 pontos, e localizando a melhor partida individual.

# Passo 1: Inicialização da matriz 4x3 com zeros e status de pontuação
pontuacoes = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
cadastrado = False
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- CAMPEONATO DE E-SPORTS (4x3) ---")
    print("1. Inserir Pontos das Equipes")
    print("2. Ranking Final e Análise de Desempenho")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema do torneio encerrado.")
        
    elif opcao == 1:
        # Passo 3: Inserir pontos das partidas (validação > 0)
        print("\n--- Inserção de Pontuações ---")
        for i in range(4):
            print(f"Equipe {i+1}:")
            for j in range(3):
                valido = False
                while not valido:
                    pontos = input(f"  Pontos na Partida {j+1}: ")
                    pontos = int(pontos)
                    if pontos >= 0:
                        pontuacoes[i][j] = pontos
                        valido = True
                    else:
                        print("  Erro: Os pontos devem ser não negativos.")
        cadastrado = True
        print("Pontuações inseridas com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Ranking Final com soma, aplicação do Bônus de Vitória (1.1x) e busca do maior ponto individual
        if not cadastrado:
            print("Erro: Insira as pontuações primeiro (Opção 1).")
        else:
            print("\n--- RANKING FINAL E ESTATÍSTICAS ---")
            maior_partida_pontos = -1
            maior_partida_equipe = -1
            maior_partida_num = -1
            
            # Vetor para armazenar as pontuações finais (soma) das 4 equipes para ordenação ou exibição
            pontos_totais = [0.0] * 4
            
            # Cálculo de somas totais por equipe e melhor partida
            for i in range(4):
                soma_equipe = 0
                for j in range(3):
                    pts = pontuacoes[i][j]
                    soma_equipe = soma_equipe + pts
                    
                    # Verifica a maior pontuação em uma única partida
                    if pts > maior_partida_pontos:
                        maior_partida_pontos = pts
                        maior_partida_equipe = i + 1
                        maior_partida_num = j + 1
                        
                # Passo 5: Aplicação de Bônus de Vitória (1.1x se total > 500)
                if soma_equipe > 500:
                    pontos_totais[i] = soma_equipe * 1.1
                    bonus_texto = "(Bônus 1.1x Aplicado!)"
                else:
                    pontos_totais[i] = float(soma_equipe)
                    bonus_texto = ""
                    
                print(f"Equipe {i+1} - Pontos Originais: {soma_equipe} | Pontuação Final: {pontos_totais[i]:.1f} {bonus_texto}")
                
            # Identificação da equipe campeã
            campeao_pontos = pontos_totais[0]
            campeao_num = 1
            for i in range(1, 4):
                if pontos_totais[i] > campeao_pontos:
                    campeao_pontos = pontos_totais[i]
                    campeao_num = i + 1
                    
            print(f"\nEquipe Campeã: Equipe {campeao_num} com {campeao_pontos:.1f} pontos!")
            print(f"Maior pontuação individual em uma partida: Equipe {maior_partida_equipe} fez {maior_partida_pontos} pontos na Partida {maior_partida_num}.")
    else:
        print("Erro: Opção inválida.")
