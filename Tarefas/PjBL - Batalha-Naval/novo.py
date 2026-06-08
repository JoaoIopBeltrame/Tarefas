import os, sys, time, random

# Cores e Estilos ANSI
AZ   = "\033[34m"; VERD = "\033[32m"; VERM = "\033[31m"
CI   = "\033[36m"; AMA  = "\033[33m"; ROSA = "\033[35m"
NEG  = "\033[1m";  RE   = "\033[0m"
HIDE = "\033[?25l"; SHOW = "\033[?25h"

# Temas do Sistema
MOLDURA = AZ + NEG
TITULO  = AMA + NEG
TEXTO   = CI
NUMERO  = VERM + NEG
VALOR   = VERD + NEG

#Global pros nomes
NAVIOS_INDICE = ['', 'destroier', 'submarino', 'contratorpedeiro', 'Navio-tanque', 'Porta-aviões']
#               0 ou mar       1             2             3               4               5
def verInformacao():
    print(f"""
    {MOLDURA}                      _________[{TITULO}⚓ BATALHA NAVAL{MOLDURA}]_________
                        /                                  \\
                        /       {TITULO}INSTRUÇÕES DE COMBATE{MOLDURA}        \\
                    /                                      \\
    ___________     /  {TEXTO}1. Tabuleiro 10x10 (A-J, colunas 1-10){MOLDURA}  \\
    [___________]___/   {TEXTO}2. Posicione na horizontal/vertical. {MOLDURA}   \\
    \\                  {TEXTO}3. Não pode se sobrepor ou sair.     {MOLDURA}    \\
    \\                 {TEXTO}4. Atire via coordenada (ex: B5).    {MOLDURA}     \\
        \\                {TEXTO}5. Resposta: {VALOR}ÁGUA{TEXTO} ou {VERM}ACERTOU{TEXTO}.         {MOLDURA}      \\
        \\               {TEXTO}6. Só afunda se atingir todo o navio.{MOLDURA}       \\
    ______\\_____________ {TEXTO}7. Vence quem derrubar a frota 1º.   {MOLDURA}________\\_______
    \\                                                                         /
    \\   {TITULO}🪖 FROTAS DISPONÍVEIS{MOLDURA}          {TITULO}📐 TAMANHO{MOLDURA}        {TITULO}⚙️ ESPECIFICAÇÕES{MOLDURA}       /
    \\                                                                     /
    \\  {NUMERO}[1]{TEXTO} Porta-aviões                {VALOR}5 Casas{TEXTO}        Unidade de Elite       /
        \\ {NUMERO}[2]{TEXTO} Navio-tanque                {VALOR}4 Casas{TEXTO}        Carga Pesada          /
        \\{NUMERO}[3]{TEXTO} Contratorpedeiro            {VALOR}3 Casas{TEXTO}        Escolta Rápida       /
        \\{NUMERO}[4]{TEXTO} Submarino                   {VALOR}2 Casas{TEXTO}        Ataque Furtivo      /
        \\{NUMERO}[5]{TEXTO} Destroier                   {VALOR}1 Casa{TEXTO}         Ataque Rápido      /
            \\_____________________________________________________________/
    {AZ}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RE}""")

def palavraAnimada(palavra='Voltando'):
    sys.stdout.write(HIDE + AMA)
    for _ in range(3):
        os.system('cls' if os.name == 'nt' else 'clear') 
        print(palavra, end='', flush= True)
        for _ in range(3):
            print('.', end='',  flush= True)
            time.sleep(0.2)
    sys.stdout.write(SHOW + RE)

def opcaoVoltar():
    while True:
        voltar = input('Deseja voltar (z) para nao e ENTER para continuar\n> ').strip().capitalize()
        if voltar == 'z':
            return False
        elif voltar == '':
            return True
        else:
            print('Voce so inferiu uma das ergras')
            time.sleep(1)
            continue

def jogarNovamente():
    while True:
        jogar = input('Gostaria de jogar de novo? (S) para sim (N) para não\n> ').strip().capitalize()
        if jogar in ['S', 'Sim']:
            return True
        elif jogar in ['N', 'Não', 'Nao']:
            return False
        else:
            print('Voce so inferiu uma das ergras')
            time.sleep(1)
            continue

