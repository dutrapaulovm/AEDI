# Exercício 42: WACC
# Objetivo: Custo Médio Ponderado.

E = input("Patrimônio líquido (E): ")
E = float(E)
D = input("Dívida (D): ")
D = float(D)
re = input("Custo do patrimônio (re - decimal): ")
re = float(re)
rd = input("Custo da dívida (rd - decimal): ")
rd = float(rd)
tc = input("Taxa de imposto corporativo (tc - decimal): ")
tc = float(tc)

V = E + D
WACC = (E/V) * re + (D/V) * rd * (1 - tc)

print(f"WACC: {WACC:.4f}")
