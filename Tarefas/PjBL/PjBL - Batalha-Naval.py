# add o negocio de selecionar onde vai as embarcações 
    # add tabela ASCII, cores e etc
    # add tratamento de desenhos no termnal
    # add insert para saber indice em que os troços vao ficar 
    # add if opcaçao ja escolhida (1, 2, 3, 4 ou 5) ai nao deixa/aceita o input do numero respectivo          
    # se quiser tira os while com flag
    #  coloque como usar as cores da tabela ascii 

import sys
import os
import time
import random

# player2 = True
escolher_opcao = True

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

def escolher_local():
    indice = input('Digite o indice\n> ')
    embarcacao = input('Digite a embarcação\n> ')
    return indice, embarcacao


def lista_batalha_naval():
    matriz_principal = []
    for i in range(11):
        linhas = []
        for j in range(11):
            linhas.append(0)
        matriz_principal.append(linhas)
    return matriz_principal

def perguntar(teste):
    return input(f'{teste}\n> ').capitalize().strip()

def por_nome():
    return input('Digita o nome\n> ').capitalize().strip()

def limpar_termi():
    os.system('cls' if os.name == 'nt' else 'clear')

def anim_reini(palavra='Reiniciando'):
    sys.stdout.write(HIDE)
    for maior in range(4):
        limpar_termi()
        sys.stdout.write(palavra)
        for menor in range(4):
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(0.1)
        print()
    sys.stdout.write(SHOW)

def ver_info():
    return input('Digite 1 para ver as informações ou ENTER para prosseguir\n> ')

def main():
    player1 = True
    print('BATALHA NAVAL') # add um whie loop e um continue para fazer as coisa e pa    
    info = ver_info()
    if info not in ('1', ''):
        print('Digite 1 ou pressione enter')
    while player1:
        limpar_termi()
        player1 = por_nome()
        
        if player1 == '':
            print('Digite um nome válido!')
            time.sleep(1.2)
            anim_reini('Voltando')
            player1 = True
            continue
        
        
    # while player2:
    #     player2 = por_nome()

    #     if player2 == player1:
    #         while escolha:
    #             resposta = escolha(f"como {player1}(1)")
    #             escolha('S para sm e N para não')
    #             if escolha == ['S', 'Sim']:
    #                 pass
    #             elif escolha == ['N', 'Não', 'Nao']:
    #                 continue
    #             else:
    #                 print('Bruhhh')
    #                 continue
    #         player2 = False

    print("TESTE")
    limpar_termi()

    #parte do jogador que vai elscolher qual navio usar
    print(f"Vez do {player1}")
    for i in range(5):
        seleceiona_navios()
        print('Selecione qual voce quer posicionar')
        opcao = input('Selecione a embarcação que voce quer\n> ')
        # while escolher_opcao:
        #     if opcao == '1':
        #         escolher_local()

                

        #     elif opcao == '2'

        #     elif opcao == '3'

        #     elif opcao == '4'

        #     elif opcao == '5'

        #     else:
        #         opcao not in ('1','2','3','4','5')
        #         print('digite apenas opcaoes')
        #         time.sleep(1.2)
        #         anim_reini('voltando')
        #         continue
        # print(matriz10x10())



if __name__ == '__main__':
    main()
