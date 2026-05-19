# Exercício 2: Boletim Geral de Notas (Matriz 3x3)
# Objetivo: Armazenar notas de 3 alunos em 3 avaliações em uma matriz, apresentando boletim geral e contador de recuperação.

# Passo 1: Inicialização da matriz notas 3x3 com zeros e status de lançamento
notas = [
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0]
]
lancado = False
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- SISTEMA ACADÊMICO (MATRIZ 3x3) ---")
    print("1. Lançar Notas")
    print("2. Boletim Geral")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema acadêmico encerrado.")
        
    elif opcao == 1:
        # Passo 3: Preenchimento da matriz com laços aninhados (for dentro de for) e validação [0, 10]
        print("\n--- Lançamento de Notas ---")
        for i in range(3):
            print(f"Aluno {i+1}:")
            for j in range(3):
                valido = False
                while not valido:
                    nota_input = input(f"  Digite a nota da Avaliação {j+1}: ")
                    nota_input = float(nota_input)
                    if 0.0 <= nota_input <= 10.0:
                        notas[i][j] = nota_input
                        valido = True
                    else:
                        print("  Erro: A nota deve estar entre 0.0 e 10.0. Digite novamente.")
        lancado = True
        print("Todas as notas foram lançadas com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Exibição do boletim e contagem de alunos em recuperação
        if not lancado:
            print("Erro: Lance as notas primeiro (Opção 1).")
        else:
            print("\n--- BOLETIM GERAL ---")
            total_recuperacao = 0
            
            for i in range(3):
                soma_aluno = 0.0
                for j in range(3):
                    soma_aluno = soma_aluno + notas[i][j]
                media_aluno = soma_aluno / 3.0
                
                # Classificação de status
                if media_aluno >= 7.0:
                    status = "APROVADO"
                elif 5.0 <= media_aluno < 7.0:
                    status = "RECUPERAÇÃO"
                    total_recuperacao = total_recuperacao + 1
                else:
                    status = "REPROVADO"
                    
                print(f"Aluno {i+1} - Avaliações: {notas[i]} | Média: {media_aluno:.2f} | Status: {status}")
                
            print(f"\nTotal de alunos em Recuperação: {total_recuperacao}")
    else:
        print("Erro: Opção inválida.")
