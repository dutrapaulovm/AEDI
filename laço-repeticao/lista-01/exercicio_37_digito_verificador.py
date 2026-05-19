# Exercício 37: Cálculo de Dígito Verificador (Módulo 11)
# (Seção 3, Exercício 2 da Lista)
# Objetivo: Calcular o dígito de controle/verificador para uma sequência de 4 dígitos usando pesos decrescentes de 5 a 2.

# Passo 1: Leitura da sequência de 4 dígitos como string
sequencia = input("Digite a sequência de 4 dígitos (ex: 1234): ")

# Passo 2: Extração dos dígitos individuais e conversão para inteiros
d1 = int(sequencia[0])
d2 = int(sequencia[1])
d3 = int(sequencia[2])
d4 = int(sequencia[3])

# Passo 3: Cálculo da soma ponderada (pesos decrescentes de 5 a 2)
s = (d1 * 5) + (d2 * 4) + (d3 * 3) + (d4 * 2)

# Passo 4: Cálculo do dígito verificador usando a fórmula de Módulo 11
# Dígito = (S * 10) % 11
resultado = (s * 10) % 11

# Se o resultado for 10, o dígito verificador é definido como 0
if resultado == 10:
    digito = 0
else:
    digito = resultado

# Passo 5: Exibição do dígito verificador e do código completo
print(f"Soma ponderada (S): {s}")
print(f"Dígito Verificador Calculado: {digito}")
print(f"Código Completo: {sequencia}-{digito}")
