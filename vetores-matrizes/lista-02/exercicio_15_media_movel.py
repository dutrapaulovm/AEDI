# Exercício 15: Média Móvel de Sinais (Janela 3)
# Objetivo: Calcular a média móvel de janela 3 de um sinal de N amostras (N >= 3) em um vetor de tamanho N-2, acumulando manualmente em laço aninhado, e fornecendo menu de visualização.

# Passo 1: Leitura do número de amostras N com validação (N >= 3)
print("--- Filtro de Sinal - Média Móvel ---")
n_valido = False
n = 0
while not n_valido:
    n = input("Digite o número de amostras do sinal (N >= 3): ")
    n = int(n)
    if n >= 3:
        n_valido = True
    else:
        print("Erro: O número de amostras deve ser no mínimo 3.")

# Passo 2: Inicialização dos vetores
amostras = [0.0] * n
media_movel = [0.0] * (n - 2)
cadastrado = False
rodando = True

# Passo 3: Laço principal do menu interativo
while rodando:
    print("\n--- FILTRAGEM E ANÁLISE DE SINAIS (MÉDIA MÓVEL) ---")
    print("1. Cadastrar Amostras do Sinal")
    print("2. Calcular Média Móvel (Janela 3)")
    print("3. Visualizar Sinal e Gráfico de Linhas (Texto)")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Filtro de sinal encerrado.")
        
    elif opcao == 1:
        # Leitura das N amostras
        print(f"\n--- Cadastro de {n} Amostras do Sinal ---")
        for i in range(n):
            val = input(f"  Amostra {i+1}: ")
            val = float(val)
            amostras[i] = val
        cadastrado = True
        print("Sinal cadastrado com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Cálculo da média móvel de janela 3 com soma manual em laço aninhado
        if not cadastrado:
            print("Erro: Cadastre as amostras primeiro (Opção 1).")
        else:
            # Percorre o vetor de média móvel de índice 0 até N-3
            for i in range(n - 2):
                soma_janela = 0.0
                # Laço aninhado para acumular os 3 vizinhos (i, i+1, i+2)
                for j in range(3):
                    soma_janela = soma_janela + amostras[i + j]
                media_movel[i] = soma_janela / 3.0
                
            print("\nMédia móvel de janela 3 calculada:")
            print(f"  Amostras     : {amostras}")
            print(f"  Média Móvel  : {media_movel}")
            
    elif opcao == 3:
        # Passo 5: Visualizar dados e exibir gráfico em texto usando repetição
        if not cadastrado:
            print("Erro: Cadastre as amostras primeiro (Opção 1).")
        else:
            print("\n--- EXIBIÇÃO DE SINAIS E GRÁFICO TEXTUAL ---")
            print("Amostras originais:")
            for i in range(n):
                valor_int = int(abs(amostras[i]))
                barras = "*" * valor_int
                print(f"  [{i:2d}]: {amostras[i]:5.1f} | {barras}")
                
            print("\nMédia Móvel (Sinal Filtrado):")
            for i in range(n - 2):
                valor_int = int(abs(media_movel[i]))
                barras = "#" * valor_int
                print(f"  [{i:2d}]: {media_movel[i]:5.1f} | {barras}")
    else:
        print("Erro: Opção inválida.")
