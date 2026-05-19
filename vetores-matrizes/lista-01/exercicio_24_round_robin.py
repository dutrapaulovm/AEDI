# Exercício 24: Escalonamento de Processos Round Robin (Vetor de 5 Posições)
# Objetivo: Simular a execução circular de 5 processos com tempos de burst armazenados em um vetor, aplicando quantum de CPU e contando os ciclos.

# Passo 1: Inicialização dos tempos de burst dos 5 processos e variáveis de controle
burst_times = [0] * 5
cadastrado = False
quantum = 0
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- SIMULADOR DE ESCALONAMENTO ROUND ROBIN ---")
    print("1. Cadastrar Processos e Tempo Quantum")
    print("2. Simular Escalonamento Circular")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Simulador de escalonamento encerrado.")
        
    elif opcao == 1:
        # Passo 3: Cadastrar tempos de execução (Burst Time >= 0) e quantum (> 0)
        print("\n--- Cadastro de Carga de Processos ---")
        q_valido = False
        while not q_valido:
            quantum = input("Digite o valor do Quantum de tempo da CPU: ")
            quantum = int(quantum)
            if quantum > 0:
                q_valido = True
            else:
                print("Erro: O Quantum de tempo deve ser maior que zero.")
                
        for i in range(5):
            valido = False
            while not valido:
                bt = input(f"Digite o Burst Time (tempo de execução) do Processo P{i+1}: ")
                bt = int(bt)
                if bt >= 0:
                    burst_times[i] = bt
                    valido = True
                else:
                    print("  Erro: O Burst Time não pode ser negativo.")
        cadastrado = True
        print("Processos cadastrados com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Executar a simulação Round Robin com laço while circular
        if not cadastrado:
            print("Erro: Cadastre os processos primeiro (Opção 1).")
        else:
            print("\n--- SIMULAÇÃO DE PROCESSAMENTO ROUND ROBIN ---")
            
            # Fazemos uma cópia do vetor de burst para não alterar o original cadastrado
            fila_processos = [0] * 5
            for i in range(5):
                fila_processos[i] = burst_times[i]
                
            ciclos = 0
            processos_ativos = True
            
            # Passo 5: Laço while contínuo rodando enquanto houver processos com tempo > 0
            while processos_ativos:
                processos_ativos = False
                rodada_executou = False
                
                print(f"\n[Ciclo {ciclos+1}] Estado da Fila: {fila_processos}")
                
                for i in range(5):
                    if fila_processos[i] > 0:
                        processos_ativos = True
                        rodada_executou = True
                        
                        # Processo executa por no máximo o tempo do quantum
                        if fila_processos[i] > quantum:
                            print(f"  CPU alocada para P{i+1}: Executa {quantum}ms e sofre preempção (restam {fila_processos[i]-quantum}ms).")
                            fila_processos[i] = fila_processos[i] - quantum
                        else:
                            print(f"  CPU alocada para P{i+1}: Executa {fila_processos[i]}ms e é CONCLUÍDO!")
                            fila_processos[i] = 0
                            
                if rodada_executou:
                    ciclos = ciclos + 1
                    
            print(f"\nConcluído! Todos os processos finalizaram a execução.")
            print(f"Total de ciclos/rodadas da CPU necessários: {ciclos}")
    else:
        print("Erro: Opção inválida.")
