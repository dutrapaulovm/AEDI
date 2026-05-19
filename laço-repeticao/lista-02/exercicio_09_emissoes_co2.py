# Exercício 9: Análise de Emissões de Carbono Industrial
# Objetivo: Monitorar e avaliar as emissões de CO2 de 3 fábricas ao longo de 4 trimestres com 2 linhas de produção cada, calculando multas e gerando o ranking das mais poluidoras.

# Passo 1: Inicialização das emissões totais por fábrica (sem usar vetores/listas)
total_f1 = 0.0
total_f2 = 0.0
total_f3 = 0.0

# Passo 2: Laço principal para processar cada uma das 3 fábricas
for f in range(1, 4):
    print(f"\n================ PROCESSANDO FÁBRICA {f} ================")
    
    # Variáveis acumuladoras da fábrica atual
    soma_emissoes_fabrica = 0.0
    multa_total_fabrica = 0.0
    
    # Variável para rastrear a emissão do trimestre anterior (para calcular o bônus de crédito de carbono)
    emissao_trimestre_anterior = -1.0
    
    # Passo 3: Laço para percorrer os 4 trimestres
    for trim in range(1, 5):
        print(f"\n  Trimestre {trim}:")
        
        # Leitura e validação da emissão da Linha de Produção 1
        l1_valido = False
        while not l1_valido:
            l1 = input("    Digite a emissão da Linha 1 (em toneladas de CO2): ")
            l1 = float(l1)
            if l1 >= 0.0:
                l1_valido = True
            else:
                print("    Erro: A emissão não pode ser negativa.")
                
        # Leitura e validação da emissão da Linha de Produção 2
        l2_valido = False
        while not l2_valido:
            l2 = input("    Digite a emissão da Linha 2 (em toneladas de CO2): ")
            l2 = float(l2)
            if l2 >= 0.0:
                l2_valido = True
            else:
                print("    Erro: A emissão não pode ser negativa.")
                
        # Passo 4: Cálculo da emissão total do trimestre
        emissao_trimestre = l1 + l2
        soma_emissoes_fabrica = soma_emissoes_fabrica + emissao_trimestre
        
        # Verificação do limite trimestral de 500 toneladas
        multa_trimestre = 0.0
        if emissao_trimestre > 500.0:
            excesso = emissao_trimestre - 500.0
            multa_trimestre = excesso * 150.00
            multa_total_fabrica = multa_total_fabrica + multa_trimestre
            print(f"    [!] Alerta: Limite excedido em {excesso:.2f} t! Multa de R$ {multa_trimestre:.2f} aplicada.")
            
        # Verificação de redução de emissões em relação ao trimestre anterior (bônus de carbono)
        if emissao_trimestre_anterior != -1.0:
            if emissao_trimestre < emissao_trimestre_anterior:
                bonus = emissao_trimestre * 0.05
                print(f"    [*] Bônus: Redução detectada! Ganhou {bonus:.2f} créditos de carbono (5% de bônus).")
                
        # Atualiza a emissão do trimestre anterior para a próxima iteração
        emissao_trimestre_anterior = emissao_trimestre

    # Passo 5: Salvar o total da fábrica atual nas variáveis específicas
    if f == 1:
        total_f1 = soma_emissoes_fabrica
    elif f == 2:
        total_f2 = soma_emissoes_fabrica
    else:
        total_f3 = soma_emissoes_fabrica
        
    print(f"\n--- Resumo Fábrica {f} ---")
    print(f"  Emissões Totais no Ano: {soma_emissoes_fabrica:.2f} toneladas")
    print(f"  Multa Ambiental Acumulada: R$ {multa_total_fabrica:.2f}")

# Passo 6: Criação do ranking das fábricas sem usar ordenação de listas/vetores
print("\n================ RANKING DE EMISSÕES DE CO2 ================")

# Determinar a primeira, segunda e terceira mais poluidora usando lógica de condicionais puras
if total_f1 >= total_f2 and total_f1 >= total_f3:
    primeira_nome = "Fábrica 1"
    primeira_valor = total_f1
    if total_f2 >= total_f3:
        segunda_nome = "Fábrica 2"
        segunda_valor = total_f2
        terceira_nome = "Fábrica 3"
        terceira_valor = total_f3
    else:
        segunda_nome = "Fábrica 3"
        segunda_valor = total_f3
        terceira_nome = "Fábrica 2"
        terceira_valor = total_f2
elif total_f2 >= total_f1 and total_f2 >= total_f3:
    primeira_nome = "Fábrica 2"
    primeira_valor = total_f2
    if total_f1 >= total_f3:
        segunda_nome = "Fábrica 1"
        segunda_valor = total_f1
        terceira_nome = "Fábrica 3"
        terceira_valor = total_f3
    else:
        segunda_nome = "Fábrica 3"
        segunda_valor = total_f3
        terceira_nome = "Fábrica 1"
        terceira_valor = total_f1
else:
    primeira_nome = "Fábrica 3"
    primeira_valor = total_f3
    if total_f1 >= total_f2:
        segunda_nome = "Fábrica 1"
        segunda_valor = total_f1
        terceira_nome = "Fábrica 2"
        terceira_valor = total_f2
    else:
        segunda_nome = "Fábrica 2"
        segunda_valor = total_f2
        terceira_nome = "Fábrica 1"
        terceira_valor = total_f1

# Passo 7: Exibição do ranking final
print(f"1º Lugar: {primeira_nome} - Emissões: {primeira_valor:.2f} t (Mais poluidora)")
print(f"2º Lugar: {segunda_nome} - Emissões: {segunda_valor:.2f} t")
print(f"3º Lugar: {terceira_nome} - Emissões: {terceira_valor:.2f} t (Menos poluidora)")
print("=============================================================")
