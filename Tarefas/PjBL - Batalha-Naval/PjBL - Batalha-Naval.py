import sys
import os
import time
import random

AZ   = "\033[34m"; VERD = "\033[32m"; VERM = "\033[31m"
CI   = "\033[36m"; AMA  = "\033[33m"; ROSA = "\033[35m"
NEG  = "\033[1m";  RE   = "\033[0m"
HIDE = "\033[?25l"; SHOW = "\033[?25h"

def seleciona_navios():
    MOLDURA = AZ + NEG
    TITULO  = AMA + NEG
    TEXTO   = CI
    NUMERO  = VERM + NEG
    VALOR   = VERD + NEG

    print(f'''{HIDE}{MOLDURA}╔═══════════════════════════════════════════════════════╗
║                                                       ║
║  {TITULO}EMBARCAÇÕES{MOLDURA}                             {TITULO}ESPAÇAMENTO{MOLDURA}  ║
║  {NUMERO}1{TEXTO}: Adicionar Porta-aviões                   {VALOR}5{MOLDURA}        ║
║  {NUMERO}2{TEXTO}: Adicionar Navio-tanque                   {VALOR}4{MOLDURA}        ║
║  {NUMERO}3{TEXTO}: Adicionar Contratorpedeiro               {VALOR}3{MOLDURA}        ║
║  {NUMERO}4{TEXTO}: Adicionar Submarino                      {VALOR}2{MOLDURA}        ║
║  {NUMERO}5{TEXTO}: Adicionar Destroier                      {VALOR}1{MOLDURA}        ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝{RE}{SHOW}''')

def limp_term():
    os.system('cls' if os.name == 'nt' else 'clear')

def terminal_voltando(palavra='Reiniciando'):
    sys.stdout.write(HIDE)
    for loop_maior in range(4):
        limp_term()
        sys.stdout.write(palavra)
        for loop_menor in range(3):
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write(SHOW)

def voltar_opcao():
    voltar = input('Pressione (z) para desfazer ou ENTER para continuar\n> ').strip().lower()
    if voltar == 'z':
        terminal_voltando('Voltando')
        return True
    return False

def matriz_jogador():
    mar = []
    for i in range(10):
        linha_mar = []
        for j in range(10):
            linha_mar.append(0)
        mar.append(linha_mar)

    print("\n    " + " ".join([str(num) for num in range(10)])) 
    print("   " + "═" * 21)
    for i, linha in enumerate(mar):
        print(f"{i} ║ " + " ".join(map(str, linha))) 
    return mar

def posicionar_navio(matriz, casasNavio, numeroNavio):
    while True:
        random_I = random.randint(0, 9)
        random_J = random.randint(0, 9)
        randomNavio = random.randint(0, 1)

        if randomNavio == 0 and random_J + casasNavio > 10:
            continue
        if randomNavio == 1 and random_I + casasNavio > 10:
            continue

        naoOcupado = True
        for i in range(casasNavio):
            if randomNavio == 0:
                if matriz[random_I][random_J + i] != 0:
                    naoOcupado = False
            else:
                if matriz[random_I + i][random_J] != 0:
                    naoOcupado = False
        if not naoOcupado:
            continue

        for k in range(casasNavio):
            if randomNavio == 0:
                matriz[random_I][random_J + k] = numeroNavio
            else:
                matriz[random_I + k][random_J] = numeroNavio
        break

porta_avioes = 1
navio_tanque = 1
contratorpedeiro = 1
submarino = 1
destroier = 1

def main():
    while True:
        print('Digite (1) para jogar')
        print('Digite (2) para ver as informações do jogo')
        escolha = input('\n> ')

        if escolha == '1':
            limp_term()
            print('\nEsse é o seu tabuleiro:')
            mar = matriz_jogador() 
            
            while True:
                print('\nEscolha a sua embarcação:')
                print(f'''CÓDIGO:                 RESTANTES: 
1- Destroier ----------- [{destroier}]
2- Submarino ----------- [{submarino}]
3- Contratorpedeiro ---- [{contratorpedeiro}]
4- Navio-tanque -------- [{navio_tanque}]
5- Porta-aviões -------- [{porta_avioes}]''')
                
                embarcacao = input('\n> ').strip().lower()
                
                if embarcacao in ('1', 'destroier'):
                    if voltar_opcao(): 
                        limp_term()
                        mar = matriz_jogador() 
                        continue                    

                    print("Navio adicionado com sucesso!")
                    break
                
        elif escolha == '2':
            limp_term()
            seleciona_navios()
            voltar = input('Pressione ENTER para voltar\n> ')
            if voltar == '':
                limp_term()
                continue

if __name__ == "__main__":
    main()
