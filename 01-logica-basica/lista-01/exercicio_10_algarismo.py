# Exercício 10: Descobrir algarismo
# Objetivo: Extrair o algarismo da dezena de um número inteiro de 3 dígitos.

# Passo 1: Entrada do número
numero = input("Digite um número inteiro de 3 casas (ex: 352): ")
numero = int(numero)

# Passo 2: Lógica de separação
# Usando a divisão inteira por 10, removemos o algarismo da unidade.
sem_unidade = numero // 10

# Agora o último dígito é a nossa dezena original. Usamos o resto da divisão por 10.
dezena = sem_unidade % 10

# Passo 3: Saída
print(f"O algarismo da casa das dezenas é: {dezena}")
