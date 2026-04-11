# Exercício 17: Sistema Admin Simulador
# Objetivo: Lógica encadeada para login perfeito

# Passo 1: Coletar os dois fatores
user = input("Usuário: ")
senha = input("Senha: ")

# Passo 2: Validar hierarquicamente
if user == "admin" and senha == "123":
    print("Acesso permitido")
elif user != "admin":
    print("Erro de usuário")
elif senha != "123":
    print("Erro de senha")
