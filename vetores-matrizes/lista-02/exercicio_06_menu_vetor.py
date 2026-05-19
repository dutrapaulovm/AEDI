# Exercício 6: Menu Interativo de Manipulação de Vetor
# Objetivo: Criar um menu interativo para inserir valores em posições de um vetor de tamanho 5 (inicialmente zerado) e exibir seu estado atual.

# Passo 1: Inicialização do vetor com 5 zeros
vetor = [0.0] * 5
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- MENU DE MANIPULAÇÃO DE VETOR ---")
    print("1. Inserir Valor em Posição")
    print("2. Mostrar Estado Atual do Vetor")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    opcao = int(opcao)
    
    if opcao == 3:
        rodando = False
        print("Saindo do gerenciador de vetor.")
        
    elif opcao == 1:
        # Passo 3: Inserção de valor em índice validado (0 a 4)
        print("\n--- Inserção de Elemento ---")
        idx_valido = False
        indice = -1
        while not idx_valido:
            indice = input("Digite o índice da posição a atualizar (0 a 4): ")
            indice = int(indice)
            if 0 <= indice <= 4:
                idx_valido = True
            else:
                print("Erro: O índice deve estar no intervalo de 0 a 4.")
                
        valor = input(f"Digite o novo valor para a posição {indice}: ")
        valor = float(valor)
        
        vetor[indice] = valor
        print(f"Sucesso: Posição {indice} atualizada com {valor}!")
        
    elif opcao == 2:
        # Passo 4: Exibição do vetor
        print("\n--- ESTADO ATUAL DO VETOR ---")
        print(f"Vetor: {vetor}")
        for i in range(5):
            print(f"  Posição [{i}]: {vetor[i]}")
    else:
        print("Erro: Opção inválida.")
