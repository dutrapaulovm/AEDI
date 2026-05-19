# Exercício 12: Gerenciamento de Rede de Hotéis
# Objetivo: Controlar a ocupação e faturamento de 2 hotéis com 3 andares e 5 quartos cada, sem usar listas, dicionários ou vetores.

# Passo 1: Inicialização das 60 variáveis escalares de estado (status: 1=Ocupado, 2=Livre, 3=Manutenção)
h1_a1_q1_status = 2; h1_a1_q1_diaria = 100.0
h1_a1_q2_status = 2; h1_a1_q2_diaria = 100.0
h1_a1_q3_status = 2; h1_a1_q3_diaria = 100.0
h1_a1_q4_status = 2; h1_a1_q4_diaria = 100.0
h1_a1_q5_status = 2; h1_a1_q5_diaria = 100.0

h1_a2_q1_status = 2; h1_a2_q1_diaria = 100.0
h1_a2_q2_status = 2; h1_a2_q2_diaria = 100.0
h1_a2_q3_status = 2; h1_a2_q3_diaria = 100.0
h1_a2_q4_status = 2; h1_a2_q4_diaria = 100.0
h1_a2_q5_status = 2; h1_a2_q5_diaria = 100.0

h1_a3_q1_status = 2; h1_a3_q1_diaria = 100.0
h1_a3_q2_status = 2; h1_a3_q2_diaria = 100.0
h1_a3_q3_status = 2; h1_a3_q3_diaria = 100.0
h1_a3_q4_status = 2; h1_a3_q4_diaria = 100.0
h1_a3_q5_status = 2; h1_a3_q5_diaria = 100.0

h2_a1_q1_status = 2; h2_a1_q1_diaria = 100.0
h2_a1_q2_status = 2; h2_a1_q2_diaria = 100.0
h2_a1_q3_status = 2; h2_a1_q3_diaria = 100.0
h2_a1_q4_status = 2; h2_a1_q4_diaria = 100.0
h2_a1_q5_status = 2; h2_a1_q5_diaria = 100.0

h2_a2_q1_status = 2; h2_a2_q1_diaria = 100.0
h2_a2_q2_status = 2; h2_a2_q2_diaria = 100.0
h2_a2_q3_status = 2; h2_a2_q3_diaria = 100.0
h2_a2_q4_status = 2; h2_a2_q4_diaria = 100.0
h2_a2_q5_status = 2; h2_a2_q5_diaria = 100.0

h2_a3_q1_status = 2; h2_a3_q1_diaria = 100.0
h2_a3_q2_status = 2; h2_a3_q2_diaria = 100.0
h2_a3_q3_status = 2; h2_a3_q3_diaria = 100.0
h2_a3_q4_status = 2; h2_a3_q4_diaria = 100.0
h2_a3_q5_status = 2; h2_a3_q5_diaria = 100.0

