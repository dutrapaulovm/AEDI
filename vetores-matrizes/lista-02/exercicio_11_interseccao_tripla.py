# Exercício 11: Intersecção Tripla de Conjuntos Numéricos
# Objetivo: Definir tamanho N para os conjuntos A, B e C, preenchê-los individualmente via menu e computar os elementos comuns aos três conjuntos (A ∩ B ∩ C).

# Passo 1: Leitura do tamanho N comum com validação (> 0)
print("--- Definição do Tamanho dos Conjuntos ---")
n_valido = False
n = 0
while not n_valido:
    n = input("Digite o tamanho N dos conjuntos (vetores): ")
    n = int(n)
    if n > 0:
        n_valido = True
    else:
        print("Erro: O tamanho N deve ser maior que zero.")

# Passo 2: Inicialização dos vetores A, B e C de tamanho N, e status de preenchimento
vetor_a = [0] * n
vetor_b = [0] * n
vetor_c = [0] * n

preenchido_a = False
preenchido_b = False
preenchido_c = False

rodando = True

# Passo 3: Laço principal do menu interativo
while rodando:
    print("\n--- SISTEMA DE INTERSECÇÃO TRIPLA ---")
    print("1. Preencher Conjunto A")
    print("2. Preencher Conjunto B")
    print("3. Preencher Conjunto C")
    print("4. Calcular Intersecção (A ∩ B ∩ C)")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema de intersecção tripla encerrado.")
        
    elif opcao == 1:
        print(f"\n--- Preenchimento do Conjunto A (tamanho {n}) ---")
        for i in range(n):
            valido = False
            while not valido:
                val = input(f"  Digite o {i+1}º elemento (positivo): ")
                val = int(val)
                if val > 0:
                    vetor_a[i] = val
                    valido = True
                else:
                    print("    Erro: O elemento deve ser positivo e maior que zero.")
        preenchido_a = True
        print("Conjunto A gravado!")
        
    elif opcao == 2:
        print(f"\n--- Preenchimento do Conjunto B (tamanho {n}) ---")
        for i in range(n):
            valido = False
            while not valido:
                val = input(f"  Digite o {i+1}º elemento (positivo): ")
                val = int(val)
                if val > 0:
                    vetor_b[i] = val
                    valido = True
                else:
                    print("    Erro: O elemento deve ser positivo e maior que zero.")
        preenchido_b = True
        print("Conjunto B gravado!")
        
    elif opcao == 3:
        print(f"\n--- Preenchimento do Conjunto C (tamanho {n}) ---")
        for i in range(n):
            valido = False
            while not valido:
                val = input(f"  Digite o {i+1}º elemento (positivo): ")
                val = int(val)
                if val > 0:
                    vetor_c[i] = val
                    valido = True
                else:
                    print("    Erro: O elemento deve ser positivo e maior que zero.")
        preenchido_c = True
        print("Conjunto C gravado!")
        
    elif opcao == 4:
        # Passo 4: Operação de intersecção com laços aninhados (sem funções ou bibliotecas complexas)
        if not (preenchido_a and preenchido_b and preenchido_c):
            print("Erro: Todos os três conjuntos (A, B, C) devem ser preenchidos primeiro.")
        else:
            print("\n--- ANÁLISE DE INTERSECÇÃO ---")
            print(f"Conjunto A: {vetor_a}")
            print(f"Conjunto B: {vetor_b}")
            print(f"Conjunto C: {vetor_c}")
            
            # Vamos encontrar elementos de A que também estão em B e em C (sem duplicatas no resultado)
            interseccao = []
            
            for i in range(n):
                elem = vetor_a[i]
                
                # Verifica se elem existe no vetor B
                no_b = False
                for j in range(n):
                    if vetor_b[j] == elem:
                        no_b = True
                        break
                        
                # Verifica se elem existe no vetor C
                no_c = False
                for j in range(n):
                    if vetor_c[j] == elem:
                        no_c = True
                        break
                        
                # Se estiver nos três, adiciona à interseção (se já não estiver nela)
                if no_b and no_c:
                    ja_na_lista = False
                    for x in interseccao:
                        if x == elem:
                            ja_na_lista = True
                            break
                    if not ja_na_lista:
                        interseccao.append(elem)
                        
            print(f"\nResultado da Intersecção (A ∩ B ∩ C): {interseccao}")
    else:
        print("Erro: Opção inválida.")
