# Exercício 2: Testes de Resistência e Pressão de Autopeças
# Objetivo: Controlar a qualidade de lotes de autopeças, realizando 4 testes de pressão por peça, validando valores e computando a taxa de aprovação.

# Passo 1: Leitura e validação da quantidade de lotes
lotes_valido = False
while not lotes_valido:
    qtd_lotes = input("Digite a quantidade de lotes a serem testados: ")
    qtd_lotes = int(qtd_lotes)
    if qtd_lotes > 0:
        lotes_valido = True
    else:
        print("Erro: A quantidade de lotes deve ser maior que zero.")

# Passo 2: Laço principal para percorrer os lotes
for lote in range(1, qtd_lotes + 1):
    print(f"\n--- Processando Lote {lote} ---")
    
    # Passo 3: Leitura e validação da quantidade de peças do lote atual
    pecas_valido = False
    while not pecas_valido:
        qtd_pecas = input(f"Digite a quantidade de peças para o Lote {lote}: ")
        qtd_pecas = int(qtd_pecas)
        if qtd_pecas > 0:
            pecas_valido = True
        else:
            print("Erro: A quantidade de peças deve ser maior que zero.")
            
    # Passo 4: Inicialização do contador de peças aprovadas
    aprovadas_lote = 0
    
    # Passo 5: Laço para percorrer cada peça do lote
    for peca in range(1, qtd_pecas + 1):
        print(f"  Peça {peca}:")
        
        # Leitura e validação do Teste 1
        t1_valido = False
        while not t1_valido:
            t1 = input("    Digite o resultado do Teste 1 (0 a 100): ")
            t1 = float(t1)
            if 0.0 <= t1 <= 100.0:
                t1_valido = True
            else:
                print("    Erro: O valor deve estar no intervalo [0, 100].")
                
        # Leitura e validação do Teste 2
        t2_valido = False
        while not t2_valido:
            t2 = input("    Digite o resultado do Teste 2 (0 a 100): ")
            t2 = float(t2)
            if 0.0 <= t2 <= 100.0:
                t2_valido = True
            else:
                print("    Erro: O valor deve estar no intervalo [0, 100].")
                
        # Leitura e validação do Teste 3
        t3_valido = False
        while not t3_valido:
            t3 = input("    Digite o resultado do Teste 3 (0 a 100): ")
            t3 = float(t3)
            if 0.0 <= t3 <= 100.0:
                t3_valido = True
            else:
                print("    Erro: O valor deve estar no intervalo [0, 100].")
                
        # Leitura e validação do Teste 4
        t4_valido = False
        while not t4_valido:
            t4 = input("    Digite o resultado do Teste 4 (0 a 100): ")
            t4 = float(t4)
            if 0.0 <= t4 <= 100.0:
                t4_valido = True
            else:
                print("    Erro: O valor deve estar no intervalo [0, 100].")
                
        # Passo 6: Cálculo da média e verificação das regras de aprovação
        media_testes = (t1 + t2 + t3 + t4) / 4.0
        
        # Uma peça é aprovada se a média for >= 70 E nenhum teste individual for < 50
        if media_testes >= 70.0 and t1 >= 50.0 and t2 >= 50.0 and t3 >= 50.0 and t4 >= 50.0:
            status = "Aprovada"
            aprovadas_lote = aprovadas_lote + 1
        else:
            status = "Reprovada"
            
        print(f"    Status da Peça {peca}: {status} (Média: {media_testes:.2f})")
        
    # Passo 7: Cálculo do percentual de aprovação do lote
    aproveitamento = (aprovadas_lote / qtd_pecas) * 100.0
    
    # Passo 8: Exibição do relatório final para o lote
    print(f"\nResultado Final: Lote {lote} - Aproveitamento: {aproveitamento:.2f}%")
