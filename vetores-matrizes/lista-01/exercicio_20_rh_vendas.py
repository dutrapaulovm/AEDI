# Exercício 20: Fechamento de Vendas e Salários do RH (Vetor de 5 Vagas)
# Objetivo: Calcular salários finais de 5 vendedores com base em um vetor de vendas e salários base fixos, aplicando bônus por meta e simulando comparação de desempenho com o líder.

# Passo 1: Inicialização dos vetores de salários base fixos e vendas
salarios_base = [2000.0] * 5
vendas = [0.0] * 5
cadastrado = False
meta_vendas = 0.0
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- FECHAMENTO DE FOLHA E DESEMPENHO DE VENDAS ---")
    print("1. Cadastrar Vendas e Meta da Empresa")
    print("2. Calcular Salários Finais e Bônus")
    print("3. Simulação de Disputa (Distância para o Líder)")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema de folha encerrado.")
        
    elif opcao == 1:
        # Passo 3: Cadastrar vendas (validação >= 0) e meta da empresa
        print("\n--- Registro de Vendas Mensais ---")
        meta_valida = False
        while not meta_valida:
            meta_vendas = input("Digite o valor da meta de vendas da empresa (R$): ")
            meta_vendas = float(meta_vendas)
            if meta_vendas > 0.0:
                meta_valida = True
            else:
                print("Erro: A meta deve ser positiva.")
                
        for i in range(5):
            valido = False
            while not valido:
                venda_val = input(f"Digite o valor de vendas do Vendedor {i+1} (R$): ")
                venda_val = float(venda_val)
                if venda_val >= 0.0:
                    vendas[i] = venda_val
                    valido = True
                else:
                    print("  Erro: O valor de vendas não pode ser negativo. Digite novamente.")
        cadastrado = True
        print("Vendas cadastradas com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Calcular salários finais aplicando regras de bônus baseadas na meta
        if not cadastrado:
            print("Erro: Cadastre as vendas primeiro (Opção 1).")
        else:
            print("\n--- FOLHA DE PAGAMENTOS COM BÔNUS ---")
            print(f"Meta Geral de Vendas: R$ {meta_vendas:.2f}")
            faturamento_total_empresa = 0.0
            
            for i in range(5):
                venda_atual = vendas[i]
                salario_fixo = salarios_base[i]
                faturamento_total_empresa = faturamento_total_empresa + venda_atual
                
                # Regras de bônus
                if venda_atual > (1.5 * meta_vendas):
                    bonus = 0.20 * salario_fixo  # Bônus de 20%
                    status_bonus = "Bônus de 20% (Meta Superada em +50%)"
                elif meta_vendas <= venda_atual <= (1.5 * meta_vendas):
                    bonus = 0.10 * salario_fixo  # Bônus de 10%
                    status_bonus = "Bônus de 10% (Meta Atingida)"
                else:
                    bonus = 0.0
                    status_bonus = "Sem Bônus"
                    
                salario_final = salario_fixo + bonus
                print(f"Vendedor {i+1} - Vendas: R$ {venda_atual:.2f} | Base: R$ {salario_fixo:.2f} | Final: R$ {salario_final:.2f} | ({status_bonus})")
                
            print(f"\nFaturamento Total Acumulado da Empresa: R$ {faturamento_total_empresa:.2f}")
            
    elif opcao == 3:
        # Passo 5: Laço aninhado para comparar a venda de cada um com o melhor vendedor
        if not cadastrado:
            print("Erro: Cadastre as vendas primeiro (Opção 1).")
        else:
            print("\n--- DISPUTA DE DESEMPENHO E DISTÂNCIA PARA O LÍDER ---")
            
            # Encontrar o maior volume de vendas
            melhor_venda = vendas[0]
            lider_num = 1
            for i in range(5):
                if vendas[i] > melhor_venda:
                    melhor_venda = vendas[i]
                    lider_num = i + 1
                    
            print(f"Líder de Vendas: Vendedor {lider_num} com R$ {melhor_venda:.2f}\n")
            
            for i in range(5):
                distancia = melhor_venda - vendas[i]
                if i + 1 == lider_num:
                    print(f"Vendedor {i+1} : É o Líder! Mantendo a ponta.")
                else:
                    print(f"Vendedor {i+1} : R$ {vendas[i]:.2f} em vendas | Distância para o topo: R$ {distancia:.2f} atrás.")
    else:
        print("Erro: Opção inválida.")
