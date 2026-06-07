# add visuais de interface no estilo daquele do pedra pael tesoura e se possivel deixar as o output do terminal mais foda, tipo, arrumado, colorido e com uns desenho e pa
#e como desenhos

import sys
import os
import time
import random

AZ   = "\033[34m"; VERD = "\033[32m"; VERM = "\033[31m"
CI   = "\033[36m"; AMA  = "\033[33m"; ROSA = "\033[35m"
NEG  = "\033[1m";  RE   = "\033[0m"
HIDE = "\033[?25l"; SHOW = "\033[?25h"

NOMES = ['', 'destroier', 'submarino', 'contratorpedeiro', 'Navio-tanque', 'Porta-aviões']

def mostrarRegras():
    print(f"""{CI}
    =============== BATALHA NAVAL ===============
    1. Tabuleiro 10x10 (linhas 0-9, colunas 0-9).
    2. Posicione seus navios na horizontal ou vertical.
    3. Navios nao podem se sobrepor nem sair da grade.
    4. A cada turno voce atira em uma coordenada (ex: linha 5 coluna 3).
    5. Resposta: AGUA (errou) ou ACERTOU (atingiu).
    6. Um navio so AFUNDA quando todas as casas dele sao atingidas.
    7. Vence quem afundar toda a frota inimiga primeiro.
    ============================================= {RE}""")

def navioUI():
    MOLDURA = AZ + NEG
    TITULO  = AMA + NEG
    TEXTO   = CI
    NUMERO  = VERM + NEG
    VALOR   = VERD + NEG
    print(f'''{HIDE}{MOLDURA}    ╔═══════════════════════════════════════════════════════╗                      
    ║                                                       ║       
    ║  {TITULO}EMBARCAÇÕES{MOLDURA}                             {TITULO}ESPAÇAMENTO{MOLDURA}  ║                                             
    ║  {NUMERO}1{TEXTO}: Adicionar Porta-aviões                   {VALOR}5{MOLDURA}        ║
    ║  {NUMERO}2{TEXTO}: Adicionar Navio-tanque                   {VALOR}4{MOLDURA}        ║
    ║  {NUMERO}3{TEXTO}: Adicionar Contratorpedeiro               {VALOR}3{MOLDURA}        ║                                        
    ║  {NUMERO}4{TEXTO}: Adicionar Submarino                      {VALOR}2{MOLDURA}        ║                                        
    ║  {NUMERO}5{TEXTO}: Adicionar Destroier                      {VALOR}1{MOLDURA}        ║                                    
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝{RE}{SHOW}''')

def cleanTerm():
    os.system('cls' if os.name == 'nt' else 'clear')

def animacaoPalavra(palavra='Reiniciando'):
    sys.stdout.write(HIDE + AMA)
    for loop_maior in range(4):
        cleanTerm()
        sys.stdout.write(palavra)
        for loop_menor in range(3):
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write(RE + SHOW)

def matrizCPU():
    matriz = [[0 for _ in range(10)] for _ in range(10)]
    for casasNavio in [1, 2, 3, 4, 5]:
        numeroNavio = casasNavio
        while True:
            naoOcupado = True
            random_I = random.randint(0, 9)
            random_J = random.randint(0, 9)
            randomNavio = random.randint(0, 1)
            if randomNavio == 0 and random_J + casasNavio > 10:
                continue
            if randomNavio == 1 and random_I + casasNavio > 10:
                continue
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
    return matriz

def tabuleiro():
    matriz10x10 = []
    for lMaior in range(10):
        linhaMatriz10x10 = []
        for lMenor in range(10):
            linhaMatriz10x10.append(0)
        matriz10x10.append(linhaMatriz10x10)
    return matriz10x10

def mostraTabuleiro(matriz10x10):
    print(f'\n     {CI}' + '   '.join([str(num) for num in range(10)]) + f'{RE}')
    print(f'  {AZ}╔' + '═' * 40 + f'{RE}')
    for nume, linhaMatriz in enumerate(matriz10x10):
        print(f'{CI}{nume}{AZ} ║  {RE}' + '   '.join(map(str, linhaMatriz)))

def aindaTem(matrizCPU, numero):
    for linha in matrizCPU:
        if numero in linha:
            return True
    return False

def frotaDestruida(matrizCPU):
    for numero in [1, 2, 3, 4, 5]:
        if aindaTem(matrizCPU, numero):
            return False
    return True

def processaTiro(matriz, li, co):
    valor = matriz[li][co]
    matriz[li][co] = 0
    if valor == 0:
        print(f'{AZ}Voce errou o tiro (AGUA){RE}')
        return
    nome = NOMES[valor]
    print(f'{VERD}Voce acertou um {nome}!{RE}')
    if aindaTem(matriz, valor):
        print(f'{AMA}Há um pedaço restante do {nome}{RE}')
    else:
        print(f'{VERM}O {nome} foi totalmente destruido{RE}')

