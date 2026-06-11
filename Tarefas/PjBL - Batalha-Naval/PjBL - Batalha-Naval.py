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

# Global pros nomes
NAVIOS_INDICE = ['', 'Destroier', 'Submarino', 'Contratorpedeiro', 'Navio-tanque', 'Porta-aviões']

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def ver_info():
    print(f'''
    {MOLDURA}╔══════════════════════════════════════════════════════════╗{RE}
    {MOLDURA}║{TITULO}{"B A T A L H A   N A V A L":^58}{MOLDURA}║{RE}
    {MOLDURA}╠══════════════════════════════════════════════════════════╣{RE}
    {MOLDURA}║{TITULO}{" INSTRUÇÕES DE COMBATE":<58}{MOLDURA}║{RE}
    {MOLDURA}║{TEXTO}{"  1. Tabuleiro 10x10 (linhas 0-9, colunas 0-9)":<58}{MOLDURA}║{RE}
    {MOLDURA}║{TEXTO}{"  2. Posicione seus navios na horizontal ou vertical":<58}{MOLDURA}║{RE}
    {MOLDURA}║{TEXTO}{"  3. Navios não podem se sobrepor nem sair da grade":<58}{MOLDURA}║{RE}
    {MOLDURA}║{TEXTO}{"  4. A cada turno você atira em uma coordenada":<58}{MOLDURA}║{RE}
    {MOLDURA}║{TEXTO}{"  5. Resposta: ÁGUA (errou) ou ACERTOU (atingiu)":<58}{MOLDURA}║{RE}
    {MOLDURA}║{TEXTO}{"  6. Um navio só afunda quando todas as casas caem":<58}{MOLDURA}║{RE}
    {MOLDURA}║{TEXTO}{"  7. Vence quem afundar toda a frota inimiga primeiro":<58}{MOLDURA}║{RE}
    {MOLDURA}╠══════════════════════════════════════════════════════════╣{RE}
    {MOLDURA}║{TITULO}{" FROTA                TAMANHO     ESPECIFICAÇÃO":<58}{MOLDURA}║{RE}
    {MOLDURA}║{NUMERO} [1]{TEXTO} {"Destroier":<17}{VALOR}{"1 casa":<12}{TEXTO}{"Ataque Rápido":<24}{MOLDURA}║{RE}
    {MOLDURA}║{NUMERO} [2]{TEXTO} {"Submarino":<17}{VALOR}{"2 casas":<12}{TEXTO}{"Ataque Furtivo":<24}{MOLDURA}║{RE}
    {MOLDURA}║{NUMERO} [3]{TEXTO} {"Contratorpedeiro":<17}{VALOR}{"3 casas":<12}{TEXTO}{"Escolta Rápida":<24}{MOLDURA}║{RE}
    {MOLDURA}║{NUMERO} [4]{TEXTO} {"Navio-tanque":<17}{VALOR}{"4 casas":<12}{TEXTO}{"Carga Pesada":<24}{MOLDURA}║{RE}
    {MOLDURA}║{NUMERO} [5]{TEXTO} {"Porta-aviões":<17}{VALOR}{"5 casas":<12}{TEXTO}{"Unidade de Elite":<24}{MOLDURA}║{RE}
    {MOLDURA}╚══════════════════════════════════════════════════════════╝{RE}
    {AZ}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RE}''')

def palavra_animada(palavra='Voltando'):
    sys.stdout.write(HIDE + AMA)
    for _ in range(3):
        limpar_tela() 
        print(palavra, end='', flush=True)
        for _ in range(3):
            print('.', end='', flush=True)
            time.sleep(0.2)
    sys.stdout.write(SHOW + RE)

def opcao_voltar():
    while True:
        voltar = input(f'{CI}Deseja voltar? (z) para voltar e ENTER para continuar\n> {RE}').strip().capitalize()
        if voltar == 'Z':
            return False
        elif voltar == '':
            return True
        else:
            print(f'{VERM}Digite apenas uma das opções válidas{RE}') 
            time.sleep(1)

def jogar_novamente():
    while True:
        jogar = input(f'{CI}Gostaria de jogar de novo? (S) para sim (N) para não\n> {RE}').strip().capitalize()
        if jogar in ['S', 'Sim']:
            return True
        elif jogar in ['N', 'Não', 'Nao']:
            return False
        else:
            print(f'{VERM}Digite apenas uma das opções válidas{RE}') 
            time.sleep(1)

def tabuleiro_player():
    return [[0] * 10 for _ in range(10)]

