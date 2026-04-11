# Exercício 27: 3 Tentativas de Login
# Objetivo: Redundância baseada em IFs aninhados caso não usemos laços.

# Passo 1: 1a Tentativa
u = input("T1 - Usuário: ")
s = input("T1 - Senha: ")

if u == "root" and s == "123":
    print("Acesso")
else:
    print("Erro T1. Faltam 2 tentativas")
    
    # Passo 2: 2a Tentativa
    u2 = input("T2 - Usuário: ")
    s2 = input("T2 - Senha: ")
    if u2 == "root" and s2 == "123":
        print("Acesso")
    else:
        print("Erro T2. Última tentativa.")
        
        # Passo 3: 3a Tentativa
        u3 = input("T3 - Usuário: ")
        s3 = input("T3 - Senha: ")
        if u3 == "root" and s3 == "123":
            print("Acesso")
        else:
            print("Erro Crítico. Conta bloqueada.")
