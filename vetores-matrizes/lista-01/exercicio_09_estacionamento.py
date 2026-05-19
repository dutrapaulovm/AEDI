# Exercício 9: Controle de Estacionamento (Vetor de 5 Vagas)
# Objetivo: Controlar permanência em minutos em 5 vagas, calculando o valor a pagar com frações de hora e acompanhando o faturamento total acumulado.

# Passo 1: Inicialização do vetor de vagas com zeros (0 = vazia) e faturamento acumulado
vagas_permanencia = [0] * 5
faturamento_total = 0.0
valor_hora = 0.0
configurado = False
rodando = True

# Passo 2: Laço principal do menu interativo
while rodando:
    print("\n--- SISTEMA DE GESTÃO DE ESTACIONAMENTO ---")
    print("1. Configurar Valor da Hora e Registrar Permanência")
    print("2. Registrar Saída de Veículo (Calcular Pagamento)")
    print("3. Relatório de Vagas e Faturamento Acumulado")
    print("0. Sair")
    
    opcao = input("Opção: ")
    opcao = int(opcao)
    
    if opcao == 0:
        rodando = False
        print("Sistema de estacionamento encerrado.")
        
    elif opcao == 1:
        # Passo 3: Configurar valor da hora (validação positivo) e registrar ocupação das vagas
        print("\n--- Configuração e Ocupação ---")
        val_valido = False
        while not val_valido:
            valor_hora = input("Digite o valor da hora de estacionamento (R$): ")
            valor_hora = float(valor_hora)
            if valor_hora > 0.0:
                val_valido = True
            else:
                print("Erro: O valor da hora deve ser positivo.")
                
        # Registro de permanência para as 5 vagas (0 se vazia)
        for i in range(5):
            valido = False
            while not valido:
                tempo = input(f"Digite o tempo de permanência da vaga {i+1} em minutos (0 se vazia): ")
                tempo = int(tempo)
                if tempo >= 0:
                    vagas_permanencia[i] = tempo
                    valido = True
                else:
                    print("Erro: O tempo de permanência não pode ser negativo.")
        configurado = True
        print("Estacionamento configurado com sucesso!")
        
    elif opcao == 2:
        # Passo 4: Registrar a saída e calcular o pagamento de uma vaga específica
        if not configurado:
            print("Erro: Configure o valor da hora e registre a ocupação primeiro (Opção 1).")
        else:
            print("\n--- Liberação de Vaga e Pagamento ---")
            vaga_valida = False
            while not vaga_valida:
                v_num = input("Digite o número da vaga a liberar (1 a 5): ")
                v_num = int(v_num)
                if 1 <= v_num <= 5:
                    v_idx = v_num - 1
                    vaga_valida = True
                else:
                    print("Erro: Vaga inválida.")
                    
            if vagas_permanencia[v_idx] == 0:
                print(f"Informação: A Vaga {v_num} já está vazia.")
            else:
                tempo_minutos = vagas_permanencia[v_idx]
                
                # Cálculo de frações de hora (fração exata)
                valor_pagar = (tempo_minutos / 60.0) * valor_hora
                faturamento_total = faturamento_total + valor_pagar
                
                print(f"\nVeículo da Vaga {v_num} liberado!")
                print(f"Tempo total de permanência: {tempo_minutos} minutos ({tempo_minutos/60.0:.2f} horas)")
                print(f"Valor a pagar: R$ {valor_pagar:.2f}")
                
                # Zera a vaga após a saída
                vagas_permanencia[v_idx] = 0
                
    elif opcao == 3:
        # Passo 5: Relatório geral, maior tempo e faturamento total
        if not configurado:
            print("Erro: Configure o valor da hora primeiro (Opção 1).")
        else:
            print("\n--- RELATÓRIO DO DIA ---")
            veiculo_mais_tempo = -1
            vaga_mais_tempo = -1
            
            for i in range(5):
                status_vaga = "Vazia" if vagas_permanencia[i] == 0 else f"Ocupada ({vagas_permanencia[i]} min)"
                print(f"Vaga {i+1}: {status_vaga}")
                
                if vagas_permanencia[i] > veiculo_mais_tempo:
                    veiculo_mais_tempo = vagas_permanencia[i]
                    vaga_mais_tempo = i + 1
                    
            if veiculo_mais_tempo > 0:
                print(f"\nVeículo que permaneceu mais tempo: Vaga {vaga_mais_tempo} ({veiculo_mais_tempo} minutos)")
            else:
                print("\nNenhum veículo estacionado no momento.")
                
            print(f"Faturamento Total Acumulado do Dia: R$ {faturamento_total:.2f}")
    else:
        print("Erro: Opção inválida.")
