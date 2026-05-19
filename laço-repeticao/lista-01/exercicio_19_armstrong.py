# Exercício 19: Número de Armstrong
# Objetivo: Verificar se um número inteiro positivo é um número de Armstrong.

# Passo 1: Leitura do número
numero = input("Digite um número inteiro positivo: ")
# Mantemos a versão em texto para facilidade de iteração de dígitos
num_str = numero
numero = int(numero)

# Passo 2: Contagem do total de dígitos
total_digitos = len(num_str)

# Passo 3: Soma dos dígitos elevados à potência do total de dígitos
soma = 0
for caractere in num_str:
    digito = int(caractere)
    
    # Calcula a potência manualmente (digito^total_digitos)
    potencia = 1
    for _ in range(total_digitos):
        potencia = potencia * digito
        
    soma = soma + potencia

# Passo 4: Verificação e exibição do resultado
if soma == numero:
    print(f"O número {numero} é um número de Armstrong.")
else:
    print(f"O número {numero} NÃO é um número de Armstrong.")
