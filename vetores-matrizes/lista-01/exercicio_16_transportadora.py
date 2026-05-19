# Exercício 16: Eficiência de Frota de Transportadora (Vetor de 5 Posições)
# Objetivo: Acompanhar o consumo de 5 veículos, validar limites de consumo, estimar custos em R$ para uma rota, e encontrar os veículos mais e menos econômicos.

# Passo 1: Inicialização das variáveis
consumo = [0.0] * 5
cadastrado = False
preco_combustivel = 0.0
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- SISTEMA DE GESTÃO DE EFICIÊNCIA DE FROTA ---")
    print("1. Cadastrar Consumo da Frota (5 Veículos)")
    print("2. Estimar Custos por Veículo para Viagem")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema de frota encerrado.")
        
    elif opcao == 1:
        # Passo 3: Cadastrar e validar consumo (deve ser > 0 e < 30) e preço de combustível
        print("\n--- Cadastro de Consumos ---")
        pr_valido = False
        while not pr_valido:
            preco_combustivel = input("Digite o preço do combustível por litro (R$): ")
            preco_combustivel = float(preco_combustivel)
            if preco_combustivel > 0.0:
                pr_valido = True
            else:
                print("Erro: O preço do combustível deve ser positivo.")
                
        for i in range(5):
            valido = False
            while not valido:
                cons_val = input(f"Digite o consumo do Veículo {i+1} (km/l): ")
                cons_val = float(cons_val)
                if 0.0 < cons_val < 30.0:
                    consumo[i] = cons_val
                    valido = True
                else:
                    print("  Erro: O consumo deve ser maior que 0 e menor que 30 km/l. Digite novamente.")
        cadastrado = True
        print("Frota cadastrada com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Estimar custos para uma viagem informada e identificar mais/menos econômicos
        if not cadastrado:
            print("Erro: Cadastre a frota primeiro (Opção 1).")
        else:
            print("\n--- Estimativa de Custos de Viagem ---")
            dist_valido = False
            distancia = 0.0
            while not dist_valido:
                distancia = input("Digite a distância total a ser percorrida (km): ")
                distancia = float(distancia)
                if distancia > 0.0:
                    dist_valido = True
                else:
                    print("Erro: A distância deve ser positiva.")
                    
            # Passo 5: Encontrar veículo mais econômico (maior km/l) e menos econômico (menor km/l)
            mais_economico_val = consumo[0]
            mais_economico_idx = 0
            menos_economico_val = consumo[0]
            menos_economico_idx = 0
            
            for i in range(5):
                if consumo[i] > mais_economico_val:
                    mais_economico_val = consumo[i]
                    mais_economico_idx = i
                if consumo[i] < menos_economico_val:
                    menos_economico_val = consumo[i]
                    menos_economico_idx = i
                    
            # Exibir custos individuais
            print("\nCustos Estimados da Viagem por Veículo:")
            for i in range(5):
                # Custo = (Distância / Consumo) * Preço do Litro
                litros_gastos = distancia / consumo[i]
                custo_estimado = litros_gastos * preco_combustivel
                print(f"  Veículo {i+1} : Consumo: {consumo[i]:.1f} km/l | Custo: R$ {custo_estimado:.2f} ({litros_gastos:.1f} litros)")
                
            print(f"\nVeículo mais econômico: Veículo {mais_economico_idx+1} ({mais_economico_val:.1f} km/l)")
            print(f"Veículo menos econômico: Veículo {menos_economico_idx+1} ({menos_economico_val:.1f} km/l)")
    else:
        print("Erro: Opção inválida.")
