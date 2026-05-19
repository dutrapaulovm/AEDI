# Exercício 27: Indexação Sequencial de Banco de Dados (Matriz 5x2)
# Objetivo: Gerenciar a indexação de 5 usuários em uma matriz 5x2 (coluna 0: ID, coluna 1: Status Ativo/Inativo), impedindo duplicatas e realizando exclusão lógica.

# Passo 1: Inicialização da matriz indexadora 5x2 com zeros (Status: 0 indica inativo/excluído ou vazio, 1 indica ativo)
tabela_usuarios = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0]
]
quantidade_inserida = 0
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- GESTOR DE INDEXAÇÃO SEQUENCIAL DE BD (5x2) ---")
    print("1. Inserir Novo Usuário (ID)")
    print("2. Pesquisar Status de Usuário por ID")
    print("3. Excluir Usuário Logicamente")
    print("4. Exibir Tabela de Índices")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Tabela de índices encerrada.")
        
    elif opcao == 1:
        # Passo 3: Inserir usuário na primeira posição vaga e validar duplicidade de ID
        if quantidade_inserida >= 5:
            print("Erro: Banco de dados de índices cheio (máximo de 5 registros).")
        else:
            print("\n--- Inserção de Registro ---")
            
            id_valido = False
            novo_id = -1
            while not id_valido:
                novo_id = input("Digite o ID único do usuário (inteiro positivo): ")
                novo_id = int(novo_id)
                if novo_id > 0:
                    # Passo 4: Verificar se o ID já existe na tabela (duplicidade)
                    id_duplicado = False
                    for i in range(5):
                        # Só valida contra registros que possuem ID correspondente ativo
                        if tabela_usuarios[i][0] == novo_id and tabela_usuarios[i][1] == 1:
                            id_duplicado = True
                            
                    if id_duplicado:
                        print("Erro: Este ID já está cadastrado e ativo. Insira outro.")
                    else:
                        id_valido = True
                else:
                    print("Erro: O ID deve ser um inteiro positivo.")
                    
            # Localiza a primeira vaga livre (ou com status inativo/0)
            slot_livre = -1
            for i in range(5):
                if tabela_usuarios[i][1] == 0:
                    slot_livre = i
                    break
                    
            tabela_usuarios[slot_livre][0] = novo_id
            tabela_usuarios[slot_livre][1] = 1  # Status 1: Ativo
            quantidade_inserida = quantidade_inserida + 1
            print(f"Sucesso: Usuário com ID {novo_id} inserido no slot indexador {slot_livre}!")
            
    elif opcao == 2:
        # Passo 5: Pesquisar usuário e status
        print("\n--- Pesquisar Usuário por ID ---")
        busca_id = input("Digite o ID a pesquisar: ")
        busca_id = int(busca_id)
        
        posicao = -1
        for i in range(5):
            if tabela_usuarios[i][0] == busca_id and tabela_usuarios[i][1] == 1:
                posicao = i
                break
                
        if posicao != -1:
            print(f"Sucesso: Usuário ID {busca_id} está ATIVO no slot indexador {posicao}.")
        else:
            print(f"Informação: Usuário ID {busca_id} não foi encontrado ou está INATIVO no banco de dados.")
            
    elif opcao == 3:
        # Passo 6: Exclusão lógica (alterar status na coluna 1 para 0)
        print("\n--- Exclusão Lógica de Registro ---")
        excluir_id = input("Digite o ID do usuário a excluir logicamente: ")
        excluir_id = int(excluir_id)
        
        posicao = -1
        for i in range(5):
            if tabela_usuarios[i][0] == excluir_id and tabela_usuarios[i][1] == 1:
                posicao = i
                break
                
        if posicao != -1:
            # Exclusão lógica: apenas altera a coluna status para 0
            tabela_usuarios[posicao][1] = 0
            quantidade_inserida = quantidade_inserida - 1
            print(f"Sucesso: Exclusão lógica realizada! O Usuário ID {excluir_id} foi marcado como inativo.")
        else:
            print(f"Erro: Usuário ID {excluir_id} não encontrado ou já está inativo.")
            
    elif opcao == 4:
        # Exibir a tabela crua de indexação
        print("\n--- TABELA DE ÍNDICES COMPLETA (Matriz 5x2) ---")
        for i in range(5):
            status_txt = "Ativo" if tabela_usuarios[i][1] == 1 else "Inativo/Livre"
            print(f"  Slot {i} : [ID: {tabela_usuarios[i][0]:3d}] -> Status: {tabela_usuarios[i][1]} ({status_txt})")
    else:
        print("Erro: Opção inválida.")
