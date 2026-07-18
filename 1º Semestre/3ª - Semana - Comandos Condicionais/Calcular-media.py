import os
import time
import sys

AZ    = "\033[1;34m"
VER   = "\033[1;32m"
VERM  = "\033[1;31m"
CI    = "\033[1;36m"
AM    = "\033[1;33m"
RESET = "\033[0m"

def animacao(cor, palavra):
    sys.stdout.write(f"{cor}{palavra}")
    for _ in range(3):
        time.sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()
    print(f"{RESET}\n")

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho(titulo, subtitulo=""):
    largura = 60
    linhas = [titulo.upper()]
    if subtitulo:
        linhas.append(subtitulo)

    maior = max(len(l) for l in linhas)
    largura = max(largura, maior + 4)

    print(f"{AZ}╔{'═'*largura}╗")
    for linha in linhas:
        esp = largura - len(linha)
        esq = esp // 2
        dir = esp - esq
        print(f"║{' '*esq}\033[1;37m{linha}{RESET}{AZ}{' '*dir}║")
    print(f"╚{'═'*largura}╝{RESET}")

while True:
    lista_numeros = []

    while True:
        try:
            limpar()
            cabecalho("Sistema de Notas", "Digite -1 para finalizar")

            notas = input(f"{CI}> {RESET}").strip()
            numero = float(notas)

            if numero == -1:
                break

            lista_numeros.append(numero)

        except ValueError:
            print(f"{VERM}Digite apenas números válidos!{RESET}")
            time.sleep(1.2)

    limpar()
    animacao(AM, "Processando")

    if lista_numeros:
        media = sum(lista_numeros) / len(lista_numeros)
        cabecalho("Resultado Final", f"Média: {media:.2f}")
        print(f"{VER}Valores armazenados: {lista_numeros}{RESET}\n")
    else:
        cabecalho("Resultado Final", "Nenhum número válido inserido")

    while True:
        time.sleep(0.7)
        continuar = input("\nGostaria de calcular novamente? (s/n): ").lower().strip()

        if continuar == "s":
            animacao(CI, "Reiniciando")
            time.sleep(0.5)
            break

        elif continuar == "n":
            animacao(AM, "Encerrando sistema")
            time.sleep(0.5)
            limpar()
            sys.exit()

        else:
            print("Opção inválida! Digite apenas 's' ou 'n'.")
            time.sleep(1)
