# Exercício 14: Análise de Engajamento de Posts (Vetor de 6 Posições)
# Objetivo: Monitorar o número de curtidas de 6 posts, identificar posts virais, ordenar as curtidas do mais popular para o menos popular e comparar com a meta.

# Passo 1: Inicialização das variáveis
curtidas = [0] * 6
cadastrado = False
meta_engajamento = 0
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- ANALISADOR DE ENGAJAMENTO SOCIAL ---")
    print("1. Cadastrar Curtidas dos 6 Posts e Meta")
    print("2. Analisar Posts Virais e Metas")
    print("3. Ordenar Posts por Popularidade")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Analisador de engajamento encerrado.")
        
    elif opcao == 1:
        # Passo 3: Cadastro com validação de curtidas (não negativas)
        print("\n--- Cadastro de Curtidas ---")
        meta_valida = False
        while not meta_valida:
            meta_engajamento = input("Digite a meta de curtidas por post: ")
            meta_engajamento = int(meta_engajamento)
            if meta_engajamento > 0:
                meta_valida = True
            else:
                print("Erro: A meta deve ser positiva.")
                
        for i in range(6):
            valido = False
            while not valido:
                likes = input(f"Digite o número de curtidas do Post {i+1}: ")
                likes = int(likes)
                if likes >= 0:
                    curtidas[i] = likes
                    valido = True
                else:
                    print("Erro: O número de curtidas não pode ser negativo.")
        cadastrado = True
        print("Registros de curtidas salvos!")
        
    elif opcao == 2:
        # Passo 4: Identificação de posts virais (curtidas > 2 * média) e verificação da meta
        if not cadastrado:
            print("Erro: Cadastre as curtidas primeiro (Opção 1).")
        else:
            print("\n--- ANÁLISE DE POSTS VIRAIS ---")
            soma = 0
            for i in range(6):
                soma = soma + curtidas[i]
            media_curtidas = soma / 6.0
            print(f"Média de curtidas dos posts: {media_curtidas:.1f}")
            
            algum_atingiu_meta = False
            for i in range(6):
                likes = curtidas[i]
                status_viral = ""
                if likes > (2 * media_curtidas):
                    status_viral = "[VIRAL] "
                    
                status_meta = "Atingiu a Meta" if likes >= meta_engajamento else "Abaixo da Meta"
                if likes >= meta_engajamento:
                    algum_atingiu_meta = True
                    
                print(f"Post {i+1}: {likes} curtidas | {status_viral}{status_meta}")
                
            if not algum_atingiu_meta:
                print("\n[ALERT] Revisar Conteúdo! Nenhum post atingiu a meta de engajamento.")
                
    elif opcao == 3:
        # Passo 5: Ordenar os posts usando ordenação Bubble Sort simples
        if not cadastrado:
            print("Erro: Cadastre as curtidas primeiro (Opção 1).")
        else:
            print("\n--- ORDENAÇÃO POR POPULARIDADE ---")
            # Fazemos uma cópia dos vetores originais de curtidas e de índices para manter a referência
            vetor_ordenado = [0] * 6
            indices_posts = [0] * 6
            for i in range(6):
                vetor_ordenado[i] = curtidas[i]
                indices_posts[i] = i + 1
                
            # Algoritmo clássico Bubble Sort aninhado
            for i in range(6):
                for j in range(0, 5 - i):
                    if vetor_ordenado[j] < vetor_ordenado[j + 1]:
                        # Troca as curtidas
                        temp_likes = vetor_ordenado[j]
                        vetor_ordenado[j] = vetor_ordenado[j + 1]
                        vetor_ordenado[j + 1] = temp_likes
                        
                        # Troca os índices
                        temp_ind = indices_posts[j]
                        indices_posts[j] = indices_posts[j + 1]
                        indices_posts[j + 1] = temp_ind
                        
            print("Posts ordenados do mais curtido ao menos curtido:")
            for i in range(6):
                print(f"  Posição {i+1}: Post {indices_posts[i]} com {vetor_ordenado[i]} curtidas.")
    else:
        print("Erro: Opção inválida.")
