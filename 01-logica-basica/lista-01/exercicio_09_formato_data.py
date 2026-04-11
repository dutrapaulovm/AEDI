# Exercício 9: Formato de data
# Objetivo: Extrair o dia, o mês e o ano de um número inteiro no formato ddmmaa.

# Passo 1: Leitura da data inteira
data_inteira = input("Digite a data no formato ddmmaa (ex: 230389): ")
data_inteira = int(data_inteira)

# Passo 2: Separação matemática
# O resto da divisão por 100 extrai as duas últimas casas (ano)
ano = data_inteira % 100

# Dividimos por 100 ignorando as casas decimais para tirar o ano, restando ddmm
ddmm = data_inteira // 100

# Agora fazemos a mesma lógica com ddmm:
# O resto da divisão por 100 de ddmm extrai as duas últimas casas (mês)
mes = ddmm % 100

# A divisão inteira de ddmm por 100 nos dá os dois primeiros dígitos (dia)
dia = ddmm // 100

# Passo 3: Exibição formatada das partes da data
print(f"DIA: {dia:02d}")
print(f"MÊS: {mes:02d}")
print(f"ANO: {ano:02d}")
