import os
import time
import sys

AZUL      = "\033[1;34m"
VERDE     = "\033[1;32m"
VERMELHO  = "\033[1;31m"
CIANO     = "\033[1;36m"
AMARELO   = "\033[1;33m"
RESET     = "\033[0m"
LARANJA   = "\033[33m"

def linha(cor_titulo, cor_borda, titulo):
    largura = 40
    titulo = f" {titulo.upper()} "
    
    restante = largura - len(titulo)
    esq = restante // 2 
    dir = restante - esq
    
    C, T, R = cor_borda, cor_titulo, RESET
    
    print(f"{C}╭{'─' * largura}╮")
    print(f"{C}│{' ' * esq}{T}{titulo}{R}{C}{' ' * dir}│")
    print(f"{C}╰{'─' * largura}╯{R}")

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def animacao(cor, palavra):
    sys.stdout.write(f"{cor}{palavra}")
    for _ in range(3):
        time.sleep(0.3)
        sys.stdout.write(".")
        sys.stdout.flush()
    print(f"{RESET}\n")

def mostrar_tabuada(n):
    print(f"\n{CIANO}Tabuada do {n}:{RESET}\n")
    
    for i in range(1, 11):
        print(f"{VERDE}{n}{RESET} x {AMARELO}{i:2}{RESET} = {AZUL}{n * i:2}{RESET}")
    
    print()

while True:
    try:
        limpar()
        linha(CIANO, VERDE, "TABUADA")

        numero_sair = input(f"{VERDE}Digite um número {AMARELO}(1-10){VERDE} ou {VERMELHO}(sair){RESET}\n> ").strip().lower()

        if numero_sair == "sair":
            animacao(LARANJA, "Encerrando")
            break

        if not numero_sair.isnumeric():
            print(f"{VERMELHO}Entrada inválida. Use apenas números.{RESET}")
            time.sleep(1.2)
            continue

        valor = int(numero_sair)

        if not (1 <= valor <= 10):
            print(f"{VERMELHO}Número fora do intervalo permitido.{RESET}")
            time.sleep(1.2)
            continue

        limpar()
        linha(CIANO, VERDE, f"TABUADA DO {valor}")
        mostrar_tabuada(valor)

        input(f"{AMARELO}Pressione ENTER para continuar...{RESET}")

    except Exception as e:
        print(f"{VERMELHO}Erro inesperado:{RESET} {e}")
        time.sleep(2)
        