def voltarOpcao():
    voltar = input(f'{AMA}Pressione (z) para desfazer ou ENTER para continuar\n> {RE}').strip().lower()
    if voltar == 'z':
        animacaoPalavra()       
        cleanTerm()
        return True
    return False

def usuarioPosicao(matriz10x10, escolherNavio):
    casasNavio = int(escolherNavio)
    numPermitidos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        escolhePosicao = input('Digite (H) para Horizontal e (V) para Vertical\n> ').capitalize().strip()
        if escolhePosicao in ['H', 'Horizontal']:
            opcao = 1
            break
        elif escolhePosicao in ['V', 'Vertical']:
            opcao = 0
            break
        else:
            print('Digite apenas o que se pede')

    while True:
        porLinha = input('Digite uma linha de (0-9)\n> ')
        porColuna = input('Digite uma coluna de (0-9)\n> ')
        if not (porLinha.isdigit() and porColuna.isdigit()):
            print(f'{VERM}Digite apenas numeros de 0 a 9{RE}')
            time.sleep(1)           
            continue

        porLinhaInt = int(porLinha)
        porColunaInt = int(porColuna)
        if porLinhaInt not in numPermitidos or porColunaInt not in numPermitidos:
            print(f'{VERM}Digite um numero entre 0 a 9{RE}')
            time.sleep(1)            
            continue

        if opcao == 1 and porColunaInt + casasNavio > 10:
            print(f'{VERM}O numero ira exceder o limite do mapa{RE}')   
            continue
        if opcao == 0 and porLinhaInt + casasNavio > 10:
            print(f'{VERM}O numero ira exceder o limite do mapa{RE}')
            time.sleep(1)            
            continue

        naoOcupado = True
        for i in range(casasNavio):
            if opcao == 1:
                if matriz10x10[porLinhaInt][porColunaInt + i] != 0:
                    naoOcupado = False
            else:
                if matriz10x10[porLinhaInt + i][porColunaInt] != 0:
                    naoOcupado = False
        if not naoOcupado:
            print(f'{VERM}Ja tem um navio nesse caminho! Tente outra posicao.{RE}')
            time.sleep(1)            
            continue

        if opcao == 1:
            print(f'{VERD}Modo Horizontal escolhido{RE}')
            for k in range(casasNavio):
                matriz10x10[porLinhaInt][porColunaInt + k] = casasNavio
        else:
            print(f'{VERD}Modo Vertical escolhido{RE}')
            for i in range(casasNavio):
                matriz10x10[porLinhaInt + i][porColunaInt] = casasNavio
        return True

def tiroCPU(matrizJogador):
    tiroCPUlinha = random.randint(0, 9)
    tiroCPUcoluna = random.randint(0, 9)
    valor = matrizJogador[tiroCPUlinha][tiroCPUcoluna]
    
    if valor == 0:
        print(f'{AZ}O navio inimigo errou (AGUA){RE}')
    else:
        nome = NOMES[valor]
        print(f'{VERM}O navio inimigo acertou o seu {nome}!{RE}')
        matrizJogador[tiroCPUlinha][tiroCPUcoluna] = 0
    return matrizJogador

def jogarNovamente():
    while True:
        jogarSN = input(f'{AMA}Deseja jogar novamente? (s) sim / (n) não\n> {RE}').strip().capitalize()
        if jogarSN in ['S', 'Sim']:
            return True
        elif jogarSN in ['N', 'Nao', 'Não']:
            return False
        print(f'{VERM}Digite apenas s ou n{RE}')

def faseDeCombate(matrizJogador):
    print(f'{VERM}A tropa inimiga ja posicionou suas tropas{RE}')
    matrizInimigo = matrizCPU()

    while not frotaDestruida(matrizInimigo):
        print(f'\n{CI}==== SEU TABULEIRO ===={RE}')
        mostraTabuleiro(matrizJogador)
        
        tiroLinha = input(f'{CI}\nDigite a linha do tiro (0-9)\n> {RE}')
        tiroColuna = input(f'{CI}Digite a coluna do tiro (0-9)\n> {RE}')
        tiro = input(f'{CI}Digite o codigo secreto (ou ENTER para atirar)\n> {RE}')

        if not (tiroLinha.isdigit() and tiroColuna.isdigit()):
            print(f'{VERM}Digite apenas numeros de 0 a 9{RE}')
            continue

        tiroLinhaInt = int(tiroLinha)
        tiroColunaInt = int(tiroColuna)
        if tiroLinhaInt < 0 or tiroLinhaInt > 9 or tiroColunaInt < 0 or tiroColunaInt > 9:
            print(f'{VERM}Digite numeros de 0 a 9{RE}')
            continue
        if tiro == 'ccbbededba':
            print(f'{ROSA}Codigo secreto ativado{RE}')
            animacaoPalavra('Usando sonar')                  
            animacaoPalavra('Avaliando tropas inimigas')     
            print(f'{ROSA}Localização inimiga{RE}')
            mostraTabuleiro(matrizInimigo)
            processaTiro(matrizInimigo, tiroLinhaInt, tiroColunaInt)
            mostraTabuleiro(matrizInimigo)
            input(f'{AMA}Pressione ENTER para continuar\n> {RE}')
            continue
        else:
            print(f'\n{CI}==== SEU TIRO ===={RE}')
            processaTiro(matrizInimigo, tiroLinhaInt, tiroColunaInt)
            
            print(f'\n{ROSA}Tiro da CPU...{RE}')
            time.sleep(1)
            matrizJogador = tiroCPU(matrizJogador)
            
            if frotaDestruida(matrizJogador):
                print(f'\n{VERM}{NEG}DERROTA! A CPU afundou toda sua frota!{RE}')
                mostraTabuleiro(matrizJogador)
                break
            
            input(f'{AMA}Pressione ENTER para continuar\n> {RE}')
            continue
    
    print(f'\n{CI}==== RESULTADO FINAL ===={RE}')
    if frotaDestruida(matrizInimigo) and not frotaDestruida(matrizJogador):
        print(f'{VERD}{NEG}VITORIA! Voce afundou toda a frota inimiga!{RE}')
    elif frotaDestruida(matrizJogador):
        print(f'{VERM}{NEG}DERROTA! A CPU afundou toda sua frota!{RE}')

