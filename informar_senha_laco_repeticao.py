senha_correta = "python123"
tentativas = 1
while tentativas <= 3:
    # Primeira tentativa
    senha = input("Digite a senha: ")
    if (senha == senha_correta):
        print("Acesso permitido")
    else:
        print("Acesso negado")

   
