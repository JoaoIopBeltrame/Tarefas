# add o negocio de selecionar onde vai as embarcações 
#   add tabela ASCII, cores e etc
# add tratamento de desenhos no termnal
# add insert para saber indice em que os troços vao ficar 
# add if opcaçao ja escolhida (1, 2, 3, 4 ou 5) ai nao deixa/aceita o input do numero respectivo          
# se quiser tira os while com flag
#  coloque como usar as cores da tabela ascii 

import sys
import os
import time
import random

AZ   = "\033[34m"; VERD = "\033[32m"; VERM = "\033[31m"
CI   = "\033[36m"; AMA  = "\033[33m"; ROSA = "\033[35m"
NEG  = "\033[1m";  RE   = "\033[0m"
HIDE = "\033[?25l"; SHOW = "\033[?25h"

def seleceiona_navios():
    print('''
           _______________________________________________________  
          |                                                       |
          |  EMBARCAÇÕES                             ESPAÇAMENTO  |
          |  1: Adicionar Porta-aviões                   5        |  
          |  2: Adicionar Navio-tanque                   4        |
          |  3: Adicionar Contratorpedeiro               3        |
          |  4: Adicionar Submarino                      2        |
          |  5: Adicionar Destroier                      1        |
          |                                                       |
          |_______________________________________________________|
    ''')

def lista_batalha_naval():
    matriz_principal = []
    for i in range(1, 11):
        linha = []
        for j in range(1, 11):
            linha.append(0)
        matriz_principal.append(linha)
    return matriz_principal
            
def inputs(frase, tipo):
    entrada = input(f'{frase}\n> ')
    if tipo == str:
        return entrada.capitalize()
    else: 
        return tipo(entrada)

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

def main():
    while True:
        inputs('Digite (1) para ver as informações do jogo e (2) para jogar')
        if entrada == '1':
            seleceiona_navios()
            inputs('Pressione ENTER para voltar a tela inicial')
            if entrada == '':
                terminal_voltando('Voltando')
                continue
        else:
            print('Digite 1 para as informações e 0 para iniciar o jogo')
                





if __name__ == '__main__':
    main()
