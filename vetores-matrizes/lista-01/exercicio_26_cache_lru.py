# Exercício 26: Simulador de Memória Cache LRU (Vetor de 4 Posições)
# Objetivo: Simular a ocupação de 4 slots de cache de páginas de CPU, gerenciando acertos (Hit) com realocação para o final e erros (Miss) com deslocamento FIFO.

# Passo 1: Inicialização da cache com zeros (0 indica slot vazio)
cache = [0] * 4
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- SIMULADOR DE MEMÓRIA CACHE LRU (4 SLOTS) ---")
    print("1. Acessar Página por ID")
    print("2. Visualizar Estado Atual da Cache")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Simulador de cache encerrado.")
        
    elif opcao == 1:
        # Passo 3: Solicitar página e pesquisar no vetor
        page_id = input("Digite o ID da página a acessar (inteiro positivo): ")
        page_id = int(page_id)
        
        if page_id <= 0:
            print("Erro: O ID da página deve ser maior que zero.")
        else:
            # Busca na cache
            hit_index = -1
            for i in range(4):
                if cache[i] == page_id:
                    hit_index = i
                    
            if hit_index != -1:
                # Passo 4: Cache Hit (Acerto)
                # Reorganiza o vetor movendo o item acessado para a última posição (mais recente)
                print(f"\n[CACHE HIT] Página {page_id} encontrada no slot {hit_index}!")
                
                # Armazena o valor do hit
                valor_hit = cache[hit_index]
                
                # Desloca os elementos à direita do hit para a esquerda
                for i in range(hit_index, 3):
                    cache[i] = cache[i + 1]
                    
                # Insere o valor hit no final da fila (mais recentemente acessado)
                cache[3] = valor_hit
                
            else:
                # Passo 5: Cache Miss (Erro)
                print(f"\n[CACHE MISS] Página {page_id} não estava na cache.")
                
                # Verifica se há slot vazio (representado por 0)
                primeiro_vazio = -1
                for i in range(4):
                    if cache[i] == 0:
                        primeiro_vazio = i
                        break
                        
                if primeiro_vazio != -1:
                    # Insere no primeiro slot livre encontrado
                    cache[primeiro_vazio] = page_id
                    print(f"Página {page_id} alocada no slot livre {primeiro_vazio}.")
                else:
                    # Cache cheia: remove o mais antigo (desloca todos para a esquerda, descartando cache[0])
                    print(f"Cache cheia! Descartando página mais antiga ({cache[0]}) do slot 0 (FIFO).")
                    
                    cache[0] = cache[1]
                    cache[1] = cache[2]
                    cache[2] = cache[3]
                    
                    # Insere o novo no final
                    cache[3] = page_id
                    print(f"Nova página {page_id} inserida no slot mais recente (slot 3).")
                    
    elif opcao == 2:
        # Passo 6: Exibir estado da cache
        print("\n--- ESTADO ATUAL DA CACHE ---")
        print(" [Mais Antigo/Menos Usado]                         [Mais Recente] ")
        print(f" Slot 0: {cache[0]} | Slot 1: {cache[1]} | Slot 2: {cache[2]} | Slot 3: {cache[3]}")
    else:
        print("Erro: Opção inválida.")
