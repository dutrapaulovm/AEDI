# Exercício 1: Faturamento Diário Semanal
# Objetivo: Armazenar o faturamento de 7 dias da semana em um vetor e oferecer análise de média e pesquisa de faturamento exato.

# Passo 1: Inicialização do vetor de faturamento com zeros e status de cadastro
faturamento = [0.0] * 7
cadastrado = False
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- MENU ANALISADOR DE FATURAMENTO ---")
    print("1. Cadastrar Faturamentos")
    print("2. Analisar Faturamentos (Média e Dias Acima)")
    print("3. Pesquisar Faturamento")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema de faturamento encerrado.")
        
    elif opcao == 1:
        # Passo 3: Cadastro dos 7 dias com validação (valores não negativos)
        print("\n--- Cadastro de Faturamento ---")
        for i in range(7):
            valido = False
            while not valido:
                valor = input(f"Digite o faturamento do Dia {i+1}: ")
                valor = float(valor)
                if valor >= 0.0:
                    faturamento[i] = valor
                    valido = True
                else:
                    print("Erro: O faturamento não pode ser negativo. Digite novamente.")
        cadastrado = True
        print("Faturamento semanal cadastrado com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Análise da média e dias acima da média
        if not cadastrado:
            print("Erro: Cadastre os faturamentos primeiro (Opção 1).")
        else:
            soma = 0.0
            for i in range(7):
                soma = soma + faturamento[i]
            media = soma / 7.0
            
            # Conta dias acima da média
            dias_acima = 0
            for i in range(7):
                if faturamento[i] > media:
                    dias_acima = dias_acima + 1
                    
            print(f"\nMédia semanal de faturamento: R$ {media:.2f}")
            print(f"Quantidade de dias com faturamento acima da média: {dias_acima}")
            
    elif opcao == 3:
        # Passo 5: Pesquisa de um faturamento específico
        if not cadastrado:
            print("Erro: Cadastre os faturamentos primeiro (Opção 1).")
        else:
            meta = input("Digite o valor de faturamento que deseja pesquisar: ")
            meta = float(meta)
            
            encontrado = False
            for i in range(7):
                if faturamento[i] == meta:
                    print(f"Sucesso: O faturamento de R$ {meta:.2f} foi atingido no Dia {i+1}!")
                    encontrado = True
                    
            if not encontrado:
                print(f"Informação: O faturamento exato de R$ {meta:.2f} não foi registrado em nenhum dia.")
    else:
        print("Erro: Opção inválida.")