def criaTabuleiroPlayer():
    tabuleiroPlayer = [[0] * 10 for _ in range(10)]
    
    return tabuleiroPlayer

def mostrarTabulero(tabuleiroLimpo):
    print(f'\n  ' + '   '.join([chr(65 + i) for i in range(10)]))  
    print(f'  {AZ}╔' + '═' * 40 + f'{RE}')
    for numero, matriz in enumerate(tabuleiroLimpo):
        print(f'\n {numero}' + '║   ' + '   '.join(map(str, matriz)))

def criaTabuleiroCPU():
    matrizInimiga = [[0 for _ in range(10)] for _ in range(10)]

    for tamanhoBarco in [1, 2, 3, 4, 5]:
        while True:
            lugarOcupado = False

            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            sentido = random.randint(0, 1) #0 horizontal 1 vertical

            if sentido == 0 and coluna + tamanhoBarco > 10:
                continue
            if sentido == 1 and linha + tamanhoBarco > 10:
                continue

            for casa in range(tamanhoBarco):
                if sentido == 0:
                    if matrizInimiga[linha][coluna + casa] != 0:
                        lugarOcupado = True
                else:
                    if matrizInimiga[linha + casa][coluna] != 0:
                        lugarOcupado = True
            if lugarOcupado:
                continue
            
            if sentido == 0:
                for porColuna in range(tamanhoBarco):
                    matrizInimiga[linha][coluna + porColuna] = tamanhoBarco
            else:
                for porLinha in range(tamanhoBarco):
                    matrizInimiga[linha + porLinha][coluna] = tamanhoBarco
            break
    return matrizInimiga
    
def aindaTemNaio(tabuleiro):
    for num in [1, 2, 3, 4, 5]:
        for indice in tabuleiro:
            if num in tabuleiro:
                return False
    return True

def porNavio(tabuleiroUsuario, escolheNavio):
    escolheNavio_INT = int(escolheNavio)
    indicePermitido = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        posicao = input('Selecione (H) para horizontal e (V) para vertical\n> ').strip().capitalize()
        if posicao in ['H', 'Horizontal']:
            valorPosicao = 0
        elif posicao in ['V', 'Vertical']:
            valorPosicao = 1
        else: 
            print('Digita so as opcaoes validas')
            continue
        break

    while True:
        lugarOcupado = False
        try:
            linha = int(input('Digite uma linha (0, 9)\n> '))
            coluna = int(input('Digite uma linha (0, 9)\n> '))
        except ValueError:
            print('Digite apenas numeros inteiros')
            continue
        
        if not (0 <= linha <= 9 and 0 <= coluna <= 9):
            print('Digite apenas numeros dentro do limite')
            continue

        if valorPosicao == 0 and coluna + escolheNavio_INT > 10:
            print(f'O limite da LINHA será excedido em {(coluna + escolheNavioInt) - 10} casas.')
            continue
        if valorPosicao == 1 and linha + escolheNavio_INT > 10:
            print(f'O limite da LINHA será excedido em {(linha + escolheNavioInt) - 10} casas.')
            continue
        
        for num in range(escolheNavio_INT):
            if valorPosicao == 0 and tabuleiroUsuario[linha][coluna + num]!= 0:
                lugarOcupado = True
            else:
                if tabuleiroUsuario[linha + num][coluna] != 0:
                    lugarOcupado = True
        
        if lugarOcupado:
            continue
        
        modo = 'Horzontal' if valorPosicao == 0 else 'Vertical'
        print(f'{VERD}Modo {modo} aplicado com sucesso!{RE}')

        for posicao in range(escolheNavio_INT):
            if valorPosicao == 0:
                tabuleiroUsuario[linha][coluna + valorPosicao] = escolheNavio_INT
            else:
                tabuleiroUsuario[linha + valorPosicao][coluna] = escolheNavio_INT
    
    return True
    
    #fazer tratamento de coisas em ambos