def main():
    while True:  # ADICIONADO: loop externo para jogar novamente
        naviosSobrando = 5
        porta_avioes = 1
        navio_tanque = 1
        contratorpedeiro = 1
        submarino = 1
        destroier = 1
        matriz10x10 = tabuleiro()
        
        while True:  # loop menu/posicionamento
            jogarInfo = input(f'{CI}Digite |(1) jogar| e |(2) ver inforação do jogo|\n> {RE}')
            if jogarInfo == '1':
                print(f'\n      {AMA}Tabuleiro atual{RE}')
                mostraTabuleiro(matriz10x10)
                print('\n')
                print(f'''{ROSA}          CÓDIGO:            RESTANTES: 
            1- Destroier ----------- [{destroier}]
            2- Submarino ----------- [{submarino}]
            3- Contratorpedeiro ---- [{contratorpedeiro}]
            4- Navio-tanque -------- [{navio_tanque}]
            5- Porta-aviões -------- [{porta_avioes}]{RE}''')
                escolherNavio = input(f'{CI}escolha um navio\n> {RE}')
                
                if naviosSobrando == 0:
                    faseDeCombate(matriz10x10)
                    break

                if escolherNavio == '1':
                    if destroier == 1:
                        usuarioPosicao(matriz10x10, escolherNavio)
                        destroier -= 1
                        naviosSobrando -= 1
                        print(f'{VERD}Destroier posicionado!{RE}')
                    else:
                        print(f'{NEG}{VERM}Voce ja posicionou o Destroier{RE}')

                elif escolherNavio == '2':
                    if submarino == 1:
                        usuarioPosicao(matriz10x10, escolherNavio)
                        submarino -= 1
                        naviosSobrando -= 1
                        print(f'{VERD}Submarino posicionado!{RE}')
                    else:
                        print(f'{NEG}{VERM}Voce ja posicionou o Submarino{RE}')

                elif escolherNavio == '3':
                    if contratorpedeiro == 1:
                        usuarioPosicao(matriz10x10, escolherNavio)
                        contratorpedeiro -= 1
                        naviosSobrando -= 1
                        print(f'{VERD}Contratorpedeiro posicionado!{RE}')
                    else:
                        print(f'{NEG}{VERM}Voce ja posicionou o Contratorpedeiro{RE}')

                elif escolherNavio == '4':
                    if navio_tanque == 1:
                        usuarioPosicao(matriz10x10, escolherNavio)
                        navio_tanque -= 1
                        naviosSobrando -= 1
                        print(f'{VERD}Navio-tanque posicionado!{RE}')
                    else:
                        print(f'{NEG}{VERM}Voce ja posicionou o Navio-tanque{RE}')

                elif escolherNavio == '5':
                    if porta_avioes == 1:
                        usuarioPosicao(matriz10x10, escolherNavio)
                        porta_avioes -= 1
                        naviosSobrando -= 1
                        print(f'{VERD}Porta-aviões posicionado!{RE}')
                    else:
                        print(f'{NEG}{VERM}Voce ja posicionou o Porta-aviões{RE}')

                else:
                    print(f'{VERM}Opção inválida! Escolha de 1 a 5.{RE}')
                    time.sleep(1)                                                                           
                    continue

            elif jogarInfo == '2':
                navioUI()
                mostrarRegras()
                voltaInicio = input(f'{AMA}Aperte ENTER para voltar a tela inicial\n> {RE}')
                if voltaInicio == '':
                    animacaoPalavra('Voltando')      
                    continue
            else:
                print(f'{VERM}Digite apenas opções entre 1 e 2{RE}')
                animacaoPalavra()                   
                continue
        
        # ADICIONADO: perguntar se quer jogar novamente
        if not jogarNovamente():
            print(f'{AMA}Obrigado por jogar! Até logo!{RE}')
            break

if __name__ == '__main__':
    main()
