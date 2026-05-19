# Exercício 30: Tabela Verdade Porta AND (Matriz 8x4)
# Objetivo: Gerar automaticamente uma tabela verdade de 3 entradas (A, B, C) e saída AND (coluna 3) em uma matriz 8x4, permitindo buscas de combinações.

# Passo 1: Inicialização e preenchimento automático da matriz 8x4
# Geramos as 8 linhas de combinações binárias (2³ = 8) com a operação AND lógica
tabela_verdade = []
for i in range(8):
    # Lógica de preenchimento automático usando operadores aritméticos de divisão e resto
    bits_a = (i // 4) % 2
    bits_b = (i // 2) % 2
    bits_c = i % 2
    
    # Operação AND lógica (1 se todos ativos, senão 0)
    resultado_and = 1 if (bits_a == 1 and bits_b == 1 and bits_c == 1) else 0
    
    tabela_verdade.append([bits_a, bits_b, bits_c, resultado_and])

rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- SISTEMAS DIGITAIS - TABELA VERDADE AND 3 ENTRADAS ---")
    print("1. Visualizar Tabela Verdade Completa (Matriz 8x4)")
    print("2. Pesquisar Combinação Específica")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistemas digitais encerrado.")
        
    elif opcao == 1:
        # Passo 3: Mostrar a tabela de forma organizada
        print("\n--- TABELA VERDADE PORTA AND (8x4) ---")
        print(" Linha | Entrada A | Entrada B | Entrada C | Saída AND")
        print("-------|-----------|-----------|-----------|-----------")
        for i in range(8):
            a = tabela_verdade[i][0]
            b = tabela_verdade[i][1]
            c = tabela_verdade[i][2]
            res = tabela_verdade[i][3]
            print(f"  {i+1:3d}  |     {a}     |     {b}     |     {c}     |     {res}")
        print("-------------------------------------------------------")
        
    elif opcao == 2:
        # Passo 4: Pesquisar uma combinação com validações (apenas 0 ou 1)
        print("\n--- Pesquisa de Combinação ---")
        
        # Validação da entrada A
        a_valida = False
        while not a_valida:
            val_a = input("Digite o valor para Entrada A (0 ou 1): ")
            val_a = int(val_a)
            if val_a == 0 or val_a == 1:
                a_valida = True
            else:
                print("Erro: Apenas os bits 0 ou 1 são válidos.")
                
        # Validação da entrada B
        b_valida = False
        while not b_valida:
            val_b = input("Digite o valor para Entrada B (0 ou 1): ")
            val_b = int(val_b)
            if val_b == 0 or val_b == 1:
                b_valida = True
            else:
                print("Erro: Apenas os bits 0 ou 1 são válidos.")
                
        # Validação da entrada C
        c_valida = False
        while not c_valida:
            val_c = input("Digite o valor para Entrada C (0 ou 1): ")
            val_c = int(val_c)
            if val_c == 0 or val_c == 1:
                c_valida = True
            else:
                print("Erro: Apenas os bits 0 ou 1 são válidos.")
                
        # Passo 5: Buscar a correspondência na tabela
        encontrado = False
        for i in range(8):
            if (tabela_verdade[i][0] == val_a and 
                tabela_verdade[i][1] == val_b and 
                tabela_verdade[i][2] == val_c):
                
                res_busca = tabela_verdade[i][3]
                print(f"\nCombinação encontrada na linha {i+1} da matriz!")
                print(f"Resultado: AND({val_a}, {val_b}, {val_c}) = {res_busca}")
                encontrado = True
                break
                
        if not encontrado:
            print("Erro: Combinação não encontrada (incomum).")
    else:
        print("Erro: Opção inválida.")
