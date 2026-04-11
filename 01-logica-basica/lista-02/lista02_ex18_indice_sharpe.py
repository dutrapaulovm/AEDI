# Exercício 18: Índice de Sharpe
# Objetivo: Desempenho de investimento.

retorno_medio = input("Retorno médio (decimal): ")
retorno_medio = float(retorno_medio)
retorno_livre = input("Retorno livre de risco (decimal): ")
retorno_livre = float(retorno_livre)
desvio = input("Desvio padrão dos retornos (decimal): ")
desvio = float(desvio)

sharpe = (retorno_medio - retorno_livre) / desvio

print(f"Índice de Sharpe: {sharpe:.4f}")
