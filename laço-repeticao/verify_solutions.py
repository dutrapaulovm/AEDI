# Script de Verificação de Soluções
# Objetivo: Compilar e validar sintaticamente cada arquivo Python das listas para garantir integridade absoluta.

import os
import py_compile

def verificar_diretorio(diretorio):
    print(f"\nVerificando diretório: {diretorio}")
    arquivos = sorted(os.listdir(diretorio))
    validos = 0
    erros = 0
    
    for arq in arquivos:
        if arq.endswith(".py"):
            caminho_completo = os.path.join(diretorio, arq)
            try:
                # Tenta compilar o arquivo para bytecode
                py_compile.compile(caminho_completo, doraise=True)
                print(f"  [OK] {arq} compilado com sucesso.")
                validos += 1
            except py_compile.PyCompileError as e:
                print(f"  [ERRO] {arq} possui erros de compilação/sintaxe!")
                print(f"    Detalhes: {e}")
                erros += 1
                
    return validos, erros

# Diretórios das listas
dir_lista1 = os.path.join("laço-repeticao", "lista-01")
dir_lista2 = os.path.join("laço-repeticao", "lista-02")

total_ok = 0
total_erro = 0

# Verifica Lista 1
v1, e1 = verificar_diretorio(dir_lista1)
total_ok += v1
total_erro += e1

# Verifica Lista 2
v2, e2 = verificar_diretorio(dir_lista2)
total_ok += v2
total_erro += e2

# Dashboard final de verificação
print("\n" + "="*50)
print("DASHBOARD FINAL DE VERIFICAÇÃO")
print(f"Total de arquivos Python válidos: {total_ok}")
print(f"Total de arquivos com erros de sintaxe: {total_erro}")
print("="*50)

if total_erro == 0:
    print("Sucesso! Todos os arquivos estão perfeitamente corretos e prontos para entrega!")
else:
    print("Atenção: Por favor, corrija os erros de sintaxe listados acima antes de entregar.")
print("="*50)
