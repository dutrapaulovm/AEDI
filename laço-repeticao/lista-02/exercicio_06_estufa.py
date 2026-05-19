# Exercício 6: Monitoramento de Estufa Inteligente via IoT
# Objetivo: Coletar e validar temperaturas de 4 sensores em 4 intervalos diários, exibindo as médias diárias e alertas de risco térmico.

# Passo 1: Leitura da data da coleta
data_coleta = input("Digite a data da coleta (DD/MM/AAAA): ")

# Passo 2: Inicialização da estrutura de dados e variáveis de relatório
print("\n--- Iniciando Leituras Diárias de Sensores (greenhouse IoT) ---")

# Laço para percorrer cada um dos 4 sensores
for sensor in range(1, 5):
    print(f"\nSensor {sensor}:")
    
    # Acumuladores específicos do sensor atual
    soma_temp_sensor = 0.0
    houve_congelamento = False
    
    # Laço para processar os 4 intervalos do dia: 0h, 6h, 12h, 18h
    for hora in [0, 6, 12, 18]:
        # Leitura e validação da temperatura
        # Deixamos a validação realista de -10 a 50 graus para permitir que o alerta de congelamento possa ser ativado se necessário,
        # ou se o usuário inserir valores dentro do limite operacional estrito.
        temp_valida = False
        while not temp_valida:
            leitura = input(f"  Digite a temperatura às {hora}h (em °C): ")
            leitura = float(leitura)
            # Validação: aceitamos de -10°C a 50°C para permitir testes do sistema
            if -10.0 <= leitura <= 50.0:
                temp_valida = True
            else:
                print("    Erro: Temperatura fora dos limites físicos plausíveis da estufa (-10°C a 50°C).")
                
        # Acumula e verifica limites de risco
        soma_temp_sensor = soma_temp_sensor + leitura
        
        # Alerta de Congelamento: se houver qualquer leitura abaixo de 10°C
        if leitura < 10.0:
            houve_congelamento = True
            
    # Passo 3: Cálculo da média diária do sensor
    media_diaria = soma_temp_sensor / 4.0
    
    # Passo 4: Verificação de alertas de risco térmico
    alerta = "Operação Normal"
    if media_diaria > 35.0:
        alerta = "ALERTA: Risco de Superaquecimento"
    elif houve_congelamento:
        alerta = "ALERTA: Risco de Congelamento"
        
    # Passo 5: Exibição do relatório individual do sensor
    print(f"Média Diária do Sensor {sensor}: {media_diaria:.2f} °C - Status: {alerta}")
