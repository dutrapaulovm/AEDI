# Exercício 10: Simulador de Ecossistema Predator-Prey (Coelhos e Lobos)
# Objetivo: Simular a evolução demográfica de coelhos e lobos durante 10 gerações, processando 3 subperíodos sazonais por geração.

# Passo 1: Inicialização do menu principal do simulador de ecossistema
simulador_ativo = True

# Parâmetros padrão iniciais
coelhos_iniciais = 100
lobos_iniciais = 20
taxa_natalidade = 0.10  # 10% de natalidade de coelhos por subperíodo
taxa_caca = 1.5         # Cada lobo caça/consome 1.5 coelhos por subperíodo

while simulador_ativo:
    print("\n=== Simulador de Ecossistema Predator-Prey ===")
    print("1 - Executar Simulação com Parâmetros Atuais")
    print("2 - Ajustar Parâmetros Demográficos")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")
    opcao = int(opcao)
    
    if opcao == 3:
        simulador_ativo = False
        print("Simulador de ecossistema encerrado.")
    elif opcao == 2:
        # Passo 2: Ajuste e validação dos parâmetros
        par_valido = False
        while not par_valido:
            coelhos_iniciais = input("Digite a população inicial de coelhos (> 0): ")
            coelhos_iniciais = int(coelhos_iniciais)
            lobos_iniciais = input("Digite a população inicial de lobos (> 0): ")
            lobos_iniciais = int(lobos_iniciais)
            
            taxa_natalidade = input("Digite a taxa de natalidade dos coelhos (ex: 0.10 para 10%): ")
            taxa_natalidade = float(taxa_natalidade)
            taxa_caca = input("Digite a taxa de caça dos lobos (quantos coelhos um lobo caça, ex: 1.5): ")
            taxa_caca = float(taxa_caca)
            
            if coelhos_iniciais > 0 and lobos_iniciais > 0 and taxa_natalidade >= 0 and taxa_caca >= 0:
                par_valido = True
                print("Parâmetros atualizados com sucesso!")
            else:
                print("Erro: Populações iniciais devem ser maiores que zero e taxas não podem ser negativas.")
                
    elif opcao == 1:
        # Passo 3: Executar a simulação de 10 gerações
        coelhos = coelhos_iniciais
        lobos = lobos_iniciais
        
        print("\n--- Iniciando Simulação ---")
        print(f"Estado Inicial: Coelhos = {coelhos} | Lobos = {lobos}")
        
        # Laço para as 10 gerações
        for geracao in range(1, 11):
            print(f"\nGeração {geracao}:")
            
            # Laço interno para os 3 subperíodos sazonais
            for sub in range(1, 4):
                # Aumento da população de coelhos por natalidade
                nascimentos = coelhos * taxa_natalidade
                coelhos = coelhos + nascimentos
                
                # Redução da população de coelhos por caça dos lobos
                presos_cacados = lobos * taxa_caca
                coelhos = coelhos - presos_cacados
                
                # Evita populações de coelhos negativas
                if coelhos < 0:
                    coelhos = 0
                    
                # Condição de Fome dos Lobos: se coelhos caírem abaixo de 10
                if coelhos < 10:
                    fome_mortes = lobos * 0.20  # Redução de 20% dos lobos por fome
                    lobos = lobos - fome_mortes
                    if lobos < 0:
                        lobos = 0
                        
                print(f"  Subperíodo {sub}: Coelhos = {int(coelhos)} | Lobos = {int(lobos)}")
                
            # Exibição do status final da geração
            print(f"Resultado Final da Geração {geracao}: Coelhos = {int(coelhos)} | Lobos = {int(lobos)}")
            
            # Se ambas populações forem extintas, encerra mais cedo
            if coelhos == 0 and lobos == 0:
                print("Extinção completa no ecossistema! A simulação foi encerrada precocemente.")
                break
        print("\n------------------------------")
    else:
        print("Erro: Opção inválida do menu.")
