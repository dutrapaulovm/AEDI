# Exercício 29: Autômato Finito Determinístico (Matriz de Transição de Estados)
# Objetivo: Representar a tabela de transição de um DFA para reconhecer a subseqüência '01' em cadeias de 5 bits, validando se atinge o estado de aceitação.

# Passo 1: Inicialização da matriz de transição de estados
# Estados: 0 (Início/Padrão), 1 (Leu '0'), 2 (Leu '01' - ACEITAÇÃO)
# Símbolos: Coluna 0 indica transição para entrada '0', Coluna 1 indica transição para entrada '1'
transicao = [
    [1, 0],  # Estado 0: se entra 0 -> vai para E1, se entra 1 -> fica em E0
    [1, 2],  # Estado 1: se entra 0 -> fica em E1, se entra 1 -> vai para E2 (Aceitou!)
    [1, 0]   # Estado 2 (Aceitação): se entra 0 -> volta para E1, se entra 1 -> volta para E0
]
estado_aceitacao = 2
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- TEORIA DA COMPUTAÇÃO - SIMULADOR DFA DE CADEIA '01' ---")
    print("1. Testar Cadeia de 5 Bits")
    print("2. Visualizar Tabela de Transição do Autômato")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Simulador de autômato encerrado.")
        
    elif opcao == 1:
        # Passo 3: Receber sequência de 5 bits com validação
        print("\n--- Testador de Cadeia de 5 Bits ---")
        cadeia = []
        for i in range(5):
            valido = False
            while not valido:
                bit = input(f"Digite o bit da posição {i+1} (0 ou 1): ")
                bit = int(bit)
                if bit == 0 or bit == 1:
                    cadeia.append(bit)
                    valido = True
                else:
                    print("  Erro: Apenas os bits 0 ou 1 são válidos.")
                    
        # Passo 4: Percorrer a matriz de estados com base na cadeia de entrada
        print(f"\nIniciando Processamento da cadeia: {cadeia}")
        estado_atual = 0  # Estado inicial
        
        for i in range(5):
            simbolo = cadeia[i]
            estado_anterior = estado_atual
            
            # Transição: estado_atual = transicao[estado_atual][simbolo]
            estado_atual = transicao[estado_atual][simbolo]
            print(f"  Passo {i+1} : Leu {simbolo} | Transição: Estado {estado_anterior} -> Estado {estado_atual}")
            
        # Passo 5: Verificação se o estado final é de aceitação
        print(f"\nEstado Final do Autômato: Estado {estado_atual}")
        if estado_atual == estado_aceitacao:
            print(">>> RESULTADO: CADEIA ACEITA! Padrão '01' localizado e finalizado com sucesso.")
        else:
            print(">>> RESULTADO: CADEIA REJEITADA! A sequência não terminou no padrão esperado.")
            
    elif opcao == 2:
        # Exibição gráfica da matriz de transição
        print("\n--- TABELA DE TRANSIÇÃO DO DFA ---")
        print(" Estado Atual | Entrada: 0  | Entrada: 1  | Tipo de Estado")
        print("--------------|-------------|-------------|----------------")
        print("   Estado 0   |  Estado 1   |  Estado 0   | Início / Busca")
        print("   Estado 1   |  Estado 1   |  Estado 2   | '0' detectado")
        print("   Estado 2   |  Estado 1   |  Estado 0   | ACEITAÇÃO ('01')")
        print("-----------------------------------------------------------")
    else:
        print("Erro: Opção inválida.")
