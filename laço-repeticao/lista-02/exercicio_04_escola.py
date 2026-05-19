# Exercício 4: Sistema de Avaliação Escolar Multiturmas
# Objetivo: Avaliar o desempenho acadêmico de alunos distribuídos em múltiplas turmas, calculando médias e status individuais e gerais.

# Passo 1: Leitura e validação da quantidade de turmas
turmas_valido = False
while not turmas_valido:
    qtd_turmas = input("Digite a quantidade de turmas (mínimo 1): ")
    qtd_turmas = int(qtd_turmas)
    if qtd_turmas >= 1:
        turmas_valido = True
    else:
        print("Erro: A quantidade de turmas deve ser pelo menos 1.")

# Passo 2: Laço principal para processar cada turma
for t in range(1, qtd_turmas + 1):
    print(f"\n================ TURMA {t} ================")
    
    # Passo 3: Leitura e validação da quantidade de alunos da turma atual
    alunos_valido = False
    while not alunos_valido:
        qtd_alunos = input(f"Digite a quantidade de alunos para a Turma {t} (mínimo 1): ")
        qtd_alunos = int(qtd_alunos)
        if qtd_alunos >= 1:
            alunos_valido = True
        else:
            print("Erro: A quantidade de alunos deve ser pelo menos 1.")
            
    # Passo 4: Inicialização das variáveis de estatísticas da turma
    soma_medias_turma = 0.0
    total_aprovados = 0
    total_recuperacao = 0
    total_reprovados = 0
    
    # Passo 5: Laço para processar cada aluno da turma
    for a in range(1, qtd_alunos + 1):
        print(f"\n  Processando Aluno {a}:")
        
        # Leitura e validação da Nota 1
        n1_valida = False
        while not n1_valida:
            n1 = input("    Digite a nota da Prova 1 (0 a 10): ")
            n1 = float(n1)
            if 0.0 <= n1 <= 10.0:
                n1_valida = True
            else:
                print("    Erro: A nota deve estar no intervalo [0.0, 10.0].")
                
        # Leitura e validação da Nota 2
        n2_valida = False
        while not n2_valida:
            n2 = input("    Digite a nota da Prova 2 (0 a 10): ")
            n2 = float(n2)
            if 0.0 <= n2 <= 10.0:
                n2_valida = True
            else:
                print("    Erro: A nota deve estar no intervalo [0.0, 10.0].")
                
        # Leitura e validação da Nota 3
        n3_valida = False
        while not n3_valida:
            n3 = input("    Digite a nota da Prova 3 (0 a 10): ")
            n3 = float(n3)
            if 0.0 <= n3 <= 10.0:
                n3_valida = True
            else:
                print("    Erro: A nota deve estar no intervalo [0.0, 10.0].")
                
        # Passo 6: Cálculo da média aritmética do aluno
        media_aluno = (n1 + n2 + n3) / 3.0
        soma_medias_turma = soma_medias_turma + media_aluno
        
        # Classificação do status do aluno
        if media_aluno >= 7.0:
            status = "Aprovado"
            total_aprovados = total_aprovados + 1
        elif 5.0 <= media_aluno < 7.0:
            status = "Recuperação"
            total_recuperacao = total_recuperacao + 1
        else:
            status = "Reprovado"
            total_reprovados = total_reprovados + 1
            
        print(f"    Média do Aluno {a}: {media_aluno:.2f} | Status: {status}")
        
    # Passo 7: Cálculo das estatísticas gerais da turma
    media_geral_turma = soma_medias_turma / qtd_alunos
    porcentagem_aprovacao = (total_aprovados / qtd_alunos) * 100.0
    
    # Passo 8: Exibição do relatório final da turma
    print(f"\n--- Relatório Final da Turma {t} ---")
    print(f"Média Geral da Turma: {media_geral_turma:.2f}")
    print(f"Quantidade de Aprovados: {total_aprovados} ({porcentagem_aprovacao:.1f}%)")
    print(f"Quantidade em Recuperação: {total_recuperacao}")
    print(f"Quantidade de Reprovados: {total_reprovados}")
