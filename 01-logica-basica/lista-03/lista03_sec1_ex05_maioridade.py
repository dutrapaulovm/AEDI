# Exercício 5: Menor ou Maior de Idade
# Objetivo: Classificar faixa etária por maioridade

# Passo 1: Leitura e conversão da idade
idade = input("Digite sua idade: ")
idade = int(idade)

# Passo 2: Condição de maioridade (+18)
if idade >= 18:
    # Passo 3a: Atende a condição
    print("Maior de idade")
else:
    # Passo 3b: Não atende
    print("Menor de idade")
