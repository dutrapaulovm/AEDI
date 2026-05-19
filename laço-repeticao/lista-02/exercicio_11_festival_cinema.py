# Exercício 11: Sistema de Votação em Festival de Cinema
# Objetivo: Avaliar 5 filmes sob 4 critérios por 3 jurados cada, validando desqualificações por nota de corte e elegendo o vencedor do festival.

# Passo 1: Inicialização das variáveis para determinar o filme vencedor e melhor critério geral
vencedor_nome = "Nenhum filme qualificado"
vencedor_nota_final = -1.0

# Acumuladores de critérios para descobrir qual teve a maior média geral
soma_roteiro_total = 0.0
soma_direcao_total = 0.0
soma_atuacao_total = 0.0
soma_som_total = 0.0
total_votos_criterio = 0

# Passo 2: Laço principal para processar os 5 filmes
for f in range(1, 6):
    print(f"\n================ FILME {f} ================")
    nome_filme = input(f"Digite o nome do {f}º filme: ")
    
    # Flags e acumuladores do filme atual
    desqualificado = False
    soma_notas_jurados = 0.0
    
    # Passo 3: Laço para processar os 3 jurados
    for j in range(1, 4):
        print(f"  Jurado {j}:")
        
        # Leitura e validação de Roteiro
        rot_valido = False
        while not rot_valido:
            rot = input("    Digite a nota para Roteiro (0 a 10): ")
            rot = float(rot)
            if 0.0 <= rot <= 10.0:
                rot_valido = True
            else:
                print("    Erro: A nota deve ser de 0 a 10.")
                
        # Leitura e validação de Direção
        dir_valido = False
        while not dir_valido:
            dire = input("    Digite a nota para Direção (0 a 10): ")
            dire = float(dire)
            if 0.0 <= dire <= 10.0:
                dir_valido = True
            else:
                print("    Erro: A nota deve ser de 0 a 10.")
                
        # Leitura e validação de Atuação
        atu_valido = False
        while not atu_valido:
            atu = input("    Digite a nota para Atuação (0 a 10): ")
            atu = float(atu)
            if 0.0 <= atu <= 10.0:
                atu_valido = True
            else:
                print("    Erro: A nota deve ser de 0 a 10.")
                
        # Leitura e validação de Som
        som_valido = False
        while not som_valido:
            som = input("    Digite a nota para Som (0 a 10): ")
            som = float(som)
            if 0.0 <= som <= 10.0:
                som_valido = True
            else:
                print("    Erro: A nota deve ser de 0 a 10.")
                
        # Passo 4: Verificação de Nota de Corte (desqualificação automática se qualquer critério < 3)
        if rot < 3.0 or dire < 3.0 or atu < 3.0 or som < 3.0:
            desqualificado = True
            
        # Acumula nos totais globais de critérios
        soma_roteiro_total = soma_roteiro_total + rot
        soma_direcao_total = soma_direcao_total + dire
        soma_atuacao_total = soma_atuacao_total + atu
        soma_som_total = soma_som_total + som
        total_votos_criterio = total_votos_criterio + 1
        
        # Cálculo da nota ponderada do jurado
        nota_jurado = ((rot * 4.0) + (dire * 3.0) + (atu * 2.0) + (som * 1.0)) / 10.0
        soma_notas_jurados = soma_notas_jurados + nota_jurado
        
    # Passo 5: Cálculo da nota final e processamento da qualificação do filme
    if desqualificado:
        print(f"\n  Resultado do Filme: {nome_filme} foi DESQUALIFICADO por possuir nota de critério individual inferior a 3.")
    else:
        nota_final_filme = soma_notas_jurados / 3.0
        print(f"\n  Resultado do Filme: {nome_filme} - Média Final: {nota_final_filme:.2f} (Qualificado)")
        
        # Verifica se é o filme vencedor com maior pontuação
        if nota_final_filme > vencedor_nota_final:
            vencedor_nota_final = nota_final_filme
            vencedor_nome = nome_filme

# Passo 6: Cálculo das médias globais de critérios
media_roteiro = soma_roteiro_total / total_votos_criterio
media_direcao = soma_direcao_total / total_votos_criterio
media_atuacao = soma_atuacao_total / total_votos_criterio
media_som = soma_som_total / total_votos_criterio

# Determina qual critério obteve a maior média geral
if media_roteiro >= media_direcao and media_roteiro >= media_atuacao and media_roteiro >= media_som:
    melhor_criterio = "Roteiro"
    melhor_criterio_media = media_roteiro
elif media_direcao >= media_roteiro and media_direcao >= media_atuacao and media_direcao >= media_som:
    melhor_criterio = "Direção"
    melhor_criterio_media = media_direcao
elif media_atuacao >= media_roteiro and media_atuacao >= media_direcao and media_atuacao >= media_som:
    melhor_criterio = "Atuação"
    melhor_criterio_media = media_atuacao
else:
    melhor_criterio = "Som"
    melhor_criterio_media = media_som

# Passo 7: Exibição dos resultados finais do festival
print("\n================ VENCEDOR E RESULTADOS FINAIS ================")
print(f"Filme Vencedor do Festival: {vencedor_nome}")
if vencedor_nota_final != -1.0:
    print(f"Média Final do Vencedor: {vencedor_nota_final:.2f}")
print(f"Critério técnico de maior média geral: {melhor_criterio} (Média: {melhor_criterio_media:.2f})")
print("==============================================================")
