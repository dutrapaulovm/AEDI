# Exercício 8: Inventário e Logística de Armazém Multinível
# Objetivo: Controlar o estoque de produtos distribuídos em 3 corredores, 5 estantes e 4 prateleiras por corredor, sem utilizar vetores ou listas.

# Passo 1: Inicialização dos acumuladores para os 3 corredores (sem usar listas)
volume_corredor1 = 0
volume_corredor2 = 0
volume_corredor3 = 0

total_criticos = 0

# Passo 2: Laço principal do menu de controle de inventário
ativo = True
while ativo:
    print("\n=== Menu do Inventário de Armazém ===")
    print("1 - Cadastrar Produto e Posição")
    print("2 - Gerar Relatório de Ocupação dos Corredores")
    print("3 - Encerrar Inventário")
    
    opcao = input("Escolha uma opção: ")
    opcao = int(opcao)
    
    if opcao == 3:
        ativo = False
        print("Inventário fechado.")
    elif opcao == 1:
        # Passo 3: Leitura e validação dos dados do produto
        nome_produto = input("\nDigite o nome do produto: ")
        
        # Validação do Corredor (1 a 3)
        corredor_valido = False
        while not corredor_valido:
            corredor = input("Digite o corredor (1 a 3): ")
            corredor = int(corredor)
            if 1 <= corredor <= 3:
                corredor_valido = True
            else:
                print("Erro: O corredor deve ser 1, 2 ou 3.")
                
        # Validação da Estante (1 a 5)
        estante_valido = False
        while not estante_valido:
            estante = input("Digite a estante (1 a 5): ")
            estante = int(estante)
            if 1 <= estante <= 5:
                estante_valido = True
            else:
                print("Erro: A estante deve ser entre 1 e 5.")
                
        # Validação da Prateleira (1 a 4)
        prateleira_valido = False
        while not prateleira_valido:
            prateleira = input("Digite a prateleira (1 a 4): ")
            prateleira = int(prateleira)
            if 1 <= prateleira <= 4:
                prateleira_valido = True
            else:
                print("Erro: A prateleira deve ser entre 1 e 4.")
                
        # Validação da Quantidade (não negativa)
        quantidade_valido = False
        while not quantidade_valido:
            quantidade = input("Digite a quantidade em estoque: ")
            quantidade = int(quantidade)
            if quantidade >= 0:
                quantidade_valido = True
            else:
                print("Erro: A quantidade não pode ser negativa.")
                
        # Passo 4: Verificação de Estoque Crítico
        status_estoque = "Normal"
        if quantidade < 10:
            status_estoque = "Estoque Crítico (Abaixo de 10 unidades)"
            total_criticos = total_criticos + 1
            
        print(f"\nProduto {nome_produto} registrado com sucesso na posição C{corredor}-E{estante}-P{prateleira}!")
        print(f"Status do item: {status_estoque}")
        
        # Passo 5: Acumulação de volumes específicos de corredor
        if corredor == 1:
            volume_corredor1 = volume_corredor1 + quantidade
        elif corredor == 2:
            volume_corredor2 = volume_corredor2 + quantidade
        else:
            volume_corredor3 = volume_corredor3 + quantidade
            
    elif opcao == 2:
        # Passo 6: Cálculo dos valores totais por corredor (R$ 50,00 por unidade)
        valor_corredor1 = volume_corredor1 * 50.0
        valor_corredor2 = volume_corredor2 * 50.0
        valor_corredor3 = volume_corredor3 * 50.0
        
        # Passo 7: Determinação de qual corredor possui o maior volume
        if volume_corredor1 >= volume_corredor2 and volume_corredor1 >= volume_corredor3:
            maior_corredor = "Corredor 1"
            maior_volume = volume_corredor1
        elif volume_corredor2 >= volume_corredor1 and volume_corredor2 >= volume_corredor3:
            maior_corredor = "Corredor 2"
            maior_volume = volume_corredor2
        else:
            maior_corredor = "Corredor 3"
            maior_volume = volume_corredor3
            
        # Passo 8: Exibição do relatório de inventário
        print("\n--- Relatório de Ocupação de Corredores ---")
        print(f"Corredor 1: Volume={volume_corredor1} unidades | Valor Total=R$ {valor_corredor1:.2f}")
        print(f"Corredor 2: Volume={volume_corredor2} unidades | Valor Total=R$ {valor_corredor2:.2f}")
        print(f"Corredor 3: Volume={volume_corredor3} unidades | Valor Total=R$ {valor_corredor3:.2f}")
        print(f"\nCorredor com maior volume estocado: {maior_corredor} ({maior_volume} unidades)")
        print(f"Total de produtos com status de Estoque Crítico: {total_criticos}")
        print("------------------------------------------")
    else:
        print("Erro: Opção inválida do menu.")
