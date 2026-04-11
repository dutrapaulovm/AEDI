# Exercício 15: Validação de Calendário (Data)
# Objetivo: Logica aninhada complexa para limites numéricos

# Passo 1: Setup das 3 variáveis de data
d = input("Dia: ")
d = int(d)
m = input("Mês (1 a 12): ")
m = int(m)
ano = input("Ano: ")
ano = int(ano)

# Passo 2: Variável flag de contexto de data correta
data_valida = False

# Passo 3: Teste temporal
if (m >= 1 and m <= 12) and (d >= 1 and d <= 31):
    # Meses de 31 dias
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        data_valida = True
    # Meses de 30 dias
    elif (m == 4 or m == 6 or m == 9 or m == 11) and (d <= 30):        
        data_valida = True
    # Lógica restrita para Bissexto
    elif m == 2:
        bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
        if bissexto:
            if d <= 29:
                data_valida = True
        else:
            if d <= 28:
                data_valida = True
                
# Passo 4: Conclusões e Prints do Output
if data_valida:
    print("Data válida")
else:
    print("Data inválida")