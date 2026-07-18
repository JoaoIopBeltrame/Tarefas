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

def titulo(TITULO):
    print("+" + "-" * 50 + "+")
    print(f"|{TITULO:^{50}}|")
    print("+" + "-" * 50 + "+")
    print()

def animacao(cor, palavra):
    sys.stdout.write(f"{cor}{palavra}")
    for i in range(3):
        time.sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()
    print(f"{RESET}\n")

while True:
    try:
        limpar()
        titulo("O NUMERO ESTA ENTRE???")

        numero_input = input(f"{VERDE}Digite o seu número ou digite{RESET}{VERMELHO} 'SAIR' {RESET}{VERDE} para encerrar o sistema\n").lower().strip()
        
        if numero_input == "sair":
            animacao(AMARELO, "ENCERRANDO SISTEMA")
            sys.exit()
        
        if not numero_input:
            time.sleep(1.3)
            continue

        numero_input_float  = float(numero_input)
        if numero_input_float < 10:
            print(f"O numero {numero_input_float} é menor do que 10")
        elif 10 <= numero_input_float <= 50:
            print(f"O numero {numero_input_float} está entre 10 e 50 ")
        else:
            print(f"O numero {numero_input_float} é maior do que 50")
        time.sleep(2.5) 

        while True:
            limpar()
            titulo(f"QUER IR DE NOVO??")
            fazer_novamente = input("Deseja usar o programa novamente? (sim)/(nao)\n").lower().strip()
            if fazer_novamente in ["sim", "s"]:
                animacao(AMARELO, "Reiniciando")
                break
            elif fazer_novamente in ["nao", "n"]:
                animacao(AMARELO, "Desligando sistema")
                sys.exit()
            else:
                print("Digite apenas (sim)/(nao)")
                time.sleep(1.5)
                continue
    
    except ValueError:
        print(f"{VERMELHO}Entrada inválida! Digite apenas números.{RESET}")
        time.sleep(2)
        
    except Exception as e:
        print(f"{LARANJA}Ocorreu um erro inesperado: {e}")
        time.sleep(2)
