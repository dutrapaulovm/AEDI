# Exercício 1: Produtividade Agrícola de Fazendas e Talhões
# Objetivo: Monitorar a produtividade mensal de talhões em fazendas com validações de entrada completas e classificação de produtividade.

# Passo 1: Leitura e validação da quantidade de fazendas
qtd_fazendas_valida = False
while not qtd_fazendas_valida:
    qtd_fazendas = input("Digite a quantidade de fazendas a serem analisadas: ")
    qtd_fazendas = int(qtd_fazendas)
    if qtd_fazendas > 0:
        qtd_fazendas_valida = True
    else:
        print("Erro: A quantidade de fazendas deve ser um valor maior que zero.")

# Passo 2: Laço principal para percorrer cada fazenda
for f in range(1, qtd_fazendas + 1):
    print(f"\n--- Processando Fazenda {f} ---")
    
    # Passo 3: Leitura e validação da quantidade de talhões para a fazenda atual
    qtd_talhoes_valido = False
    while not qtd_talhoes_valido:
        qtd_talhoes = input(f"Digite a quantidade de talhões para a Fazenda {f}: ")
        qtd_talhoes = int(qtd_talhoes)
        if qtd_talhoes > 0:
            qtd_talhoes_valido = True
        else:
            print("Erro: A quantidade de talhões deve ser maior que zero.")
            
    # Passo 4: Inicialização do acumulador de médias de talhões da fazenda
    soma_medias_talhoes = 0.0
    
    # Passo 5: Laço para percorrer cada talhão da fazenda atual
    for t in range(1, qtd_talhoes + 1):
        print(f"  Talhão {t}:")
        
        # Leitura e validação da produção do Mês 1
        m1_valido = False
        while not m1_valido:
            m1 = input("    Digite a produção do Mês 1 (em toneladas): ")
            m1 = float(m1)
            if m1 >= 0.0:
                m1_valido = True
            else:
                print("    Erro: A produção não pode ser negativa.")
                
        # Leitura e validação da produção do Mês 2
        m2_valido = False
        while not m2_valido:
            m2 = input("    Digite a produção do Mês 2 (em toneladas): ")
            m2 = float(m2)
            if m2 >= 0.0:
                m2_valido = True
            else:
                print("    Erro: A produção não pode ser negativa.")
                
        # Leitura e validação da produção do Mês 3
        m3_valido = False
        while not m3_valido:
            m3 = input("    Digite a produção do Mês 3 (em toneladas): ")
            m3 = float(m3)
            if m3 >= 0.0:
                m3_valido = True
            else:
                print("    Erro: A produção não pode ser negativa.")
                
        # Passo 6: Cálculo da média de produção do talhão
        media_talhao = (m1 + m2 + m3) / 3.0
        soma_medias_talhoes = soma_medias_talhoes + media_talhao
        
    # Passo 7: Cálculo da média final de produção da fazenda
    media_fazenda = soma_medias_talhoes / qtd_talhoes
    
    # Passo 8: Classificação da produtividade da fazenda
    if media_fazenda >= 50.0:
        classificacao = "Alta"
    elif 20.0 <= media_fazenda < 50.0:
        classificacao = "Regular"
    else:
        classificacao = "Baixa"
        
    # Passo 9: Exibição do resultado final para a fazenda
    print(f"\nResultado: Fazenda {f} - Média Final: {media_fazenda:.2f} t - Classificação: {classificacao}")
