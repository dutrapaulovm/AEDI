# Exercício 25: Detecção de Erros por Bit de Paridade (Matriz 4x4)
# Objetivo: Organizar 16 bits em um grid 4x4, calcular o bit de paridade par para cada linha, e verificar a integridade da transmissão.

# Passo 1: Inicialização da matriz de dados 4x4 e vetor de paridade
dados = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
paridade_original = [0] * 4
cadastrado = False
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- SISTEMA TRANSMISSOR DE DADOS - PARIDADE PAR (4x4) ---")
    print("1. Cadastrar Sequência de Bits e Gerar Paridade")
    print("2. Verificar Integridade dos Dados (Íntegra vs Corrompida)")
    print("3. Simular Ruído (Inverter um Bit da Matriz)")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema de paridade encerrado.")
        
    elif opcao == 1:
        # Passo 3: Cadastrar bits (apenas 0 ou 1)
        print("\n--- Cadastro de Mensagem de 16 Bits ---")
        for i in range(4):
            print(f"Linha {i+1} de bits:")
            for j in range(4):
                valido = False
                while not valido:
                    bit = input(f"  Bit [{i+1}][{j+1}]: ")
                    bit = int(bit)
                    if bit == 0 or bit == 1:
                        dados[i][j] = bit
                        valido = True
                    else:
                        print("  Erro: Insira apenas 0 ou 1.")
                        
        # Passo 4: Calcular o bit de paridade par por linha
        # Se a soma dos bits na linha for ímpar, o bit de paridade é 1. Se for par, o bit é 0.
        for i in range(4):
            soma_linha = 0
            for j in range(4):
                soma_linha = soma_linha + dados[i][j]
            # Se resto por 2 for diferente de zero, a paridade é 1, senão 0
            paridade_original[i] = soma_linha % 2
            
        cadastrado = True
        print("\nParidade de linha gerada com sucesso!")
        print(f"Vetor de Paridade Gravado: {paridade_original}")
        
    elif opcao == 2:
        # Passo 5: Comparar a paridade recalculada com o vetor original gravado
        if not cadastrado:
            print("Erro: Cadastre os dados primeiro (Opção 1).")
        else:
            print("\n--- Verificação de Integridade de Transmissão ---")
            corrompido = False
            
            # Recalcula a paridade atual da matriz
            for i in range(4):
                soma_atual = 0
                for j in range(4):
                    soma_atual = soma_atual + dados[i][j]
                paridade_atual = soma_atual % 2
                
                # Se a paridade atual diferir da original gravada, houve corrupção
                if paridade_atual != paridade_original[i]:
                    print(f"  [ALERTA] Divergência na Linha {i+1}: Original={paridade_original[i]}, Atual={paridade_atual}")
                    corrompido = True
                    
            if corrompido:
                print("\nResultado: MENSAGEM CORROMPIDA! Divergência de paridade de linha detectada.")
            else:
                print("\nResultado: MENSAGEM ÍNTEGRA! Nenhum erro de bit detectado nas linhas.")
                
    elif opcao == 3:
        # Passo 6: Inverter um bit específico para simular ruído/erro de canal
        if not cadastrado:
            print("Erro: Cadastre os dados primeiro (Opção 1).")
        else:
            print("\n--- Simulação de Inserção de Ruído ---")
            # Seleciona as coordenadas a corromper
            l_valido = False
            while not l_valido:
                l_idx = input("Selecione a linha a alterar (1 a 4): ")
                l_idx = int(l_idx)
                if 1 <= l_idx <= 4:
                    l_idx = l_idx - 1
                    l_valido = True
                else:
                    print("Erro: Linha inválida.")
                    
            c_valido = False
            while not c_valido:
                c_idx = input("Selecione a coluna a alterar (1 a 4): ")
                c_idx = int(c_idx)
                if 1 <= c_idx <= 4:
                    c_idx = c_idx - 1
                    c_valido = True
                else:
                    print("Erro: Coluna inválida.")
                    
            # Inverte o bit (0 vira 1, 1 vira 0)
            bit_original = dados[l_idx][c_idx]
            if bit_original == 1:
                dados[l_idx][c_idx] = 0
            else:
                dados[l_idx][c_idx] = 1
                
            print(f"\nSucesso: Ruído simulado! O bit na posição [{l_idx+1}][{c_idx+1}] foi invertido de {bit_original} para {dados[l_idx][c_idx]}.")
    else:
        print("Erro: Opção inválida.")
