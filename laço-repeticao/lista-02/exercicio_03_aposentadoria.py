# Exercício 3: Simulador de Aposentadoria e Investimentos
# Objetivo: Simular rendimentos mensais e anuais de um investimento de acordo com o perfil selecionado (Conservador, Moderado ou Arrojado).

import random

# Passo 1: Inicialização do laço principal do menu contínuo
rodando = True
while rodando:
    print("\n=== Simulador de Aposentadoria ===")
    print("1 - Iniciar Nova Simulação")
    print("2 - Sair do Programa")
    
    opcao_menu = input("Escolha uma opção: ")
    opcao_menu = int(opcao_menu)
    
    if opcao_menu == 2:
        rodando = False
        print("Sistema encerrado com sucesso!")
    elif opcao_menu == 1:
        # Passo 2: Entrada e validação do nome do investidor
        nome = input("\nDigite o nome do investidor: ")
        
        # Entrada e validação do saldo inicial
        saldo_valido = False
        while not saldo_valido:
            saldo_inicial = input("Digite o saldo inicial da conta (R$): ")
            saldo_inicial = float(saldo_inicial)
            if saldo_inicial >= 0.0:
                saldo_valido = True
            else:
                print("Erro: O saldo inicial não pode ser negativo.")
                
        # Entrada e validação do perfil de investimento
        perfil_valido = False
        while not perfil_valido:
            print("\nPerfis de Investimento:")
            print("1 - Conservador (0.5% ao mês fixo)")
            print("2 - Moderado (0.8% ao mês fixo)")
            print("3 - Arrojado (Variável entre -1% e 3% ao mês)")
            perfil = input("Escolha o perfil de investimento (1 a 3): ")
            perfil = int(perfil)
            if 1 <= perfil <= 3:
                perfil_valido = True
            else:
                print("Erro: Opção inválida de perfil.")
                
        # Entrada e validação da quantidade de anos
        anos_valido = False
        while not anos_valido:
            anos = input("Digite a quantidade de anos para a simulação: ")
            anos = int(anos)
            if anos > 0:
                anos_valido = True
            else:
                print("Erro: A quantidade de anos deve ser maior que zero.")
                
        # Passo 3: Processamento dos rendimentos ano a ano e mês a mês
        saldo_atual = saldo_inicial
        
        for ano in range(1, anos + 1):
            print(f"\n--- Progresso do Ano {ano} ---")
            
            # Loop interno para os 12 meses do ano atual
            for mes in range(1, 13):
                # Definição da taxa de rendimento baseada no perfil
                if perfil == 1:
                    rendimento = 0.005  # 0.5% fixo
                elif perfil == 2:
                    rendimento = 0.008  # 0.8% fixo
                else:
                    # Arrojado: taxa variável aleatória entre -1% e 3%
                    rendimento = random.uniform(-0.01, 0.03)
                    
                # Atualização do saldo pelo rendimento do mês
                saldo_anterior = saldo_atual
                saldo_atual = saldo_atual * (1.0 + rendimento)
                rendimento_ganho = saldo_atual - saldo_anterior
                
                # Exibe detalhes apenas se for perfil arrojado ou primeiro ano para não poluir muito a tela
                if perfil == 3 or ano == 1:
                    print(f"  Mês {mes:02d}: Taxa={rendimento*100:+.2f}% | Rendimento=R$ {rendimento_ganho:.2f} | Saldo=R$ {saldo_atual:.2f}")
            
            # Exibição do resumo acumulado ao final de cada ano
            print(f"Patrimônio ao final do Ano {ano}: R$ {saldo_atual:.2f}")
            
        # Relatório Final da Simulação
        print(f"\n--- Relatório Final da Simulação para {nome} ---")
        print(f"Saldo Inicial: R$ {saldo_inicial:.2f}")
        print(f"Patrimônio Final após {anos} anos: R$ {saldo_atual:.2f}")
        lucro_total = saldo_atual - saldo_inicial
        print(f"Rendimento Total Acumulado: R$ {lucro_total:.2f}")
    else:
        print("Erro: Opção inválida do menu principal.")
