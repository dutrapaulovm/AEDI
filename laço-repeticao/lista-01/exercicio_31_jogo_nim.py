# Exercício 31: O Jogo de Nim (O Último Perde)
# (Seção 2, Exercício 25 da Lista)
# Objetivo: Implementar um jogo interativo de Nim com 20 pedras, onde dois jogadores se alternam e quem retirar a última pedra perde.

# Passo 1: Inicialização do estoque de pedras e do jogador atual
pedras = 20
jogador_atual = 1

# Passo 2: Laço principal do jogo (enquanto houver pedras)
while pedras > 0:
    print(f"\nRestam {pedras} pedras.")
    
    # Passo 3: Laço de validação para a jogada do jogador da vez
    jogada_valida = False
    retirar = 0
    while not jogada_valida:
        escolha = input(f"Jogador {jogador_atual}, retire 1, 2 ou 3 pedras: ")
        retirar = int(escolha)
        
        # Verifica se o valor é válido (1, 2 ou 3) e se não é maior que o estoque atual de pedras
        if 1 <= retirar <= 3:
            if retirar <= pedras:
                jogada_valida = True
            else:
                print(f"Erro: Você não pode retirar {retirar} pedras porque só restam {pedras}.")
        else:
            print("Erro: A jogada deve ser 1, 2 ou 3 pedras.")
            
    # Passo 4: Atualiza o saldo de pedras
    pedras = pedras - retirar
    
    # Passo 5: Verifica se o jogo acabou
    if pedras == 0:
        print(f"\nFIM DE JOGO! Jogador {jogador_atual} retirou a última pedra e PERDEU!")
    else:
        # Alterna o jogador atual para a próxima rodada
        if jogador_atual == 1:
            jogador_atual = 2
        else:
            jogador_atual = 1
