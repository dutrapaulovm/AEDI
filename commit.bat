@echo off
:: Configura o encoding do console para UTF-8 para exibir caracteres e acentos em Português corretamente
chcp 65001 > nul

echo ======================================================
echo             ASSISTENTE DE COMMIT - GIT
echo ======================================================
echo.

:: Verifica se o diretório atual contém um repositório Git
if not exist .git (
    echo [ERRO] Este diretório não é um repositório Git ativo!
    echo Certifique-se de executar este script na pasta raiz onde o diretório .git está localizado.
    goto end
)

:: Exibe o status atual simplificado
echo Status atual das suas alterações:
echo ------------------------------------------------------
git status -s
echo ------------------------------------------------------
echo.

:: Pergunta se deseja adicionar todos os arquivos modificados/novos
set /p add_choice="Deseja preparar todas as alterações (git add .)? [S/N]: "
if /i "%add_choice%"=="S" (
    echo Preparando arquivos...
    git add .
    echo.
) else (
    echo Pulando preparo automático. Assumindo que você já preparou (git add) o que precisava.
    echo.
)

:: Solicita a mensagem do commit de forma interativa
:ask_message
set "commit_message="
set /p commit_message="Digite a mensagem do seu commit (obrigatório): "
if "%commit_message%"=="" (
    echo [AVISO] A mensagem de commit não pode ser vazia!
    goto ask_message
)

:: Realiza o commit
echo.
echo Executando o commit...
git commit -m "%commit_message%"
if %errorlevel% neq 0 (
    echo.
    echo [ERRO] Houve um problema ao realizar o commit. 
    echo Verifique se há alterações preparadas (staged) para serem salvas.
    goto end
)
echo.
echo [SUCESSO] Commit realizado com sucesso!
echo.

:: Pergunta se deseja realizar o envio (git push)
set /p push_choice="Deseja enviar (git push) as alterações para o repositório remoto? [S/N]: "
if /i "%push_choice%"=="S" (
    echo.
    echo Enviando alterações...
    git push
    if %errorlevel% neq 0 (
        echo.
        echo [ERRO] Falha ao enviar as alterações (git push).
    ) else (
        echo.
        echo [SUCESSO] Alterações enviadas com sucesso ao repositório remoto!
    )
)

:end
echo.
echo ======================================================
echo Script finalizado. Pressione qualquer tecla para sair.
echo ======================================================
pause > nul