# Passo 2: Laço principal do menu de gerenciamento do hotel
hotel_ativo = True
while hotel_ativo:
    print("\n=== Menu de Gerenciamento da Rede de Hotéis ===")
    print("1 - Realizar Check-in (Ocupar Quarto)")
    print("2 - Realizar Check-out (Liberar Quarto)")
    print("3 - Gerar Relatório de Ocupação e Receita")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")
    opcao = int(opcao)
    
    if opcao == 4:
        hotel_ativo = False
        print("Sistema hoteleiro encerrado.")
    elif opcao == 1 or opcao == 2:
        # Check-in ou Check-out
        # Passo 3: Leitura e validação da posição do quarto
        pos_valida = False
        while not pos_valida:
            h = input("Digite o Hotel (1 ou 2): ")
            h = int(h)
            a = input("Digite o Andar (1, 2 ou 3): ")
            a = int(a)
            q = input("Digite o Quarto (1 a 5): ")
            q = int(q)
            
            if 1 <= h <= 2 and 1 <= a <= 3 and 1 <= q <= 5:
                pos_valida = True
            else:
                print("Erro: Posição inválida! Tente novamente.")
                
        # Obter o status atual e aplicar Check-in/Check-out
        if h == 1:
            if a == 1:
                if q == 1: status_atual = h1_a1_q1_status
                elif q == 2: status_atual = h1_a1_q2_status
                elif q == 3: status_atual = h1_a1_q3_status
                elif q == 4: status_atual = h1_a1_q4_status
                else: status_atual = h1_a1_q5_status
            elif a == 2:
                if q == 1: status_atual = h1_a2_q1_status
                elif q == 2: status_atual = h1_a2_q2_status
                elif q == 3: status_atual = h1_a2_q3_status
                elif q == 4: status_atual = h1_a2_q4_status
                else: status_atual = h1_a2_q5_status
            else:
                if q == 1: status_atual = h1_a3_q1_status
                elif q == 2: status_atual = h1_a3_q2_status
                elif q == 3: status_atual = h1_a3_q3_status
                elif q == 4: status_atual = h1_a3_q4_status
                else: status_atual = h1_a3_q5_status
        else:
            if a == 1:
                if q == 1: status_atual = h2_a1_q1_status
                elif q == 2: status_atual = h2_a1_q2_status
                elif q == 3: status_atual = h2_a1_q3_status
                elif q == 4: status_atual = h2_a1_q4_status
                else: status_atual = h2_a1_q5_status
            elif a == 2:
                if q == 1: status_atual = h2_a2_q1_status
                elif q == 2: status_atual = h2_a2_q2_status
                elif q == 3: status_atual = h2_a2_q3_status
                elif q == 4: status_atual = h2_a2_q4_status
                else: status_atual = h2_a2_q5_status
            else:
                if q == 1: status_atual = h2_a3_q1_status
                elif q == 2: status_atual = h2_a3_q2_status
                elif q == 3: status_atual = h2_a3_q3_status
                elif q == 4: status_atual = h2_a3_q4_status
                else: status_atual = h2_a3_q5_status
                
        # Lógica para CHECK-IN
        if opcao == 1:
            if status_atual == 2: # Livre
                novo_status = 1 # Ocupado
                print(f"Check-in realizado com sucesso no Hotel {h}, Andar {a}, Quarto {q}!")
            else:
                print("Erro: O quarto escolhido NÃO está livre (está Ocupado ou em Manutenção).")
                novo_status = status_atual
        # Lógica para CHECK-OUT
        else:
            if status_atual == 1: # Ocupado
                novo_status = 2 # Livre
                print(f"Check-out realizado com sucesso no Hotel {h}, Andar {a}, Quarto {q}!")
            else:
                print("Erro: O quarto escolhido NÃO está ocupado.")
                novo_status = status_atual
                
        # Atualizar a variável de status correta
        if h == 1:
            if a == 1:
                if q == 1: h1_a1_q1_status = novo_status
                elif q == 2: h1_a1_q2_status = novo_status
                elif q == 3: h1_a1_q3_status = novo_status
                elif q == 4: h1_a1_q4_status = novo_status
                else: h1_a1_q5_status = novo_status
            elif a == 2:
                if q == 1: h1_a2_q1_status = novo_status
                elif q == 2: h1_a2_q2_status = novo_status
                elif q == 3: h1_a2_q3_status = novo_status
                elif q == 4: h1_a2_q4_status = novo_status
                else: h1_a2_q5_status = novo_status
            else:
                if q == 1: h1_a3_q1_status = novo_status
                elif q == 2: h1_a3_q2_status = novo_status
                elif q == 3: h1_a3_q3_status = novo_status
                elif q == 4: h1_a3_q4_status = novo_status
                else: h1_a3_q5_status = novo_status
        else:
            if a == 1:
                if q == 1: h2_a1_q1_status = novo_status
                elif q == 2: h2_a1_q2_status = novo_status
                elif q == 3: h2_a1_q3_status = novo_status
                elif q == 4: h2_a1_q4_status = novo_status
                else: h2_a1_q5_status = novo_status
            elif a == 2:
                if q == 1: h2_a2_q1_status = novo_status
                elif q == 2: h2_a2_q2_status = novo_status
                elif q == 3: h2_a2_q3_status = novo_status
                elif q == 4: h2_a2_q4_status = novo_status
                else: h2_a2_q5_status = novo_status
            else:
                if q == 1: h2_a3_q1_status = novo_status
                elif q == 2: h2_a3_q2_status = novo_status
                elif q == 3: h2_a3_q3_status = novo_status
                elif q == 4: h2_a3_q4_status = novo_status
                else: h2_a3_q5_status = novo_status
                
    elif opcao == 3:
        # Relatório de ocupação e receita potencial vs real
        # Passo 4: Coleta de estatísticas acumulando manualmente
        receita_potencial_total = 0.0
        receita_real_atual = 0.0
        
        # Hotel 1, Andar 1
        h1_a1_ocupados = 0
        if h1_a1_q1_status == 1: h1_a1_ocupados += 1; receita_real_atual += h1_a1_q1_diaria
        if h1_a1_q2_status == 1: h1_a1_ocupados += 1; receita_real_atual += h1_a1_q2_diaria
        if h1_a1_q3_status == 1: h1_a1_ocupados += 1; receita_real_atual += h1_a1_q3_diaria
        if h1_a1_q4_status == 1: h1_a1_ocupados += 1; receita_real_atual += h1_a1_q4_diaria
        if h1_a1_q5_status == 1: h1_a1_ocupados += 1; receita_real_atual += h1_a1_q5_diaria
        receita_potencial_total += (h1_a1_q1_diaria + h1_a1_q2_diaria + h1_a1_q3_diaria + h1_a1_q4_diaria + h1_a1_q5_diaria)
        
        # Hotel 1, Andar 2
        h1_a2_ocupados = 0
        if h1_a2_q1_status == 1: h1_a2_ocupados += 1; receita_real_atual += h1_a2_q1_diaria
        if h1_a2_q2_status == 1: h1_a2_ocupados += 1; receita_real_atual += h1_a2_q2_diaria
        if h1_a2_q3_status == 1: h1_a2_ocupados += 1; receita_real_atual += h1_a2_q3_diaria
        if h1_a2_q4_status == 1: h1_a2_ocupados += 1; receita_real_atual += h1_a2_q4_diaria
        if h1_a2_q5_status == 1: h1_a2_ocupados += 1; receita_real_atual += h1_a2_q5_diaria
        receita_potencial_total += (h1_a2_q1_diaria + h1_a2_q2_diaria + h1_a2_q3_diaria + h1_a2_q4_diaria + h1_a2_q5_diaria)
        
        # Hotel 1, Andar 3
        h1_a3_ocupados = 0
        if h1_a3_q1_status == 1: h1_a3_ocupados += 1; receita_real_atual += h1_a3_q1_diaria
        if h1_a3_q2_status == 1: h1_a3_ocupados += 1; receita_real_atual += h1_a3_q2_diaria
        if h1_a3_q3_status == 1: h1_a3_ocupados += 1; receita_real_atual += h1_a3_q3_diaria
        if h1_a3_q4_status == 1: h1_a3_ocupados += 1; receita_real_atual += h1_a3_q4_diaria
        if h1_a3_q5_status == 1: h1_a3_ocupados += 1; receita_real_atual += h1_a3_q5_diaria
        receita_potencial_total += (h1_a3_q1_diaria + h1_a3_q2_diaria + h1_a3_q3_diaria + h1_a3_q4_diaria + h1_a3_q5_diaria)
        
        # Hotel 2, Andar 1
        h2_a1_ocupados = 0
        if h2_a1_q1_status == 1: h2_a1_ocupados += 1; receita_real_atual += h2_a1_q1_diaria
        if h2_a1_q2_status == 1: h2_a1_ocupados += 1; receita_real_atual += h2_a1_q2_diaria
        if h2_a1_q3_status == 1: h2_a1_ocupados += 1; receita_real_atual += h2_a1_q3_diaria
        if h2_a1_q4_status == 1: h2_a1_ocupados += 1; receita_real_atual += h2_a1_q4_diaria
        if h2_a1_q5_status == 1: h2_a1_ocupados += 1; receita_real_atual += h2_a1_q5_diaria
        receita_potencial_total += (h2_a1_q1_diaria + h2_a1_q2_diaria + h2_a1_q3_diaria + h2_a1_q4_diaria + h2_a1_q5_diaria)
        
        # Hotel 2, Andar 2
        h2_a2_ocupados = 0
        if h2_a2_q1_status == 1: h2_a2_ocupados += 1; receita_real_atual += h2_a2_q1_diaria
        if h2_a2_q2_status == 1: h2_a2_ocupados += 1; receita_real_atual += h2_a2_q2_diaria
        if h2_a2_q3_status == 1: h2_a2_ocupados += 1; receita_real_atual += h2_a2_q3_diaria
        if h2_a2_q4_status == 1: h2_a2_ocupados += 1; receita_real_atual += h2_a2_q4_diaria
        if h2_a2_q5_status == 1: h2_a2_ocupados += 1; receita_real_atual += h2_a2_q5_diaria
        receita_potencial_total += (h2_a2_q1_diaria + h2_a2_q2_diaria + h2_a2_q3_diaria + h2_a2_q4_diaria + h2_a2_q5_diaria)
        
        # Hotel 2, Andar 3
        h2_a3_ocupados = 0
        if h2_a3_q1_status == 1: h2_a3_ocupados += 1; receita_real_atual += h2_a3_q1_diaria
        if h2_a3_q2_status == 1: h2_a3_ocupados += 1; receita_real_atual += h2_a3_q2_diaria
        if h2_a3_q3_status == 1: h2_a3_ocupados += 1; receita_real_atual += h2_a3_q3_diaria
        if h2_a3_q4_status == 1: h2_a3_ocupados += 1; receita_real_atual += h2_a3_q4_diaria
        if h2_a3_q5_status == 1: h2_a3_ocupados += 1; receita_real_atual += h2_a3_q5_diaria
        receita_potencial_total += (h2_a3_q1_diaria + h2_a3_q2_diaria + h2_a3_q3_diaria + h2_a3_q4_diaria + h2_a3_q5_diaria)
        
        # Passo 5: Exibição do relatório de Ocupação e Receita
        print("\n--- Relatório Financeiro da Rede ---")
        print(f"Receita Potencial Máxima (100% Ocupação): R$ {receita_potencial_total:.2f}")
        print(f"Receita Real Atual: R$ {receita_real_atual:.2f}")
        ocupacao_geral = ((h1_a1_ocupados + h1_a2_ocupados + h1_a3_ocupados + h2_a1_ocupados + h2_a2_ocupados + h2_a3_ocupados) / 30.0) * 100.0
        print(f"Taxa de Ocupação Geral: {ocupacao_geral:.1f}%")
        
        # Sobretaxa por Alta Ocupação (ocupação de andar > 80% ou seja, >= 4 quartos ocupados de 5)
        # Se um andar tem >= 4 quartos ocupados, as diárias de novos check-ins daquele andar sobem 15%
        print("\n--- Gráfico Textual de Ocupação por Andar (O=Ocupado, L=Livre, M=Manutenção) ---")
        
        # Hotel 1
        print("HOTEL 1:")
        print(f"  Andar 3: [{'O' if h1_a3_q1_status==1 else 'L' if h1_a3_q1_status==2 else 'M'}{'O' if h1_a3_q2_status==1 else 'L' if h1_a3_q2_status==2 else 'M'}{'O' if h1_a3_q3_status==1 else 'L' if h1_a3_q3_status==2 else 'M'}{'O' if h1_a3_q4_status==1 else 'L' if h1_a3_q4_status==2 else 'M'}{'O' if h1_a3_q5_status==1 else 'L' if h1_a3_q5_status==2 else 'M'}] - Ocupação: {h1_a3_ocupados*20}%")
        print(f"  Andar 2: [{'O' if h1_a2_q1_status==1 else 'L' if h1_a2_q1_status==2 else 'M'}{'O' if h1_a2_q2_status==1 else 'L' if h1_a2_q2_status==2 else 'M'}{'O' if h1_a2_q3_status==1 else 'L' if h1_a2_q3_status==2 else 'M'}{'O' if h1_a2_q4_status==1 else 'L' if h1_a2_q4_status==2 else 'M'}{'O' if h1_a2_q5_status==1 else 'L' if h1_a2_q5_status==2 else 'M'}] - Ocupação: {h1_a2_ocupados*20}%")
        print(f"  Andar 1: [{'O' if h1_a1_q1_status==1 else 'L' if h1_a1_q1_status==2 else 'M'}{'O' if h1_a1_q2_status==1 else 'L' if h1_a1_q2_status==2 else 'M'}{'O' if h1_a1_q3_status==1 else 'L' if h1_a1_q3_status==2 else 'M'}{'O' if h1_a1_q4_status==1 else 'L' if h1_a1_q4_status==2 else 'M'}{'O' if h1_a1_q5_status==1 else 'L' if h1_a1_q5_status==2 else 'M'}] - Ocupação: {h1_a1_ocupados*20}%")
        
        # Hotel 2
        print("HOTEL 2:")
        print(f"  Andar 3: [{'O' if h2_a3_q1_status==1 else 'L' if h2_a3_q1_status==2 else 'M'}{'O' if h2_a3_q2_status==1 else 'L' if h2_a3_q2_status==2 else 'M'}{'O' if h2_a3_q3_status==1 else 'L' if h2_a3_q3_status==2 else 'M'}{'O' if h2_a3_q4_status==1 else 'L' if h2_a3_q4_status==2 else 'M'}{'O' if h2_a3_q5_status==1 else 'L' if h2_a3_q5_status==2 else 'M'}] - Ocupação: {h2_a3_ocupados*20}%")
        print(f"  Andar 2: [{'O' if h2_a2_q1_status==1 else 'L' if h2_a2_q1_status==2 else 'M'}{'O' if h2_a2_q2_status==1 else 'L' if h2_a2_q2_status==2 else 'M'}{'O' if h2_a2_q3_status==1 else 'L' if h2_a2_q3_status==2 else 'M'}{'O' if h2_a2_q4_status==1 else 'L' if h2_a2_q4_status==2 else 'M'}{'O' if h2_a2_q5_status==1 else 'L' if h2_a2_q5_status==2 else 'M'}] - Ocupação: {h2_a2_ocupados*20}%")
        print(f"  Andar 1: [{'O' if h2_a1_q1_status==1 else 'L' if h2_a1_q1_status==2 else 'M'}{'O' if h2_a1_q2_status==1 else 'L' if h2_a1_q2_status==2 else 'M'}{'O' if h2_a1_q3_status==1 else 'L' if h2_a1_q3_status==2 else 'M'}{'O' if h2_a1_q4_status==1 else 'L' if h2_a1_q4_status==2 else 'M'}{'O' if h2_a1_q5_status==1 else 'L' if h2_a1_q5_status==2 else 'M'}] - Ocupação: {h2_a1_ocupados*20}%")
        
        # Atualização de diárias para andares de alta ocupação (demanda > 80%, ou seja, ocupados >= 4 de 5)
        # Se ocupados == 4 ou 5, a diária daquele andar específico aumenta 15% para novas diárias
        if h1_a1_ocupados >= 4: h1_a1_q1_diaria=h1_a1_q2_diaria=h1_a1_q3_diaria=h1_a1_q4_diaria=h1_a1_q5_diaria=115.00
        else: h1_a1_q1_diaria=h1_a1_q2_diaria=h1_a1_q3_diaria=h1_a1_q4_diaria=h1_a1_q5_diaria=100.00
        
        if h1_a2_ocupados >= 4: h1_a2_q1_diaria=h1_a2_q2_diaria=h1_a2_q3_diaria=h1_a2_q4_diaria=h1_a2_q5_diaria=115.00
        else: h1_a2_q1_diaria=h1_a2_q2_diaria=h1_a2_q3_diaria=h1_a2_q4_diaria=h1_a2_q5_diaria=100.00
        
        if h1_a3_ocupados >= 4: h1_a3_q1_diaria=h1_a3_q2_diaria=h1_a3_q3_diaria=h1_a3_q4_diaria=h1_a3_q5_diaria=115.00
        else: h1_a3_q1_diaria=h1_a3_q2_diaria=h1_a3_q3_diaria=h1_a3_q4_diaria=h1_a3_q5_diaria=100.00
        
        if h2_a1_ocupados >= 4: h2_a1_q1_diaria=h2_a1_q2_diaria=h2_a1_q3_diaria=h2_a1_q4_diaria=h2_a1_q5_diaria=115.00
        else: h2_a1_q1_diaria=h2_a1_q2_diaria=h2_a1_q3_diaria=h2_a1_q4_diaria=h2_a1_q5_diaria=100.00
        
        if h2_a2_ocupados >= 4: h2_a2_q1_diaria=h2_a2_q2_diaria=h2_a2_q3_diaria=h2_a2_q4_diaria=h2_a2_q5_diaria=115.00
        else: h2_a2_q1_diaria=h2_a2_q2_diaria=h2_a2_q3_diaria=h2_a2_q4_diaria=h2_a2_q5_diaria=100.00
        
        if h2_a3_ocupados >= 4: h2_a3_q1_diaria=h2_a3_q2_diaria=h2_a3_q3_diaria=h2_a3_q4_diaria=h2_a3_q5_diaria=115.00
        else: h2_a3_q1_diaria=h2_a3_q2_diaria=h2_a3_q3_diaria=h2_a3_q4_diaria=h2_a3_q5_diaria=100.00
    else:
        print("Erro: Opção inválida do menu.")
