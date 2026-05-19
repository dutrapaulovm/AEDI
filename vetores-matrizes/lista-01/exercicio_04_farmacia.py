# Exercício 4: Controle de Estoque de Farmácia (Matriz 2x4)
# Objetivo: Gerenciar 2 prateleiras com 4 tipos de medicamentos em uma matriz, permitindo vendas, validação de falta de itens e exibição formatada.

# Passo 1: Inicialização da matriz estoque 2x4 com zeros e status de preenchimento
estoque = [
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
preenchido = False
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- CONTROLE DE ESTOQUE FARMACÊUTICO ---")
    print("1. Cadastrar/Abastecer Estoque")
    print("2. Registrar Venda")
    print("3. Visualizar Estoque e Faltas")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema farmacêutico encerrado.")
        
    elif opcao == 1:
        # Passo 3: Abastecimento da matriz com validação (valores não negativos)
        print("\n--- Abastecimento do Estoque ---")
        for i in range(2):
            print(f"Prateleira {i+1}:")
            for j in range(4):
                valido = False
                while not valido:
                    qtd = input(f"  Quantidade para o Medicamento {j+1}: ")
                    qtd = int(qtd)
                    if qtd >= 0:
                        estoque[i][j] = qtd
                        valido = True
                    else:
                        print("  Erro: A quantidade não pode ser negativa. Digite novamente.")
        preenchido = True
        print("Estoque cadastrado com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Operação de Venda de Medicamento
        if not preenchido:
            print("Erro: Cadastre o estoque primeiro (Opção 1).")
        else:
            print("\n--- Registro de Venda ---")
            
            # Validação do índice da prateleira (0 ou 1)
            prateleira_valida = False
            while not prateleira_valida:
                p_ind = input("Digite o número da prateleira (1 ou 2): ")
                p_ind = int(p_ind)
                if 1 <= p_ind <= 2:
                    p_ind = p_ind - 1  # Ajuste para índice 0-based
                    prateleira_valida = True
                else:
                    print("Erro: Prateleira inválida. Escolha 1 ou 2.")
                    
            # Validação do índice do medicamento/coluna (1 a 4)
            coluna_valida = False
            while not coluna_valida:
                c_ind = input("Digite o número do medicamento/coluna (1 a 4): ")
                c_ind = int(c_ind)
                if 1 <= c_ind <= 4:
                    c_ind = c_ind - 1  # Ajuste para índice 0-based
                    coluna_valida = True
                else:
                    print("Erro: Coluna inválida. Escolha de 1 a 4.")
                    
            # Leitura da quantidade da venda
            qtd_venda = input("Digite a quantidade de caixas a vender: ")
            qtd_venda = int(qtd_venda)
            
            # Validação de estoque disponível
            if qtd_venda > estoque[p_ind][c_ind]:
                print(f"Erro: Estoque Insuficiente! Apenas {estoque[p_ind][c_ind]} caixas disponíveis.")
            else:
                estoque[p_ind][c_ind] = estoque[p_ind][c_ind] - qtd_venda
                print(f"Sucesso: Venda de {qtd_venda} caixas registrada!")
                
            # Exibição do estoque formatado após a operação
            print("\nEstoque Atualizado:")
            for i in range(2):
                print(f"Prateleira {i+1}: {estoque[i]}")
                
    elif opcao == 3:
        # Passo 5: Relatório de estoque formatado e contagem de itens zerados
        if not preenchido:
            print("Erro: Cadastre o estoque primeiro (Opção 1).")
        else:
            print("\n--- VISUALIZAÇÃO DO ESTOQUE ---")
            itens_em_falta = 0
            
            for i in range(2):
                linha_formatada = ""
                for j in range(4):
                    linha_formatada = linha_formatada + f"[{estoque[i][j]:02d}] "
                    if estoque[i][j] == 0:
                        itens_em_falta = itens_em_falta + 1
                print(f"Prateleira {i+1}: {linha_formatada}")
                
            print(f"\nTotal de tipos de medicamentos esgotados (em falta): {itens_em_falta}")
    else:
        print("Erro: Opção inválida.")
