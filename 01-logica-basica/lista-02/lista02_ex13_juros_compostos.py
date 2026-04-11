# Exercício 13: Juros Compostos
# Objetivo: Montante final.

P = input("Capital inicial: ")
P = float(P)
r = input("Taxa de juros anual (decimal): ")
r = float(r)
n = input("Vezes que os juros são compostos no ano: ")
n = float(n)
t = input("Tempo em anos: ")
t = float(t)

M = P * (1 + (r / n))**(n * t)

print(f"Montante final: R$ {M:.2f}")
