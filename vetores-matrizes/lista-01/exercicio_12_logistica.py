# Exercício 12: Logística de Cargas Terrestres (Matriz 3x3)
# Objetivo: Gerenciar a carga em toneladas de 3 caminhões em 3 rotas distintas, controlando sobrecarga de 10t por caminhão e 25t acumuladas por rota.

# Passo 1: Inicialização da matriz logistica 3x3 com zeros e status de carga
logistica = [
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0]
]
carregado = False
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- SISTEMA LOGÍSTICO DE TRANSPORTE (3x3) ---")
    print("1. Lançar Carga dos Caminhões nas Rotas")
    print("2. Relatório de Sobrecarga e Rotas")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema logístico encerrado.")
        
    elif opcao == 1:
        # Passo 3: Preenchimento da matriz com validação (> 0 e <= 10.0 toneladas)
        print("\n--- Carregamento da Matriz de Logística ---")
        for i in range(3):
            print(f"Caminhão {i+1}:")
            for j in range(3):
                valido = False
                while not valido:
                    carga = input(f"  Carga para a Rota {j+1} (em toneladas): ")
                    carga = float(carga)
                    if 0.0 <= carga <= 10.0:
                        logistica[i][j] = carga
                        valido = True
                    else:
                        print("  Erro: A carga máxima de um caminhão em uma rota é 10.0 toneladas. Digite novamente.")
        carregado = True
        print("Cargas lançadas com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Cálculo da soma total por caminhão (linha) e por rota (coluna)
        if not carregado:
            print("Erro: Realize o carregamento primeiro (Opção 1).")
        else:
            print("\n--- RELATÓRIO DE SOBRECARGAS ---")
            
            # Soma por caminhão (linhas)
            print("Cargas Totais por Caminhão:")
            for i in range(3):
                soma_caminhao = 0.0
                for j in range(3):
                    soma_caminhao = soma_caminhao + logistica[i][j]
                print(f"  Caminhão {i+1}: {soma_caminhao:.2f} toneladas no total.")
                
            # Soma por rota (colunas) e verificação de sobrecarga acumulada da rota (> 25t)
            print("\nCargas Totais por Rota e Análise de Limite:")
            for j in range(3):
                soma_rota = 0.0
                for i in range(3):
                    soma_rota = soma_rota + logistica[i][j]
                    
                if soma_rota > 25.0:
                    status_rota = "SOBRECARGA DETECTADA!"
                else:
                    status_rota = "DENTRO DO LIMITE"
                    
                print(f"  Rota {j+1}: {soma_rota:.2f} t - Status: {status_rota}")
    else:
        print("Erro: Opção inválida.")
