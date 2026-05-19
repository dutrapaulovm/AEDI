# Exercício 11: Auditoria de Atrasos de Funcionários (Vetor de 5 Posições)
# Objetivo: Monitorar minutos de atraso de 5 funcionários, aplicar regras de descontos de salário hora e advertências, e fazer análises corporativas comparativas.

# Passo 1: Inicialização das variáveis dos 5 funcionários
nomes = [""] * 5
atrasos = [0] * 5
cadastrado = False
salario_hora = 20.0
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- SISTEMA DE AUDITORIA DE ATRASOS (RH) ---")
    print("1. Registrar Nomes e Atrasos")
    print("2. Relatório Crítico de Descontos e Alertas")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema de auditoria de atrasos encerrado.")
        
    elif opcao == 1:
        # Passo 3: Leitura com validação de minutos (não negativos)
        print("\n--- Registro de Atrasos ---")
        sal_valido = False
        while not sal_valido:
            salario_hora = input("Digite o salário-hora base médio da empresa (R$): ")
            salario_hora = float(salario_hora)
            if salario_hora > 0.0:
                sal_valido = True
            else:
                print("Erro: O salário-hora deve ser maior que zero.")
                
        for i in range(5):
            nome = input(f"Digite o nome do funcionário {i+1}: ")
            nomes[i] = nome
            
            valido = False
            while not valido:
                minutos = input(f"  Digite os minutos de atraso de {nome}: ")
                minutos = int(minutos)
                if minutos >= 0:
                    atrasos[i] = minutos
                    valido = True
                else:
                    print("  Erro: Os minutos de atraso não podem ser negativos. Digite novamente.")
        cadastrado = True
        print("Registros salvos com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Geração do relatório com descontos, advertências e comparação por laços aninhados
        if not cadastrado:
            print("Erro: Faça os registros primeiro (Opção 1).")
        else:
            print("\n--- RELATÓRIO DE AUDITORIA E DESCONTOS ---")
            total_descontos = 0.0
            
            # Soma total de atrasos para cálculo da média dos outros
            soma_total_atrasos = 0.0
            for i in range(5):
                soma_total_atrasos = soma_total_atrasos + atrasos[i]
                
            for i in range(5):
                nome = nomes[i]
                atraso = atrasos[i]
                desconto = 0.0
                alerta = "Sem Advertência"
                
                # Regras de desconto e advertência
                if atraso > 15:
                    # Desconto = (Atraso / 60) * (Salário Hora / 2)
                    desconto = (atraso / 60.0) * (salario_hora / 2.0)
                    total_descontos = total_descontos + desconto
                    
                if atraso > 30:
                    alerta = "ALERTA DE ADVERTÊNCIA!"
                    
                # Comparação com a média dos outros funcionários (laço aninhado)
                soma_outros = 0.0
                for j in range(5):
                    if j != i:
                        soma_outros = soma_outros + atrasos[j]
                media_outros = soma_outros / 4.0
                
                # Exibição do status individual
                print(f"Funcionário: {nome} | Atraso: {atraso} min | Desconto: R$ {desconto:.2f} | Status: {alerta}")
                print(f"  -> Média de atraso dos outros funcionários: {media_outros:.1f} min")
                if atraso > media_outros:
                    print("     [COMPORTAMENTO] Atraso individual acima da média do grupo.")
                else:
                    print("     [COMPORTAMENTO] Atraso individual sob controle em relação ao grupo.")
                    
            print(f"\nTotal acumulado de descontos aplicados: R$ {total_descontos:.2f}")
    else:
        print("Erro: Opção inválida.")
