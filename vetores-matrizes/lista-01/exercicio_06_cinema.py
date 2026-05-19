# Exercício 6: Reserva de Sala VIP de Cinema (Matriz 3x4)
# Objetivo: Gerenciar a ocupação de assentos em uma sala com 3 fileiras e 4 poltronas (0: Livre, 1: Ocupado), exibindo um mapa gráfico textual e taxa de ocupação.

# Passo 1: Inicialização da matriz com zeros usando laços aninhados
mapa_assentos = []
for i in range(3):
    fileira = [0] * 4
    mapa_assentos.append(fileira)

rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- SISTEMA DE RESERVAS SINAL VIP ---")
    print("1. Visualizar Mapa de Assentos")
    print("2. Reservar Assento")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema de reservas encerrado.")
        
    elif opcao == 1:
        # Passo 3: Exibição gráfica do mapa com 'L' para livre e 'X' para ocupado
        print("\n--- MAPA DE ASSENTOS ---")
        print("        Poltrona:  1   2   3   4")
        for i in range(3):
            linha_mapa = f"Fileira {i+1} :     "
            for j in range(4):
                if mapa_assentos[i][j] == 0:
                    linha_mapa = linha_mapa + " L  "
                else:
                    linha_mapa = linha_mapa + " X  "
            print(linha_mapa)
        print("------------------------")
        
    elif opcao == 2:
        # Passo 4: Reserva de assento com validação de coordenadas e de duplicidade
        print("\n--- Realizar Reserva ---")
        
        # Validação da fileira (1 a 3)
        fileira_valida = False
        while not fileira_valida:
            f_ind = input("Digite o número da fileira (1 a 3): ")
            f_ind = int(f_ind)
            if 1 <= f_ind <= 3:
                f_ind = f_ind - 1  # Ajuste para índice 0-based
                fileira_valida = True
            else:
                print("Erro: Fileira inválida. Escolha 1, 2 ou 3.")
                
        # Validação da poltrona (1 a 4)
        poltrona_valida = False
        while not poltrona_valida:
            p_ind = input("Digite o número da poltrona (1 a 4): ")
            p_ind = int(p_ind)
            if 1 <= p_ind <= 4:
                p_ind = p_ind - 1  # Ajuste para índice 0-based
                poltrona_valida = True
            else:
                print("Erro: Poltrona inválida. Escolha de 1 a 4.")
                
        # Passo 5: Verificação se o assento já está ocupado
        if mapa_assentos[f_ind][p_ind] == 1:
            print("Erro: Assento Ocupado! Por favor, faça outra escolha.")
        else:
            mapa_assentos[f_ind][p_ind] = 1
            print("Sucesso: Assento reservado com êxito!")
            
            # Cálculo da porcentagem de ocupação
            ocupados = 0
            for i in range(3):
                for j in range(4):
                    if mapa_assentos[i][j] == 1:
                        ocupados = ocupados + 1
            porcentagem = (ocupados / 12.0) * 100.0
            print(f"Ocupação da sala atualizada: {porcentagem:.1f}%")
    else:
        print("Erro: Opção inválida.")
