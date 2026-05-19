# Exercício 3: Monitoramento de Crescimento Botânico (Vetor de 5 Posições)
# Objetivo: Acompanhar a altura de 5 plantas, calcular a diferença percentual em relação a uma referência e encontrar a planta mais alta com comparação de pares.

# Passo 1: Inicialização das variáveis
alturas = [0.0] * 5
inserido = False
referencia = 0.0
rodando = True

# Passo 2: Laço do menu interativo
while rodando:
    print("\n--- SISTEMA DE MONITORAMENTO BOTÂNICO ---")
    print("1. Inserir Alturas e Referência")
    print("2. Relatório de Crescimento")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema botânico encerrado.")
        
    elif opcao == 1:
        # Passo 3: Leitura das alturas com validação (> 0) e referência
        print("\n--- Inserção de Dados ---")
        ref_valido = False
        while not ref_valido:
            referencia = input("Digite a altura de referência (em cm): ")
            referencia = float(referencia)
            if referencia > 0.0:
                ref_valido = True
            else:
                print("Erro: A referência deve ser um valor maior que zero.")
                
        for i in range(5):
            valido = False
            while not valido:
                altura_planta = input(f"Digite a altura da planta {i+1} (em cm): ")
                altura_planta = float(altura_planta)
                if altura_planta > 0.0:
                    alturas[i] = altura_planta
                    valido = True
                else:
                    print("Erro: A altura deve ser maior que zero.")
        inserido = True
        print("Dados inseridos com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Relatório de crescimento percentual e localização da planta mais alta por pares
        if not inserido:
            print("Erro: Insira os dados primeiro (Opção 1).")
        else:
            print("\n--- RELATÓRIO DE CRESCIMENTO ---")
            print(f"Altura de Referência Esperada: {referencia:.2f} cm")
            
            # Mapeamento do crescimento percentual
            for i in range(5):
                diff_percentual = ((alturas[i] - referencia) / referencia) * 100.0
                print(f"Planta {i+1} - Altura: {alturas[i]:.2f} cm | Diferença: {diff_percentual:+.2f}%")
                
            # Passo 5: Laço aninhado para comparar cada planta com todas as outras e achar a maior
            maior_altura = alturas[0]
            indice_maior = 0
            
            for i in range(5):
                planta_atual = alturas[i]
                eh_a_maior = True
                for j in range(5):
                    if alturas[j] > planta_atual:
                        eh_a_maior = False
                if eh_a_maior:
                    maior_altura = planta_atual
                    indice_maior = i
                    
            print(f"\nA planta mais alta é a Planta {indice_maior+1} com {maior_altura:.2f} cm.")
    else:
        print("Erro: Opção inválida.")