def tabuleiro_limpo(tabuleiro):
    print(f'\n      {NEG}{CI}' + '   '.join(str(i) for i in range(10)) + f'{RE}')
    print(f'    {AZ}╔' + '═' * 39 + f'╗{RE}')
    for numero, linha in enumerate(tabuleiro):
        celulas = []
        for valor in linha:
            if valor == 0:
                celulas.append(f'{AZ}~{RE}')
            else:
                celulas.append(f'{VERD}{NEG}{valor}{RE}')
        print(f'  {NEG}{numero}{RE} {AZ}║{RE} ' + '   '.join(celulas) + f' {AZ}║{RE}')
    print(f'    {AZ}╚' + '═' * 39 + f'╝{RE}')

def tabuleiro_inimigo():
    tabuleiro = [[0] * 10 for _ in range(10)]

    for navio in [1, 2, 3, 4, 5]:
        while True:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            sentido = random.randint(0, 1)

            if sentido == 0 and coluna + navio > 10:
                continue
            if sentido == 1 and linha + navio > 10:
                continue

            casas = [(linha, column + i) if sentido == 0 else (linha + i, coluna) for i in range(navio)]

            # Correção rápida de digitação de variável interna: column -> coluna
            casas = [(linha, coluna + i) if sentido == 0 else (linha + i, coluna) for i in range(navio)]

            lugarOcupado = False
            for lin, col in casas:
                if tabuleiro[lin][col] != 0:
                    lugarOcupado = True
                    break
            if lugarOcupado:
                continue

            for lin, col in casas:
                tabuleiro[lin][col] = navio
            break

    return tabuleiro

def verifica_navio_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        for valor in linha:
            if valor in [1, 2, 3, 4, 5]:
                return True
    return False

def por_navio(tabuleiro_pessoa, navio):
    navio_INT = int(navio)

    while True:
        posicao = input(f'{CI}Selecione (H) para horizontal e (V) para vertical\n> {RE}').strip().capitalize()
        if posicao in ['H', 'Horizontal']:
            valor = 0
        elif posicao in ['V', 'Vertical']:
            valor = 1
        else:
            print(f'{VERM}Digite apenas as opções válidas{RE}') 
            continue
        break

    while True:
        try:
            linha = int(input(f'{CI}Digite uma linha (0-9)\n> {RE}'))
            coluna = int(input(f'{CI}Digite uma coluna (0-9)\n> {RE}'))
        except ValueError:
            print(f'{VERM}Digite apenas números inteiros{RE}')
            continue

        if not (0 <= linha <= 9 and 0 <= coluna <= 9):
            print(f'{VERM}Digite apenas números dentro do limite (0-9){RE}')
            continue

        if (valor == 0 and coluna + navio_INT > 10) or (valor == 1 and linha + navio_INT > 10):
            print(f'{VERM}O navio ultrapassa o limite do tabuleiro{RE}')
            continue

        coordenadas = [(linha, coluna + c) if valor == 0 else (linha + c, coluna) for c in range(navio_INT)]

        lugarOcupado = False
        for lin, col in coordenadas:
            if tabuleiro_pessoa[lin][col] != 0:
                lugarOcupado = True
                break
        if lugarOcupado:
            print(f'{VERM}Neste local já existe um navio{RE}')
            continue

        direcao = 'Horizontal' if valor == 0 else 'Vertical'
        print(f'{VERD}Modo {direcao} aplicado com sucesso!{RE}')
        time.sleep(0.8)

        for lin, col in coordenadas:
            tabuleiro_pessoa[lin][col] = navio_INT
        break

def tiro_inimigo(tabuleiro_pessoa):
    linha = random.randint(0, 9)
    coluna = random.randint(0, 9)
    acertou = tabuleiro_pessoa[linha][coluna]

    if acertou == 0:
        print(f'{AZ}>> O inimigo acertou a água{RE}') 
    else:
        navio = NAVIOS_INDICE[acertou]
        tabuleiro_pessoa[linha][coluna] = 0
        print(f'{VERM}>> O inimigo acertou o seu {navio}!{RE}') 

def tiro_player(tabuleiro_inimigo, linha, coluna):
    acertou = tabuleiro_inimigo[linha][coluna]
    if acertou == 0:
        print(f'{AZ}>> Você acertou a água{RE}') 
    else:
        navio = NAVIOS_INDICE[acertou]
        tabuleiro_inimigo[linha][coluna] = 0
        print(f'{VERD}>> Você acertou o {navio}!{RE}') 
        if verifica_navio_tabuleiro(tabuleiro_inimigo):
            print(f'{AMA}   Ainda restam inimigos nesta frota.{RE}')
        else:
            print(f'{VERM}   O último {navio} foi totalmente destruído!{RE}')

