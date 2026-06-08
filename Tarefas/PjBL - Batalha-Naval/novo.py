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
        else:
            print('Digite apenas as  opções validdas')
            continue                     
        
def voltarOpcao():
    while True:
        voltar = input('Deseja voltar? (z) para voltar e (ENTER) para continuar\n> ').strip().lower()
        if voltar == '':
            return None
        elif voltar == 'z':
            return False         
        else:
            print('Digite so coisa valida')

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
                    matrizInimiga[randomLinha + porCasa][randomColuna] = tamanhoCasa  
                else:
                    matrizInimiga[randomLinha][randomColuna + porCasa] = tamanhoCasa  
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
        break
         
    
    while True:
        casaOcupada = False
        perguntaLinha = input('Digite uma linha\n> ')
        perguntaColuna = input('Digite uma coluna\n> ')
                
        if not (perguntaColuna.isdigit() and perguntaLinha.isdigit()):
            print('Digite apenas numeros')
            continue
            
        perguntaLinhaInt = int(perguntaLinha)
        perguntaColunaInt = int(perguntaColuna)
            
        #subtração
        resultadoColuna = (perguntaColunaInt + escolheNavioInt) - 10   
        resultadoLinha = (perguntaLinhaInt + escolheNavioInt) - 10      
            
        if not (perguntaColunaInt in porIndice and perguntaLinhaInt in porIndice):  
            print('Digite apenas um numero de 0 a 9')
            continue
        
        if  valorPosi == 0 and perguntaLinhaInt + escolheNavioInt > 10:   
            print(f'O limite da coluna ira exceder em {resultadoColuna}')
            time.sleep(1.5)
            continue
        if  valorPosi == 1 and perguntaColunaInt + escolheNavioInt > 10:   
            print(f'O limite da linha ira exceder em {resultadoLinha}')
            time.sleep(1.5)
            continue
        

        for i in range(escolheNavioInt):       
            if valorPosi == 1:                   
                if matrizFinalUsuario[perguntaLinhaInt][perguntaColunaInt + i] != 0:
                    casaOcupada = True           
                if matrizFinalUsuario[perguntaLinhaInt + i][perguntaColunaInt] != 0:
                    casaOcupada = True           

        if casaOcupada:   
            continue
        
            
        if valorPosi == 1:                      
            print(f'{VERD}Modo Horizontal escolhido{RE}')
            for k in range(escolheNavioInt):
                matrizFinalUsuario[perguntaLinhaInt][perguntaColunaInt + k] = escolheNavioInt  
        else:
            print(f'{VERD}Modo Vertical escolhido{RE}')  
            for i in range(escolheNavioInt):         
                matrizFinalUsuario[perguntaLinhaInt + i][perguntaColunaInt] = escolheNavioInt   
        return True   

def barcoDestruido(matrizInimiga):
    for numero in [1, 2, 3, 4, 5]:
        for linha in matrizInimiga:
            if numero in linha:
                return False   
    return True 

def tiroUsuario(matrizInimiga, linha, coluna):
    tipoNavio = matrizInimiga[linha][coluna]
    if tipoNavio == 0:                       
        print('Voce acertou a agua')
        return None
    navioAcerto = NAVIOS_INDICE[tipoNavio]
    print(f'Voce acertou um navio {navioAcerto}')
    if not barcoDestruido(matrizInimiga):   
        print(f'{AMA}Há um pedaço restante do {navioAcerto}{RE}')
    else:
        print(f'{VERM}O {navioAcerto} foi totalmente destruido{RE}')
    
    matrizInimiga[linha][coluna] = 0        

def tiroCPU(matrizFinalUsuario):
    tiroRandomLinha = random.randint(0, 9)
    tiroRandomColuna = random.randint(0, 9)
    randomTiroNaMatrz = matrizFinalUsuario[tiroRandomLinha][tiroRandomColuna]
    if randomTiroNaMatrz == 0:
        print('O inimigo acerttou a agua')
    else:
        nome = NAVIOS_INDICE[randomTiroNaMatrz]
        print(f'O inimigo acertou {nome}')
        matrizFinalUsuario[tiroRandomLinha][tiroRandomColuna] = 0
    return matrizFinalUsuario





# def main():


# if __name__ == '__main__':     
#     main()



def faseDeCombate(matrizUsuario):
    #  criar a frota da CPU -> use tabuleiroCPU() e guarde numa variavel
    #          ex: matrizInimiga = tabuleiroCPU()
   
    #  abrir o loop principal -> while True:
    #          (tudo daqui pra baixo fica DENTRO do while)

        # : mostrar o tabuleiro do jogador (mostrarTabuleroUsuario)
        #          obs: se quiser, mostre tambem o que ja foi descoberto da CPU

        # pedir a linha do tiro (input) e a coluna do tiro (input)

        # validar o input (igual voce ja faz em porEmbarcacao):
        #          - se nao for digito -> print erro + continue
        #          - converter pra int
        #          - se nao estiver entre 0 e 9 -> print erro + continue

        # O JOGADOR ATIRA -> chame tiroUsuario(matrizInimiga, linha, coluna)

        #  CHECAR VITORIA (ANTES da CPU atirar!):
        #          - if barcoDestruido(matrizInimiga):
        #                print "VITORIA"
        #                break   (sai do loop)

        #  A CPU ATIRA -> matrizUsuario = tiroCPU(matrizUsuario)
        #          (guarde o retorno, igual fez no tiroUsuario)

        #  CHECAR DERROTA:
        #          - if barcoDestruido(matrizUsuario):
        #                print "DERROTA"
        #                break


