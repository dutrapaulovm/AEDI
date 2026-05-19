# Exercício 5: Ritmo de Atleta de Alto Rendimento (Vetor de 5 Posições)
# Objetivo: Armazenar tempos de 5 voltas de um atleta, descartando leituras errôneas (< 10s), identificando a volta mais rápida e calculando a variância entre as voltas.

# Passo 1: Inicialização das variáveis
tempos = [0.0] * 5
cadastrado = False
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- ANALISADOR DE RITMO DE ATLETA ---")
    print("1. Cadastrar Tempos das 5 Voltas")
    print("2. Análise de Ritmo (Mais Rápida e Variância)")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Analisador de ritmo encerrado.")
        
    elif opcao == 1:
        # Passo 3: Leitura com validação de erro de sensor (tempo deve ser >= 10s)
        print("\n--- Lançamento de Tempos das Voltas ---")
        for i in range(5):
            valido = False
            while not valido:
                tempo = input(f"Digite o tempo da Volta {i+1} (em segundos): ")
                tempo = float(tempo)
                if tempo >= 10.0:
                    tempos[i] = tempo
                    valido = True
                else:
                    print("  Erro de sensor: Tempos menores que 10 segundos são impossíveis. Digite novamente.")
        cadastrado = True
        print("Todos os tempos foram cadastrados com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Cálculo da volta mais rápida e da variância estatística simples
        if not cadastrado:
            print("Erro: Cadastre os tempos primeiro (Opção 1).")
        else:
            print("\n--- ANÁLISE DE RITMO ---")
            
            # Encontra a volta mais rápida (menor tempo)
            volta_mais_rapida = tempos[0]
            indice_mais_rapida = 0
            soma_tempos = 0.0
            
            for i in range(5):
                soma_tempos = soma_tempos + tempos[i]
                if tempos[i] < volta_mais_rapida:
                    volta_mais_rapida = tempos[i]
                    indice_mais_rapida = i
            
            media_tempos = soma_tempos / 5.0
            
            # Passo 5: Cálculo da variância simples das voltas
            soma_diferencas_quad = 0.0
            for i in range(5):
                diferenca = tempos[i] - media_tempos
                soma_diferencas_quad = soma_diferencas_quad + (diferenca ** 2)
            variancia = soma_diferencas_quad / 5.0
            
            print(f"Volta mais rápida: Volta {indice_mais_rapida+1} com {volta_mais_rapida:.2f} segundos.")
            print(f"Média de ritmo por volta: {media_tempos:.2f} segundos.")
            print(f"Variância simples de ritmo: {variancia:.4f} (s²)")
    else:
        print("Erro: Opção inválida.")
