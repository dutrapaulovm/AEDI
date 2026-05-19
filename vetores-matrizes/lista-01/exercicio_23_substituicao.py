# Exercício 23: Criptografia por Cifra de Substituição Cíclica (Vetor de 5 Posições)
# Objetivo: Definir uma chave numérica de deslocamento de 5 posições (valores de 1 a 9) e cifrar uma sequência de dígitos usando a lógica de Vigenère modular.

# Passo 1: Inicialização do vetor de chave e status de configuração
chave = [0] * 5
configurado = False
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- SISTEMA CRIPTOGRÁFICO DE SUBSTUIÇÃO MODULAR ---")
    print("1. Definir Chave de Deslocamento (5 Elementos)")
    print("2. Cifrar Mensagem Numérica")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema criptográfico encerrado.")
        
    elif opcao == 1:
        # Passo 3: Definir chave de 5 dígitos (validação de 1 a 9)
        print("\n--- Definição da Chave Criptográfica ---")
        for i in range(5):
            valido = False
            while not valido:
                num = input(f"  Digite o valor de deslocamento da posição {i+1} (1 a 9): ")
                num = int(num)
                if 1 <= num <= 9:
                    chave[i] = num
                    valido = True
                else:
                    print("    Erro: Cada número da chave deve estar entre 1 e 9.")
        configurado = True
        print(f"Chave criptográfica definida com sucesso: {chave}")
        
    elif opcao == 2:
        # Passo 4: Cifrar dados aplicando a chave de forma cíclica (uso de operador %)
        if not configurado:
            print("Erro: Defina a chave criptográfica primeiro (Opção 1).")
        else:
            print("\n--- Cifragem de Dados ---")
            mensagem = input("Digite a sequência de dígitos numéricos a cifrar (ex: 20265): ")
            
            # Validação elementar para garantir que o usuário digitou apenas números
            eh_numerica = True
            for char in mensagem:
                if not ("0" <= char <= "9"):
                    eh_numerica = False
                    
            if not eh_numerica:
                print("Erro: A mensagem deve conter exclusivamente dígitos de 0 a 9.")
            else:
                mensagem_cifrada = ""
                
                # Passo 5: Laço cíclico sobre a chave usando o operador módulo %
                for i in range(len(mensagem)):
                    digito = int(mensagem[i])
                    
                    # A chave cicla a cada 5 caracteres: chave[i % 5]
                    deslocamento = chave[i % 5]
                    
                    # Novo dígito cifrado mantido em módulo 10 (0 a 9)
                    novo_digito = (digito + deslocamento) % 10
                    mensagem_cifrada = mensagem_cifrada + str(novo_digito)
                    
                print(f"\nMensagem Original: {mensagem}")
                print(f"Chave Aplicada:    {chave}")
                print(f"Mensagem Cifrada:  {mensagem_cifrada}")
    else:
        print("Erro: Opção inválida.")
