# Exercício 5: Controle de Qualidade de Lotes de Chocolate
# Objetivo: Realizar o controle de peso de barras de chocolate contidas em caixas de um lote, classificando-as em Padrão, Refugo ou Excesso.

# Passo 1: Inicialização do laço principal do menu interativo
sistema_ativo = True
while sistema_ativo:
    print("\n=== Controle de Qualidade - Fábrica de Chocolates ===")
    print("1 - Iniciar Análise de Novo Lote")
    print("2 - Encerrar Sistema")
    
    opcao = input("Escolha uma opção: ")
    opcao = int(opcao)
    
    if opcao == 2:
        sistema_ativo = False
        print("Sistema de controle de qualidade finalizado.")
    elif opcao == 1:
        # Passo 2: Leitura do identificador do lote e quantidade de caixas
        lote_id = input("\nDigite o identificador do lote (ex: LOTE-2026): ")
        
        caixas_valido = False
        while not caixas_valido:
            qtd_caixas = input("Digite a quantidade de caixas no lote: ")
            qtd_caixas = int(qtd_caixas)
            if qtd_caixas > 0:
                caixas_valido = True
            else:
                print("Erro: A quantidade de caixas deve ser maior que zero.")
                
        # Leitura da quantidade de barras por caixa
        barras_valido = False
        while not barras_valido:
            barras_por_caixa = input("Digite a quantidade de barras de chocolate por caixa: ")
            barras_por_caixa = int(barras_por_caixa)
            if barras_por_caixa > 0:
                barras_valido = True
            else:
                print("Erro: A quantidade de barras deve ser maior que zero.")
                
        # Passo 3: Inicialização das variáveis acumuladoras do lote
        soma_peso_lote = 0.0
        total_barras_lote = 0
        
        # Passo 4: Laço para percorrer cada caixa do lote
        for c in range(1, qtd_caixas + 1):
            print(f"\n  --- Processando Caixa {c} ---")
            # Inicialização das categorias específicas da caixa atual
            padrao_caixa = 0
            refugo_caixa = 0
            excesso_caixa = 0
            
            # Passo 5: Laço para processar cada barra da caixa atual
            for b in range(1, barras_por_caixa + 1):
                # Leitura e validação do peso da barra
                peso_valido = False
                while not peso_valido:
                    peso = input(f"    Digite o peso da barra {b} (em gramas): ")
                    peso = float(peso)
                    if peso > 0.0:
                        peso_valido = True
                    else:
                        print("    Erro: O peso deve ser maior que zero.")
                        
                # Acumulação de dados gerais
                soma_peso_lote = soma_peso_lote + peso
                total_barras_lote = total_barras_lote + 1
                
                # Classificação do peso da barra
                if 95.0 <= peso <= 105.0:
                    padrao_caixa = padrao_caixa + 1
                elif peso < 95.0:
                    refugo_caixa = refugo_caixa + 1
                else:
                    excesso_caixa = excesso_caixa + 1
                    
            # Passo 6: Exibição do relatório de categorias da caixa atual
            print(f"  Resultado da Caixa {c}:")
            print(f"    Barras Padrão: {padrao_caixa}")
            print(f"    Barras Refugo (Leves): {refugo_caixa}")
            print(f"    Barras com Excesso: {excesso_caixa}")
            
        # Passo 7: Cálculo da média de peso do lote
        media_peso_lote = soma_peso_lote / total_barras_lote
        
        # Passo 8: Exibição do relatório final do lote
        print(f"\n================ Relatório Final do Lote {lote_id} ================")
        print(f"Total de Caixas Analisadas: {qtd_caixas}")
        print(f"Total Geral de Barras: {total_barras_lote}")
        print(f"Peso Total do Lote: {soma_peso_lote:.2f} g")
        print(f"Média de Peso por Barra: {media_peso_lote:.2f} g")
        print("=================================================================")
    else:
        print("Erro: Opção inválida do menu.")
