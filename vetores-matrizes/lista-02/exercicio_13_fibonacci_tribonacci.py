# Exercício 13: Comparativo de Fibonacci vs Tribonacci
# Objetivo: Preencher dois vetores de tamanho N (entre 3 e 25) com as sequências de Fibonacci e Tribonacci, e identificar os elementos em comum usando laço aninhado.

# Passo 1: Leitura de N com validação [3, 25]
print("--- Configuração de Séries Numéricas ---")
n_valido = False
n = 0
while not n_valido:
    n = input("Digite o tamanho N dos vetores (de 3 a 25): ")
    n = int(n)
    if 3 <= n <= 25:
        n_valido = True
    else:
        print("Erro: O tamanho N deve estar contido no intervalo [3, 25].")

# Passo 2: Inicialização dos vetores de tamanho N e status de controle
fibonacci = [0] * n
tribonacci = [0] * n
gerado = False
rodando = True

# Passo 3: Laço principal do menu interativo
while rodando:
    print("\n--- COMPARADOR DE FIBONACCI VS TRIBONACCI ---")
    print("1. Gerar Sequências")
    print("2. Buscar Termos Comuns")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema de análise de sequências encerrado.")
        
    elif opcao == 1:
        # Geração da sequência de Fibonacci
        # F0 = 0, F1 = 1, Fn = Fn-1 + Fn-2
        fibonacci[0] = 0
        fibonacci[1] = 1
        for i in range(2, n):
            fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]
            
        # Geração da sequência de Tribonacci
        # T0 = 0, T1 = 0, T2 = 1, Tn = Tn-1 + Tn-2 + Tn-3
        if n >= 1:
            tribonacci[0] = 0
        if n >= 2:
            tribonacci[1] = 0
        if n >= 3:
            tribonacci[2] = 1
        for i in range(3, n):
            tribonacci[i] = tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3]
            
        print("\nSequências geradas com sucesso:")
        print(f"  Fibonacci : {fibonacci}")
        print(f"  Tribonacci: {tribonacci}")
        gerado = True
        
    elif opcao == 2:
        # Passo 4: Busca de termos comuns usando laços aninhados
        if not gerado:
            print("Erro: Gere as sequências primeiro (Opção 1).")
        else:
            print("\n--- ANÁLISE DE TERMOS COMUNS ---")
            comuns = []
            
            for i in range(n):
                termo_fib = fibonacci[i]
                
                # Procura termo_fib no vetor Tribonacci
                encontrado = False
                for j in range(n):
                    if tribonacci[j] == termo_fib:
                        encontrado = True
                        break
                        
                # Adiciona se encontrado e se não for repetido na lista de comuns
                if encontrado:
                    ja_existe = False
                    for x in comuns:
                        if x == termo_fib:
                            ja_existe = True
                            break
                    if not ja_existe:
                        comuns.append(termo_fib)
                        
            print(f"Elementos que pertencem a ambas as sequências: {comuns}")
    else:
        print("Erro: Opção inválida.")
