import sys
import os
import time
import random

AZ   = "\033[34m"; VERD = "\033[32m"; VERM = "\033[31m"
CI   = "\033[36m"; AMA  = "\033[33m"; ROSA = "\033[35m"
NEG  = "\033[1m";  RE   = "\033[0m"
HIDE = "\033[?25l"; SHOW = "\033[?25h"
MOLDURA = AZ + NEG
TITULO  = AMA + NEG
TEXTO   = CI
NUMERO  = VERM + NEG
VALOR   = VERD + NEG

NAVIOS_INDICE = ['', 'destroier', 'submarino', 'contratorpedeiro', 'Navio-tanque', 'Porta-aviões']
#           0 ou mar       1             2               3               4               5

def verInformacao():
    print(f"""{CI}
    =============== BATALHA NAVAL ===============
    1. Tabuleiro 10x10 (linhas A-J, colunas 1-10).
    2. Posicione seus navios na horizontal ou vertical.
    3. Navios nao podem se sobrepor nem sair da grade.
    4. A cada turno voce atira em uma coordenada (ex: B5).
    5. Resposta: AGUA (errou) ou ACERTOU (atingiu).
    6. Um navio so AFUNDA quando todas as casas dele sao atingidas.
    7. Vence quem afundar toda a frota inimiga primeiro.
    ============================================= {RE}""")
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

def palavraAnimada(palavra='Voltando'):
    sys.stdout.write(HIDE + AMA)
    for _ in range(3):
        cleanTerm()
        print(palavra, end='', flush= True)
        for _ in range(3):
            print('.', end='',  flush= True)
            time.sleep(0.2)
    sys.stdout.write(SHOW + RE)

def jogarNovamente():
    while True:
        jogarSN = input('Deseja jogar novamente (s) para sim e (n) para não\n> ').strip().capitalize()
        if jogarSN in ['S','Sim']:
            return True
        elif jogarSN in ['N', 'Nao', 'Não']:
            return False
        continue

def voltarOpcao():
    while True:
        voltar = input('Deseja voltar? (z) para voltar e (ENTER) para continuar\n> ').strip().lower()
        if voltar == '':
            return None
        elif voltar == 'z':
            return False
        continue

def tabuleiroCPU():
    matrizInimiga = [[0 for _ in range(10)] for _ in range(10)]
    
    for tamanhoCasa in [1, 2, 3, 4, 5]:
        
        while True:
            casaOcupada = True
            
            randomLinha = random.randint(0, 9)
            randomColuna = random.randint(0, 9)
            randomPosicao = random.randint(0, 1) # 0 Vertical 1 Horizontal

            if randomPosicao == 0 and randomLinha + tamanhoCasa > 10:
                continue
            if randomPosicao == 1 and randomColuna + tamanhoCasa > 10:
                continue

            for sobreposicao in range(tamanhoCasa):
                if randomPosicao == 0:
                    if matrizInimiga[randomLinha + sobreposicao][randomColuna] != 0:
                        casaOcupada = False
                else:
                    if matrizInimiga[randomLinha][randomColuna + sobreposicao] != 0:
                        casaOcupada = False
            if not casaOcupada:
                continue

            for porCasa in range(tamanhoCasa):
                if randomPosicao == 0:
                    matrizInimiga[randomLinha + porCasa][randomColuna] == porCasa
                matrizInimiga[randomLinha][randomColuna + porCasa]
        
        break
    return matrizInimiga

def tabuleiroUsuario():
    matrizFinalUsuario = []
    for loopMa in range(10):
        matrizLinha = []
        for loopMe in range(10):
            matrizLinha.append(0)
        matrizFinalUsuario.append(matrizLinha)
    
    return matrizFinalUsuario

def mostrarTabuleroUsuario(matrizFinalUsuario):
    print(f'\n  ' + '   '.join([chr(65 + i) for i in range(10)]))
    print(f'  {AZ}╔' + '═' * 40 + f'{RE}')
    for numero, matriz in enumerate(matrizFinalUsuario):
        print(f'\n {numero}' + '║   ' + '   '.join(map(str, matriz)))

def porEmbarcacao(matrizFinalUsuario, escolheNavio):
    escolheNavioInt = int(escolheNavio)
    porIndice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    casaOcupada = True
   

    #parte em que vai mostrar em quanto a posição excede 

    while True:
        perguntaSentido = input('Digite (H) horizontal (V) vertical\n> ').strip().capitalize()
        if perguntaSentido in ['H', 'Horizontal']:
            valorPosi = 1
        elif perguntaSentido in ['V', 'Vertical']:
            valorPosi = 0
        else:
            print('Digite uma palara  valida')
            continue
    
    while True:
        perguntaLinha = input('Digite uma linha\n> ')
        perguntaColuna = input('Digite uma coluna\n> ')
                

        if not (perguntaColuna.isdigit() and perguntaLinha.isdigit()):
            print('Digite apenas numeros')
            continue

            
        perguntaLinhaInt = int(perguntaLinha)
        perguntaColunaInt = int(perguntaColuna)
            
        #subtração
        resultadoColuna = (perguntaColunaInt + escolheNavio) - 10  
        resultadoLinha = (perguntaLinhaInt + escolheNavio) - 10  
            
        if not (perguntaColuna in porIndice and perguntaLinha in porIndice):
            print('Digite apenas um numero de 0 a 9')
            continue
        
        if  opcao == 0 and perguntaColunaInt + escolheNavio > 10:
            print(f'O limite da coluna ira exceder em {resultadoColuna}')
            time.sleep(1.5)
            continue
        if  opcao == 1 and perguntaLinhaInt + escolheNavio > 10:
            print(f'O limite da linha ira exceder em {resultadoLinha}')
            time.sleep(1.5)
            continue
        
        for i in range(escolheNavio):
            if opcao == 1:
                matrizFinalUsuario[perguntaLinhaInt][perguntaColunaInt + i] != 0
                nome = NOMES[escolheNavio]
                print(f'O navio {nome} foi atingindo')
                casaOcupada = False
            
            matrizFinalUsuario[perguntaLinhaInt + i][perguntaColunaInt] != 0
            nome = NOMES[escolheNavio]
            print(f'O navio {nome} foi atingindo')
            casaOcupada = False
        
        if not casaOcupada:
            continue
            
        if opcao == 1:
            print(f'{VERD}Modo Horizontal escolhido{RE}')
            for k in range(escolheNavioInt):
                matrizFinalUsuario[perguntaLinhaInt + k] = casasNavio

        print(f'{VERD}Modo Vertical escolhido{RE}')
        for i in range(casasNavio):
            matriz10x10[porLinhaInt + i][porColunaInt] = casasNavio

    return True



# def main():





# if __name__ == __main__():
#     main()

















