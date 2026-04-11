# Exercício 23: Períodos do dia
# Objetivo: Limites baseados no relógio

# Passo 1: Leitura
hora = input("Horário 0-23: ")
hora = int(hora)

# Passo 2: Checagem
if hora >= 0 and hora < 6:
    print("Madrugada")
elif hora >= 6 and hora < 12:
    print("Manhã")
elif hora >= 12 and hora < 18:
    print("Tarde")
elif hora >= 18 and hora <= 23:
    print("Noite")
else:
    print("Hora inválida")
