# Script de Verificação Geral de Soluções
# Objetivo: Validar sintaxe de todos os 60 exercícios das listas 1 e 2, garantindo que não existam funções (def) nem guards (__main__) nos arquivos de código.

import os
import ast

def verificar_arquivos():
    diretorio_base = os.path.dirname(os.path.abspath(__file__))
    pastas = ["lista-01", "lista-02"]
    
    erros = 0
    arquivos_analisados = 0
    
    print("--- INICIANDO VERIFICAÇÃO AUTOMÁTICA DE ADERÊNCIA ---")
    print("Regras Validadas:")
    print("  1. Compilação da Sintaxe (Livre de Erros)")
    print("  2. Ausência de Definições de Funções ('def')")
    print("  3. Ausência de Blocos 'if __name__ == \"__main__\":'\n")
    
    for pasta in pastas:
        caminho_pasta = os.path.join(diretorio_base, pasta)
        if not os.path.exists(caminho_pasta):
            print(f"Erro: Pasta '{pasta}' não foi localizada.")
            continue
            
        print(f"Analisando arquivos em: {pasta}/")
        arquivos = sorted([f for f in os.listdir(caminho_pasta) if f.endswith(".py")])
        
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(caminho_pasta, arquivo)
            arquivos_analisados += 1
            
            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                conteudo = f.read()
                
            # Regra 1: Compilação de sintaxe
            try:
                tree = ast.parse(conteudo, filename=arquivo)
            except SyntaxError as e:
                print(f"  [ERRO DE SINTAXE] {pasta}/{arquivo}: Linha {e.lineno} - {e.msg}")
                erros += 1
                continue
                
            # Regra 2 & 3: Inspeção do AST (Abstract Syntax Tree)
            tem_funcao = False
            tem_main_guard = False
            
            for node in ast.walk(tree):
                # Procura por nós do tipo FunctionDef
                if isinstance(node, ast.FunctionDef):
                    tem_funcao = True
                    
                # Procura por nós do tipo If com expressão "if __name__ == '__main__':"
                if isinstance(node, ast.If):
                    if isinstance(node.test, ast.Compare):
                        # Verifica se compara __name__ com '__main__'
                        left = node.test.left
                        if isinstance(left, ast.Name) and left.id == "__name__":
                            for comparator in node.test.comparators:
                                if isinstance(comparator, ast.Constant) and comparator.value == "__main__":
                                    tem_main_guard = True
                                elif isinstance(comparator, ast.Str) and comparator.s == "__main__":
                                    tem_main_guard = True
                                    
            if tem_funcao:
                print(f"  [VIOLAÇÃO: FUNÇÃO DETECTADA] {pasta}/{arquivo} contém definições 'def'")
                erros += 1
            if tem_main_guard:
                print(f"  [VIOLAÇÃO: MAIN GUARD DETECTADA] {pasta}/{arquivo} contém blocos '__main__'")
                erros += 1
                
    print("\n--- RESUMO DA VERIFICAÇÃO ---")
    print(f"Total de arquivos analisados: {arquivos_analisados} / 60")
    if erros == 0:
        print("RESULTADO: SUCESSO ABSOLUTO! Todos os arquivos estão em conformidade e livres de erros.")
    else:
        print(f"RESULTADO: FALHA! Encontrados {erros} erros/violações nas regras estabelecidas.")

if __name__ == "__main__":
    verificar_arquivos()
