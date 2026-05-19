# Exercício 7: Processador de Voltas e Tempos de Pilotos em GP
# Objetivo: Acompanhar o tempo de corrida de 3 pilotos durante 5 voltas, aplicando penalidades de tempo por cortes de pista e declarando o vencedor.

# Passo 1: Inicialização das variáveis para determinar o vencedor geral
melhor_tempo_total = 99999999.0
vencedor_nome = ""

# Passo 2: Laço para processar cada um dos 3 pilotos
for p in range(1, 4):
    print(f"\n--- Piloto {p} ---")
    nome = input(f"Digite o nome do {p}º piloto: ")
    
    # Acumuladores de tempo e melhor volta do piloto atual
    tempo_total = 0.0
    melhor_volta_tempo = 99999999.0
    melhor_volta_numero = 0
    penalidades = 0
    
    # Passo 3: Laço para ler e processar as 5 voltas do piloto
    for volta in range(1, 6):
        tempo_valido = False
        while not tempo_valido:
            tempo = input(f"  Digite o tempo da Volta {volta} (em segundos): ")
            tempo = float(tempo)
            if tempo > 0.0:
                tempo_valido = True
            else:
                print("  Erro: O tempo de volta deve ser maior que zero.")
                
        # Acumula o tempo no total
        tempo_total = tempo_total + tempo
        
        # Identifica se é a melhor volta (tempo mais rápido) deste piloto
        if tempo < melhor_volta_tempo:
            melhor_volta_tempo = tempo
            melhor_volta_numero = volta
            
        # Penalidade: se a volta for menor que 60 segundos (corte de caminho), +5s
        if tempo < 60.0:
            penalidades = penalidades + 1
            
    # Passo 4: Aplicação das penalidades no tempo final
    tempo_penalidade = penalidades * 5.0
    tempo_final_calculado = tempo_total + tempo_penalidade
    
    # Passo 5: Exibição do relatório individual do piloto
    print(f"\n  Resumo do Piloto {nome}:")
    print(f"    Tempo de pista acumulado: {tempo_total:.2f} s")
    print(f"    Melhor Volta: Volta {melhor_volta_numero} com {melhor_volta_tempo:.2f} s")
    if penalidades > 0:
        print(f"    Penalidades Aplicadas: {penalidades} cortes (+{tempo_penalidade:.1f} s)")
    print(f"    Tempo Final de Prova: {tempo_final_calculado:.2f} s")
    
    # Passo 6: Verifica se este piloto tem o menor tempo acumulado do GP
    if tempo_final_calculado < melhor_tempo_total:
        melhor_tempo_total = tempo_final_calculado
        vencedor_nome = nome

# Passo 7: Exibição do resultado final (Pole Position / Vencedor do GP)
print(f"\n================ FIM DO GP ================")
print(f"Vencedor da Corrida: {vencedor_nome}!")
print(f"Tempo Final do Vencedor: {melhor_tempo_total:.2f} s")
print("===========================================")
