import os
import time
import sys

def animacao(cor, palavra):
    sys.stdout.write(f"{cor}{palavra}")
    for _ in range(3):
        time.sleep(0.6)
        sys.stdout.write(".")
        sys.stdout.flush()
    print(f"{RESET}\n")

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

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


AZ      = "\033[1;34m"
VERD     = "\033[1;32m"
VERM  = "\033[1;31m"
CI     = "\033[1;36m"
AMA   = "\033[1;33m"
RESET     = "\033[0m"
LA   = "\033[33m"

while True:
    try:
        limpar()
        linha(CI, LA, "CALCULADORA")
        digite_operacao = input("Digite a sua operação matematica\n> ")
        calc_sair = input("Pressione (s) para sair ou (c) para calcular\n> ").lower().strip()
        if calc_sair in ["c"]:
            animacao(AMA, "Calculando")
            time.sleep(0.6)
            resultado = eval(digite_operacao)
            print(resultado)
        elif ["s"]:
            animacao(AMA, "Encerrando sistema")
            time.sleep(0.4)
            sys.exit()
        else:
            print("ERRO!!! Digite (s) ou (n)")
            time.sleep(1.2)
            continue
    except ValueError:
        print("Digte apenas numeros")
    except Exception as e:
        print(f'Um erro do tpo {e} ocorreu')
