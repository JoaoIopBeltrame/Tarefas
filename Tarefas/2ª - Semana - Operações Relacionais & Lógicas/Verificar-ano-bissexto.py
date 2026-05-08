import os
import time
import sys

AZUL      = "\033[1;34m"
VERDE     = "\033[1;32m"
VERMELHO  = "\033[1;31m"
AMARELO   = "\033[1;33m"
CIANO     = "\033[1;36m"
RESET     = "\033[0m"
LARANJA   = "\033[33m"

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def titulo(COR_BORDA, COR_TEXTO, TITULO):
    largura = 50
    print(f"{COR_BORDA}+" + "-" * largura + f"+{RESET}")
    texto_centralizado = f"{TITULO:^{largura}}"
    print(f"{COR_BORDA}|{RESET}{COR_TEXTO}{texto_centralizado}{RESET}{COR_BORDA}|{RESET}")
    print(f"{COR_BORDA}+" + "-" * largura + f"+{RESET}")
    print()

def animacao(cor, palavra):
    sys.stdout.write(f"{cor}{palavra}")
    for _ in range(3):
        time.sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()
    print(f"{RESET}\n")

while True:
    try:
        limpar()
        titulo(LARANJA, CIANO, "ANO BISSEXTO OU NAO")

        digitar_ano = input(f"{VERDE}Digite o ano ou{RESET}{VERMELHO} 'sair'{RESET}\n").strip()
        
        if digitar_ano in ["SAIR", "sair", "Sair"]:
            animacao(VERMELHO, "Encerrando sistema")
            sys.exit()

        digitar_ano_int = int(digitar_ano)
        
        if (digitar_ano_int % 4 == 0 and digitar_ano_int % 100 != 0) or (digitar_ano_int % 400 == 0):
            print(f"{VERDE}O ANO {AMARELO}{digitar_ano_int}{RESET} {VERDE}É BISSEXTO{RESET}")
        else:
            print(f"{VERMELHO}O ANO {AMARELO}{digitar_ano_int}{RESET} {VERMELHO}NÃO É BISSEXTO{RESET}")
        
        time.sleep(1.5)

        while True:
            denovo = input(f"\n{CIANO}Deseja calcular outro ano?{RESET} {AMARELO}(s/n){RESET}\n").lower().strip()
            if denovo in ["sim", "s"]:
                animacao(AMARELO, "Reiniciando")
                break
            elif denovo in ["nao", "n"]:
                animacao(VERMELHO, "Desligando")
                sys.exit()
            else:
                print(f"{VERMELHO}Digite apenas (sim) ou (nao)!{RESET}")
                time.sleep(1)
                continue
            
    except ValueError:
        print(f"{VERMELHO}Erro! Digite apenas números inteiros.{RESET}")
        time.sleep(2)
        continue
    except Exception as e:
        print(f"Erro inesperado: {e}")
        break
