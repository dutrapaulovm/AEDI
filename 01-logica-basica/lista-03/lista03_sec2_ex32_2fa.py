# Exercício 32: Autenticação de dois fatores
# Objetivo: Acesso parcial.

# Passo 1
senha = input("Senha digitada: ")
codigo = input("Código Token: ")

# Passo 2: Hierarquia de acesso
if senha == "pass" and codigo == "999":
    print("Acesso Total")
elif senha == "pass" and codigo != "999":
    print("Acesso Parcial - Apenas Leitura")
else:
    print("Acesso Negado")
