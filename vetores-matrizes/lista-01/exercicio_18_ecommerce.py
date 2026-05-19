# Exercício 18: Controle de Preços E-commerce (Matriz 3x4)
# Objetivo: Gerenciar preços de 3 categorias com 4 itens cada, aplicar promoção relâmpago a toda a matriz e localizar o item mais caro pós-promoção.

# Passo 1: Inicialização da matriz 3x4 com zeros e status de cadastro
precos = [
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0]
]
cadastrado = False
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- GESTOR DE PREÇOS E-COMMERCE (3x4) ---")
    print("1. Cadastrar Preços das 3 Categorias")
    print("2. Aplicar Desconto Promocional Relâmpago")
    print("3. Visualizar Preços e Mais Caros por Categoria")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Gestor de preços encerrado.")
        
    elif opcao == 1:
        # Passo 3: Cadastrar e validar preços (devem ser estritamente positivos)
        print("\n--- Cadastro de Preços ---")
        for i in range(3):
            print(f"Categoria {i+1}:")
            for j in range(4):
                valido = False
                while not valido:
                    preco = input(f"  Preço do Item {j+1} (R$): ")
                    preco = float(preco)
                    if preco > 0.0:
                        precos[i][j] = preco
                        valido = True
                    else:
                        print("  Erro: O preço deve ser maior que zero (R$ 0.00). Digite novamente.")
        cadastrado = True
        print("Preços cadastrados com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Aplicar desconto promocional em toda a matriz
        if not cadastrado:
            print("Erro: Cadastre os preços primeiro (Opção 1).")
        else:
            print("\n--- Aplicação de Desconto Promocional ---")
            desc_valido = False
            while not desc_valido:
                percent_desc = input("Digite a porcentagem de desconto da promoção relâmpago (%): ")
                percent_desc = float(percent_desc)
                if 0.0 <= percent_desc <= 100.0:
                    desc_valido = True
                else:
                    print("Erro: A porcentagem deve estar entre 0 e 100.")
                    
            # Laço aninhado para aplicar o desconto a toda a matriz
            fator_multiplicativo = 1.0 - (percent_desc / 100.0)
            for i in range(3):
                for j in range(4):
                    precos[i][j] = precos[i][j] * fator_multiplicativo
            print(f"Sucesso: Desconto de {percent_desc:.1f}% aplicado a todos os itens!")
            
    elif opcao == 3:
        # Passo 5: Exibição da matriz e busca pelo mais caro de cada linha (categoria)
        if not cadastrado:
            print("Erro: Cadastre os preços primeiro (Opção 1).")
        else:
            print("\n--- PREÇOS ATUAIS DOS ITENS ---")
            for i in range(3):
                print(f"Categoria {i+1}: {precos[i]}")
                
            print("\nItem mais caro de cada categoria:")
            for i in range(3):
                mais_caro_categoria = precos[i][0]
                item_idx = 0
                for j in range(1, 4):
                    if precos[i][j] > mais_caro_categoria:
                        mais_caro_categoria = precos[i][j]
                        item_idx = j
                print(f"  Categoria {i+1} : Item {item_idx+1} é o mais caro custando R$ {mais_caro_categoria:.2f}")
    else:
        print("Erro: Opção inválida.")
