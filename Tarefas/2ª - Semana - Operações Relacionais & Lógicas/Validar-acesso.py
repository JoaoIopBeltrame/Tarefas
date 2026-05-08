import os
import time
import sys

AZUL      = "\033[1;34m"
LARANJA   = "\033[33m"
VERDE     = "\033[1;32m"
VERMELHO  = "\033[1;31m"
AMARELO   = "\033[1;33m"
CIANO     = "\033[1;36m"
RESET     = "\033[0m"

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def titulo():
    print(f"{AZUL}+" + "-" * 38 + f"+{RESET}")
    print(f"{AZUL}|{RESET}{'ABSOLUTE CINEMA':^38}{AZUL}|{RESET}")
    print(f"{AZUL}+" + "-" * 38 + f"+{RESET}")
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
        titulo()
        entrada = input(f"{VERDE}Digite a sua idade!{RESET} Digite{AMARELO} sair{RESET} para finalizar:\n").lower().strip()
        
        if entrada == "sair":
            animacao(AMARELO, "Finalizando sistema")
            break 

        digite_idade_int = int(entrada)
        possuir_ingresso = False

        while True:
            tem_ingresso = input("Você possui ingresso? (sim/nao): ").lower().strip()
            
            if tem_ingresso in ["sim", "s"]:
                possuir_ingresso = True
                break
            
            elif tem_ingresso in ["nao", "n"]:
                quer_ingresso = input("Deseja comprar o ingresso? (sim/nao): ").lower().strip()
                
                if quer_ingresso in ["sim", "s"]:
                    if digite_idade_int >= 18:
                        animacao(AMARELO, "Comprando o ingresso")
                        possuir_ingresso = True
                        break
                    else:
                        print(f"{VERMELHO}COMPRA NEGADA! Menores de 18 não podem comprar.{RESET}")
                        time.sleep(2)
                        break
                else:
                    animacao(AMARELO, "Compra não efetuada")
                    break
            else:
                print("Por favor, responda com 'sim' ou 'nao'.")

        print(f"{VERDE}---------- RESULTADO ----------{RESET}")
        match (digite_idade_int >= 18, possuir_ingresso):
            case (True, True):
                print(f"{VERDE}Acesso permitido! Bom filme!{RESET}")
            case (True, False):
                print(f"{AMARELO}Acesso negado! Compre o ingresso.{RESET}")
            case (False, True):
                print(f"{LARANJA}Acesso negado! Filme proibido para menores.{RESET}")
            case (False, False):
                print(f"{VERMELHO}Acesso negado! Sem idade e sem ingresso.{RESET}")
        
        input(f"\n{CIANO}Pressione Enter para continuar...{RESET}")

    except ValueError:
        print(f"{VERMELHO}Entrada inválida! Digite apenas números para a idade.{RESET}")
        time.sleep(2)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        time.sleep(2)
