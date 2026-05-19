# Exercício 28: Filtro de Suavização de Imagem - Kernel (Matriz 5x5)
# Objetivo: Cadastrar intensidades de cinza (0 a 255) em um grid 5x5, aplicar um kernel de suavização (média dos 8 vizinhos) e exibir as imagens lado a lado.

# Passo 1: Inicialização da matriz original e da matriz filtrada 5x5
imagem = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
filtrada = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
cadastrado = False
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- PROCESSADOR DE IMAGENS - KERNEL DE SUAVIZAÇÃO (5x5) ---")
    print("1. Cadastrar Intensidades de Pixels da Imagem")
    print("2. Aplicar Filtro de Suavização (Média de 8 Vizinhos)")
    print("3. Visualizar Imagens Original e Filtrada Lado a Lado")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Processador de imagens encerrado.")
        
    elif opcao == 1:
        # Passo 3: Cadastrar e validar intensidades dos pixels (0 a 255)
        print("\n--- Cadastro de Pixels (0: Preto, 255: Branco) ---")
        for i in range(5):
            print(f"Linha {i+1} do Grid de Pixels:")
            for j in range(5):
                valido = False
                while not valido:
                    pixel = input(f"  Pixel [{i+1}][{j+1}]: ")
                    pixel = int(pixel)
                    if 0 <= pixel <= 255:
                        imagem[i][j] = pixel
                        valido = True
                    else:
                        print("  Erro: A intensidade do pixel deve estar no intervalo [0, 255]. Digite novamente.")
        cadastrado = True
        print("Imagem cadastrada com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Aplicar o filtro de média dos 8 vizinhos em laços aninhados para pixels internos (exceto bordas)
        if not cadastrado:
            print("Erro: Cadastre os pixels da imagem original primeiro (Opção 1).")
        else:
            print("\n--- Aplicando Filtro de Suavização ---")
            
            # Copia os pixels das bordas da imagem original para a imagem filtrada
            for i in range(5):
                for j in range(5):
                    if i == 0 or i == 4 or j == 0 or j == 4:
                        filtrada[i][j] = imagem[i][j]
                        
            # Aplica o kernel apenas nos pixels internos (Linhas 1 a 3, Colunas 1 a 3)
            for i in range(1, 4):
                for j in range(1, 4):
                    # Soma das 8 células vizinhas
                    soma_vizinhos = (
                        imagem[i-1][j-1] + imagem[i-1][j] + imagem[i-1][j+1] +
                        imagem[i][j-1]                     + imagem[i][j+1] +
                        imagem[i+1][j-1] + imagem[i+1][j] + imagem[i+1][j+1]
                    )
                    # Calcula a média (divisão inteira para pixel discreto)
                    filtrada[i][j] = soma_vizinhos // 8
                    
            print("Filtro de suavização aplicado com sucesso em todos os pixels internos!")
            
    elif opcao == 3:
        # Passo 5: Visualização lado a lado formatada no console
        if not cadastrado:
            print("Erro: Cadastre a imagem primeiro (Opção 1).")
        else:
            print("\n--- EXIBIÇÃO DE IMAGENS LADO A LADO ---")
            print("        Imagem Original                    Imagem Filtrada")
            print("-------------------------------    -------------------------------")
            for i in range(5):
                # Linha formatada da imagem original
                linha_orig = ""
                for j in range(5):
                    linha_orig = linha_orig + f"{imagem[i][j]:03d} "
                    
                # Linha formatada da imagem filtrada
                linha_filt = ""
                for j in range(5):
                    linha_filt = linha_filt + f"{filtrada[i][j]:03d} "
                    
                print(f"  {linha_orig}    |    {linha_filt}")
            print("-------------------------------    -------------------------------")
    else:
        print("Erro: Opção inválida.")
