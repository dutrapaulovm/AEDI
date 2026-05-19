# Exercício 24: EAN-13 e Aumento de Preço
# Objetivo: Solicitar 5 códigos de barras EAN-13 e seus preços de venda, aplicando reajuste por categoria e exibindo a soma e média final dos produtos válidos.

# Passo 1: Inicialização das variáveis acumuladoras
soma_total = 0.0
total_validos = 0

# Passo 2: Laço de repetição para ler 5 produtos
for vez in range(1, 6):
    ean = input(f"Digite o código de barras do {vez}º produto: ")
    preco = input(f"Digite o preço de venda do {vez}º produto: ")
    preco = float(preco)
    
    # Passo 3: Extração dos 3 primeiros dígitos do código de barras (prefixo)
    prefixo = int(ean[:3])
    
    # Passo 4: Classificação da categoria e aplicação do aumento
    if 789 <= prefixo <= 799:
        categoria = "Bebidas"
        preco_reajustado = preco * 1.05
    elif 800 <= prefixo <= 899:
        categoria = "Alimentos"
        preco_reajustado = preco * 1.10
    elif 900 <= prefixo <= 999:
        categoria = "Limpeza"
        preco_reajustado = preco * 1.08
    else:
        categoria = "Inválido"
        preco_reajustado = 0.0
        
    print(f"Produto {vez}: Categoria={categoria} | Preço Reajustado=R$ {preco_reajustado:.2f}")
    
    # Passo 5: Acumulação dos dados se for um produto válido
    if categoria != "Inválido":
        soma_total = soma_total + preco_reajustado
        total_validos = total_validos + 1

# Passo 6: Exibição dos resultados finais
print("\n--- Relatório Final ---")
print(f"Soma total dos preços reajustados: R$ {soma_total:.2f}")

if total_validos > 0:
    media = soma_total / total_validos
    print(f"Média dos preços reajustados: R$ {media:.2f}")
else:
    print("Nenhum produto válido foi inserido para o cálculo da média.")
