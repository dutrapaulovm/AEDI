# Exercício 20: VPL (Valor Presente Líquido)
# Objetivo: Lógica simplificada ou usando loop para n fluxos de caixa.

n = input("Número de períodos: ")
n = int(n)
r = input("Taxa de desconto (decimal): ")
r = float(r)

vpl = 0
for t in range(n + 1):
    cf = input(f"Fluxo de caixa no período {t}: ")
    cf = float(cf)
    vpl += cf / ((1 + r)**t)

print(f"Valor Presente Líquido (VPL): R$ {vpl:.2f}")
