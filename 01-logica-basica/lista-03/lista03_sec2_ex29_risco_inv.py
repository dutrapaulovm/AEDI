# Exercício 29: Perfil de Risco
# Objetivo: Condição baseada em strings

# Passo 1: Leitura das configurações
retorno = input("Retorno esperado (baixo/alto): ")
retorno = retorno.lower()
volatilidade = input("Volatilidade (baixa/alta): ")
volatilidade = volatilidade.lower()

# Passo 2: Definição de riscos
if retorno == "baixo" and volatilidade == "baixa":
    print("Baixo Risco")
elif retorno == "alto" and volatilidade == "alta":
    print("Alto Risco")
else:
    print("Médio Risco")
