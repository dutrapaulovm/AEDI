# Exercício 21: Simulador de Alocação de Memória RAM (Vetor de 8 Posições)
# Objetivo: Controlar o estado de 8 blocos de memória (0: Livre, 1: Alocado), prevenindo fragmentação, validando índices de 0 a 7 e localizando a maior sequência contígua de blocos livres (buraco).

# Passo 1: Inicialização do vetor de memória com zeros
memoria = [0] * 8
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- SIMULADOR DE ALOCAÇÃO DE MEMÓRIA OS ---")
    print("1. Alocar Bloco de Memória")
    print("2. Liberar Bloco de Memória")
    print("3. Visualizar Mapa e Maior Buraco Contíguo")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Simulador de alocação de memória encerrado.")
        
    elif opcao == 1:
        # Passo 3: Alocação com validação de índice (0 a 7) e de fragmentação (já alocado)
        print("\n--- Alocação de Memória ---")
        idx_valido = False
        bloco_idx = -1
        while not idx_valido:
            bloco_idx = input("Digite o índice do bloco a alocar (0 a 7): ")
            bloco_idx = int(bloco_idx)
            if 0 <= bloco_idx <= 7:
                idx_valido = True
            else:
                print("Erro: O bloco deve estar no intervalo de 0 a 7.")
                
        if memoria[bloco_idx] == 1:
            print("Erro: Fragmentação detectada! O bloco já está alocado.")
        else:
            memoria[bloco_idx] = 1
            print(f"Sucesso: Bloco {bloco_idx} alocado com êxito!")
            
    elif opcao == 2:
        # Passo 4: Liberação de bloco com validação
        print("\n--- Liberação de Memória ---")
        idx_valido = False
        bloco_idx = -1
        while not idx_valido:
            bloco_idx = input("Digite o índice do bloco a liberar (0 a 7): ")
            bloco_idx = int(bloco_idx)
            if 0 <= bloco_idx <= 7:
                idx_valido = True
            else:
                print("Erro: O bloco deve estar no intervalo de 0 a 7.")
                
        if memoria[bloco_idx] == 0:
            print("Informação: O bloco já está livre.")
        else:
            memoria[bloco_idx] = 0
            print(f"Sucesso: Bloco {bloco_idx} liberado com êxito!")
            
    elif opcao == 3:
        # Passo 5: Visualizar mapa e calcular a maior sequência contígua de zeros (buraco) em laço aninhado/simples
        print("\n--- MAPA DE MEMÓRIA RAM ---")
        mapa_str = ""
        for i in range(8):
            mapa_str = mapa_str + f"| B{i}: {memoria[i]} "
        mapa_str = mapa_str + "|"
        print(mapa_str)
        
        # Cálculo do maior buraco de blocos livres contíguos (consecutivos 0s)
        maior_buraco = 0
        buraco_atual = 0
        
        for i in range(8):
            if memoria[i] == 0:
                buraco_atual = buraco_atual + 1
                if buraco_atual > maior_buraco:
                    maior_buraco = buraco_atual
            else:
                buraco_atual = 0
                
        print(f"\nMaior buraco contíguo livre: {maior_buraco} blocos de memória.")
    else:
        print("Erro: Opção inválida.")
