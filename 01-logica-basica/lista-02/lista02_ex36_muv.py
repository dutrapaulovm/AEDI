# Exercício 36: Movimento MUV
# Objetivo: Posição final.

u = input("Velocidade inicial: ")
u = float(u)
a = input("Aceleração: ")
a = float(a)
t = input("Tempo: ")
t = float(t)

s = u * t + 0.5 * a * (t**2)

print(f"Posição final: {s:.2f}")
