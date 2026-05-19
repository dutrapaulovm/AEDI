# Exercício 17: Ocupação de Imóveis e Desconto de Condomínio (Matriz 3x4)
# Objetivo: Controlar ocupação de 3 prédios com 4 apartamentos cada, exibindo mapa de ocupação e aplicando desconto de 10% na taxa de condomínio se a taxa do prédio for superior a 75%.

# Passo 1: Inicialização da matriz 3x4 com zeros (0: Vazio, 1: Alugado)
apartamentos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
condominio_base = 500.0
cadastrado = False
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- GESTÃO DE IMÓVEIS IMOBILIÁRIA (3x4) ---")
    print("1. Cadastrar Ocupação Inicial e Condomínio Base")
    print("2. Registrar Aluguel de Apartamento")
    print("3. Mapa de Ocupação e Descontos de Condomínio")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema imobiliário encerrado.")
        
    elif opcao == 1:
        # Passo 3: Cadastro inicial de ocupações (0 ou 1) e condomínio
        print("\n--- Cadastro de Ocupações ---")
        cond_valido = False
        while not cond_valido:
            condominio_base = input("Digite o valor do condomínio base (R$): ")
            condominio_base = float(condominio_base)
            if condominio_base > 0.0:
                cond_valido = True
            else:
                print("Erro: O condomínio base deve ser maior que zero.")
                
        for i in range(3):
            print(f"Prédio {i+1}:")
            for j in range(4):
                valido = False
                while not valido:
                    status = input(f"  Apartamento {j+1} (0 para Vazio, 1 para Alugado): ")
                    status = int(status)
                    if status == 0 or status == 1:
                        apartamentos[i][j] = status
                        valido = True
                    else:
                        print("  Erro: Insira apenas 0 ou 1.")
        cadastrado = True
        print("Registros de ocupação salvos!")
        
    elif opcao == 2:
        # Passo 4: Aluguel de apartamento com validação de status e de índices
        if not cadastrado:
            print("Erro: Faça a ocupação inicial primeiro (Opção 1).")
        else:
            print("\n--- Registrar Novo Contrato de Aluguel ---")
            
            # Validação do prédio (1 a 3)
            p_valido = False
            while not p_valido:
                predio_idx = input("Digite o número do prédio (1 a 3): ")
                predio_idx = int(predio_idx)
                if 1 <= predio_idx <= 3:
                    predio_idx = predio_idx - 1
                    p_valido = True
                else:
                    print("Erro: Prédio inválido.")
                    
            # Validação do apartamento (1 a 4)
            a_valido = False
            while not a_valido:
                apt_idx = input("Digite o número do apartamento (1 a 4): ")
                apt_idx = int(apt_idx)
                if 1 <= apt_idx <= 4:
                    apt_idx = apt_idx - 1
                    a_valido = True
                else:
                    print("Erro: Apartamento inválido.")
                    
            # Validação: não alugar apartamento já ocupado (1)
            if apartamentos[predio_idx][apt_idx] == 1:
                print("Erro: Este apartamento já está alugado (Ocupado)! Escolha outro.")
            else:
                apartamentos[predio_idx][apt_idx] = 1
                print(f"Sucesso: Apartamento {apt_idx+1} do Prédio {predio_idx+1} alugado com sucesso!")
                
    elif opcao == 3:
        # Passo 5: Gráfico visual de ocupação e cálculo de condomínio com desconto
        if not cadastrado:
            print("Erro: Cadastre os dados primeiro (Opção 1).")
        else:
            print("\n--- MAPA GRÁFICO DE OCUPAÇÃO ---")
            for i in range(3):
                linha_grafica = ""
                for j in range(4):
                    if apartamentos[i][j] == 1:
                        linha_grafica = linha_grafica + " [X] "
                    else:
                        linha_grafica = linha_grafica + " [ ] "
                print(f"Prédio {i+1}: {linha_grafica}")
                
            print("\n--- TABELA DE TAXAS DE CONDOMÍNIO ---")
            for i in range(3):
                alugados = 0
                for j in range(4):
                    if apartamentos[i][j] == 1:
                        alugados = alugados + 1
                        
                taxa_ocupacao = (alugados / 4.0) * 100.0
                
                # Regra de desconto: ocupação > 75% ganha 10% de desconto
                if taxa_ocupacao > 75.0:
                    condominio_final = condominio_base * 0.90
                    desconto_txt = "(10% de Desconto Aplicado!)"
                else:
                    condominio_final = condominio_base
                    desconto_txt = ""
                    
                print(f"Prédio {i+1} : Ocupação: {taxa_ocupacao:.1f}% | Condomínio: R$ {condominio_final:.2f} {desconto_txt}")
    else:
        print("Erro: Opção inválida.")