def fase_de_combate(tabuleiro_pessoa, tabuleiro_cpu):
    limpar_tela() 
    print(f'{VERM}{NEG}{"A tropa inimiga já posicionou suas tropas!":^50}{RE}')
    time.sleep(1.5) 

    modo_sonar = False

    while verifica_navio_tabuleiro(tabuleiro_pessoa) and verifica_navio_tabuleiro(tabuleiro_cpu):
        limpar_tela() 
        
        # Verifica se o jogador já ativou o sonar neste jogo
        if not modo_sonar:
            print(f'\n{MOLDURA}{"═"*20}[ {TITULO}SEU TURNO{MOLDURA} ]{"═"*20}{RE}') 
            print(f'{TITULO}SEU TABULEIRO:{RE}') 
            tabuleiro_limpo(tabuleiro_pessoa)

            atirar = input(f'{CI}Digite o código secreto ou ENTER para continuar\n> {RE}').strip().lower()
            if atirar == 'ccbbededba':
                print(f'{ROSA}Código secreto ativado{RE}')
                palavra_animada('Usando sonar')
                palavra_animada('Avaliando tropas inimigas')
                modo_sonar = True
                continue # Recomeça o loop já no modo sonar
        else:
            print(f'\n{ROSA}{NEG}{"═"*18}[ MODO SONAR ]{"═"*18}{RE}') 
            print(f'{TITULO}SEU TABULEIRO:{RE}') 
            tabuleiro_limpo(tabuleiro_pessoa)
            print(f'{ROSA}TABULEIRO INIMIGO (sonar):{RE}') 
            tabuleiro_limpo(tabuleiro_cpu)
            
        try:
            linha = int(input(f'{CI}Digite a linha em que você quer atirar (0 - 9)\n> {RE}').strip())
            coluna = int(input(f'{CI}Digite a coluna em que você quer atirar (0 - 9)\n> {RE}').strip())
        except ValueError:
            print(f'{VERM}Digite apenas números inteiros{RE}')
            time.sleep(1)
            palavra_animada()
            continue
            
        # Adicionado validação de limites para evitar IndexError
        if not (0 <= linha <= 9 and 0 <= coluna <= 9):
            print(f'{VERM}Coordenadas fora do limite! Escolha números entre 0 e 9.{RE}')
            time.sleep(1.5)
            continue

        tiro_player(tabuleiro_cpu, linha, coluna)
        tiro_inimigo(tabuleiro_pessoa)
        time.sleep(2.5)

    # Lógica de fim de jogo
    limpar_tela()
    if verifica_navio_tabuleiro(tabuleiro_pessoa):
        print(f'''{VERD}{NEG}
╔═════════════════════════════════════════╗
║{"VITÓRIA! VOCÊ AFUNDOU A FROTA INIMIGA":^41}║
╚═════════════════════════════════════════╝{RE}''')
    else:
        print(f'''{VERM}{NEG}
╔═════════════════════════════════════════╗
║{"DERROTA! SUA FROTA FOI AFUNDADA":^41}║
╚═════════════════════════════════════════╝{RE}''')
    time.sleep(3) 

def main():
    while True:
        limpar_tela() 
        print(f'''
{MOLDURA}╔══════════════════════════════════════╗
║{TITULO}{"BATALHA NAVAL":^38}{MOLDURA}║
╠══════════════════════════════════════╣
║{NUMERO}{" [1]":<5}{TEXTO}{"Jogar":<33}{MOLDURA}║
║{NUMERO}{" [2]":<5}{TEXTO}{"Ver as regras":<33}{MOLDURA}║
╚══════════════════════════════════════╝{RE}''')
        opcao = input(f'{CI}> {RE}').strip()

        if opcao == '1':
            tabuleiro_pessoa = tabuleiro_player()
            tabuleiro_cpu = tabuleiro_inimigo()
            navios = [1, 2, 3, 4, 5]
            
            for navio in navios:
                restantes = navios[navios.index(navio):]
                limpar_tela() 
                print(f'\n{MOLDURA}{"═"*15}[ {TITULO}POSICIONAMENTO{MOLDURA} ]{"═"*15}{RE}') 
                tabuleiro_limpo(tabuleiro_pessoa)
                print(f'\n{ROSA}{NEG}NAVIOS RESTANTES:{RE}')
                
                for n in restantes:
                    print(f'  {NUMERO}[{n}]{TEXTO} {NAVIOS_INDICE[n]}{RE}')
                    
                print(f'\n{AMA}Posicione o navio de tamanho {navio} — {NAVIOS_INDICE[navio]}{RE}')
                por_navio(tabuleiro_pessoa, navio)

            fase_de_combate(tabuleiro_pessoa, tabuleiro_cpu)

            if not jogar_novamente():
                print(f'{VERD}Obrigado por jogar!{RE}')
                break

        elif opcao == '2':
            limpar_tela() 
            ver_info()
            opcao_voltar()

        else:
            print(f'{VERM}Digite apenas 1 ou 2{RE}')
            time.sleep(1)

if __name__ == '__main__':
    main()

