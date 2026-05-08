import sys
import os
import time

AZ    = "\033[1;34m"
VER   = "\033[1;32m"
VERM  = "\033[1;31m"
CI    = "\033[1;36m"
AM    = "\033[1;33m"
RESET = "\033[0m"

def continuar():
    while True:
        escolha = input(f'{CI}Deseja calcular novamente? {RESET}{AM}(s/n){RESET}\n> ').strip().lower()

        if escolha in ('s', 'sim'):
            return True
        elif escolha in ('n', 'nao', 'não'):
            return False
        else:
            print('Digite apenas s ou n!')

def titulo(texto, subtitulo=None, cor=CI, largura=40):
    print(f"{cor}╭{'─' * largura}╮")
    print(f"│{str(texto).upper().center(largura)}│")
    if subtitulo:
        print(f"│{'-' * largura}│")
        print(f"│{subtitulo.center(largura)}│")
    print(f"╰{'─' * largura}╯{RESET}")

def animacao(palavra, cor=AM):
    sys.stdout.write(f"{cor}{palavra}")
    for _ in range(3):
        time.sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()
    print(f"{RESET}\n")

def entrada_padrao(menssagem='Digite números um por um para calcular e escreva "calcular" para ver o total\n> '):
    coloca_menssagem = input(menssagem).strip().lower()
    return coloca_menssagem

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def opcoes():
    print(f'''
{CI}1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
0 - Sair
{RESET}''')

inicio_flag = True
while inicio_flag:
    limpar()
    titulo(f'{AM}Calculadora{RESET}')
    opcoes()
    operador = input(f'{VER}Escolha uma operação{RESET}\n> ').strip().lower()

    match operador:
        case '1':
            titulo('Soma')
        case '2':
            titulo('Subtração')
        case '3':
            titulo('Multiplicação')
        case '4':
            titulo('Divisao')
        case '0':
            animacao(f'{VERM}Encerrando sistema{RESET}')
            sys.exit()

    if operador not in {'0', '1', '2', '3', '4'}:
        print(f"{VERM}Operação inválida!{RESET}")
        time.sleep(1)
        continue

    calculo_flag = True
    numeros = []
    while calculo_flag:
        entrada = input(f'{CI}Dige os numeros que voce quer utilizar e (calcular) para calcular\n> {RESET}').strip().lower()
        if entrada == 'calcular':
            if len(numeros) < 2:
                print(f'{VERM}Erro!! Voce deve digitar no minimo 2 numeros para realizar o calculo{RESET}')
                time.sleep(1.8)
                continue
            else:
                animacao('Processando')
                try:
                    resultado = numeros[0]
                    for i in numeros[1:]:
                        if operador == '1':
                            resultado += i
                        elif operador == '2':
                            resultado -= i
                        elif operador == '3':
                            resultado *= i
                        elif operador == '4':
                            resultado /= i

                    print(f'{VER}O resultado da operação é\n> {resultado}{RESET}')
                    print(f'{AZ}Numeros usados\n> {numeros}{RESET}')

                    if continuar():
                        calculo_flag = False
                    else:
                        animacao('Encerrando Sistema')
                        limpar()
                        sys.exit()

                except ZeroDivisionError:
                    print('Não é possivel fazer uma divisão por zero')

        else:
            try:
                numeros.append(float(entrada))
                print(numeros)
            except ValueError:
                print(f'{VERM} e possivel o uso de numeros{RESET}')
                time.sleep(1)
                animacao(f'{VERM}Voltando{RESET}')
                continue
