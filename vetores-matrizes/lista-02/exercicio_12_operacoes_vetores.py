# Exercício 12: Soma e Subtração de Vetores U e V
# Objetivo: Definir tamanho N, receber vetores U e V com validação de termos no intervalo [-50, 50], calcular W = U + V e Z = U - V, e exibir os quatro vetores lado a lado.

# Passo 1: Obtenção do tamanho N comum com validação (> 0)
print("--- Configuração de Operações Vetoriais ---")
n_valido = False
n = 0
while not n_valido:
    n = input("Digite o tamanho N dos vetores: ")
    n = int(n)
    if n > 0:
        n_valido = True
    else:
        print("Erro: O tamanho deve ser maior que zero.")

# Passo 2: Inicialização dos vetores
vetor_u = [0.0] * n
vetor_v = [0.0] * n
vetor_w = [0.0] * n
vetor_z = [0.0] * n

cadastrado = False
calculado = False
rodando = True

# Passo 3: Laço principal do menu interativo
while rodando:
    print("\n--- MENU DE OPERAÇÕES DE VETORES ---")
    print("1. Atualizar Vetores (Inserir U e V)")
    print("2. Calcular Resultados (W = U + V e Z = U - V)")
    print("3. Exibir Resultados Lado a Lado")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema vetorial encerrado.")
        
    elif opcao == 1:
        # Preenchimento de U e V com validações [-50.0, 50.0]
        print(f"\n--- Cadastro do Vetor U (N = {n}) ---")
        for i in range(n):
            valido = False
            while not valido:
                val = input(f"  Digite U[{i}] (de -50 a 50): ")
                val = float(val)
                if -50.0 <= val <= 50.0:
                    vetor_u[i] = val
                    valido = True
                else:
                    print("    Erro: O valor deve estar contido no intervalo [-50.0, 50.0].")
                    
        print(f"\n--- Cadastro do Vetor V (N = {n}) ---")
        for i in range(n):
            valido = False
            while not valido:
                val = input(f"  Digite V[{i}] (de -50 a 50): ")
                val = float(val)
                if -50.0 <= val <= 50.0:
                    vetor_v[i] = val
                    valido = True
                else:
                    print("    Erro: O valor deve estar contido no intervalo [-50.0, 50.0].")
                    
        cadastrado = True
        calculado = False  # Reseta o cálculo já que os vetores mudaram
        print("Vetores U e V atualizados com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Calcular W = U + V e Z = U - V
        if not cadastrado:
            print("Erro: Cadastre e atualize os dados de U e V primeiro (Opção 1).")
        else:
            for i in range(n):
                vetor_w[i] = vetor_u[i] + vetor_v[i]
                vetor_z[i] = vetor_u[i] - vetor_v[i]
            calculado = True
            print("Cálculos de W (soma) e Z (subtração) executados!")
            
    elif opcao == 3:
        # Passo 5: Exibição estruturada dos 4 vetores lado a lado
        if not calculado:
            print("Erro: Execute os cálculos primeiro (Opção 2).")
        else:
            print("\n--- VISUALIZAÇÃO DOS RESULTADOS LADO A LADO ---")
            print(" Índice |   Vetor U   |   Vetor V   | Vetor W (U+V) | Vetor Z (U-V)")
            print("--------|-------------|-------------|---------------|---------------")
            for i in range(n):
                u_val = vetor_u[i]
                v_val = vetor_v[i]
                w_val = vetor_w[i]
                z_val = vetor_z[i]
                print(f"   {i:2d}   |   {u_val:7.2f}   |   {v_val:7.2f}   |    {w_val:7.2f}    |    {z_val:7.2f}")
    else:
        print("Erro: Opção inválida.")
