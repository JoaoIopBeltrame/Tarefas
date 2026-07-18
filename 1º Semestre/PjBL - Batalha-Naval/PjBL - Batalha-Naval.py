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
    {AZ}{NEG}        |   |{RE}
    {AZ}{NEG} _______|   |_______________________________________{RE}
    {AZ}{NEG}/  {RE}{TITULO}B A T A L H A   N A V A L  —  INSTRUCOES{AZ}{NEG}        \\{RE}
    {AZ}{NEG}|{RE}{AZ}  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ {AZ}{NEG}|{RE}
    {AZ}{NEG}|{RE}{TEXTO}  1. Tabuleiro 10x10  (linhas 0-9, colunas 0-9)   {AZ}{NEG}|{RE}
    {AZ}{NEG}|{RE}{TEXTO}  2. Posicione navios na horizontal ou vertical   {AZ}{NEG}|{RE}
    {AZ}{NEG}|{RE}{TEXTO}  3. Navios nao podem se sobrepor nem sair        {AZ}{NEG}|{RE}
    {AZ}{NEG}|{RE}{TEXTO}  4. A cada turno voce atira em uma coordenada    {AZ}{NEG}|{RE}
    {AZ}{NEG}|{RE}{TEXTO}  5. AGUA = errou  /  ACERTOU = atingiu           {AZ}{NEG}|{RE}
    {AZ}{NEG}|{RE}{TEXTO}  6. Navio afunda so quando todas as casas caem   {AZ}{NEG}|{RE}
    {AZ}{NEG}|{RE}{TEXTO}  7. Vence quem afundar toda a frota inimiga      {AZ}{NEG}|{RE}
    {AZ}{NEG}|{RE}{AZ}  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ {AZ}{NEG}|{RE}
    {AZ}{NEG}|  {RE}{TITULO}FROTA               TAMANHO     TIPO            {AZ}{NEG}|{RE}
    {AZ}{NEG}|{RE}{AZ}  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ {AZ}{NEG}|{RE}
    {AZ}{NEG}|{RE} {NUMERO}[1]{RE} {TEXTO}{"Destroier":<16} {VALOR}{"1 casa":<11} {TEXTO}{"Ataque Rapido":<16}{AZ}{NEG}|{RE}
    {AZ}{NEG}|{RE} {NUMERO}[2]{RE} {TEXTO}{"Submarino":<16} {VALOR}{"2 casas":<11} {TEXTO}{"Ataque Furtivo":<16}{AZ}{NEG}|{RE}
    {AZ}{NEG}|{RE} {NUMERO}[3]{RE} {TEXTO}{"Contratorpedeiro":<16} {VALOR}{"3 casas":<11} {TEXTO}{"Escolta Rapida":<16}{AZ}{NEG}|{RE}
    {AZ}{NEG}|{RE} {NUMERO}[4]{RE} {TEXTO}{"Navio-tanque":<16} {VALOR}{"4 casas":<11} {TEXTO}{"Carga Pesada":<16}{AZ}{NEG}|{RE}
    {AZ}{NEG}|{RE} {NUMERO}[5]{RE} {TEXTO}{"Porta-avioes":<16} {VALOR}{"5 casas":<11} {TEXTO}{"Unidade de Elite":<16}{AZ}{NEG}|{RE}
    {AZ}{NEG}\\__________________________________________________/{RE}
    {AZ}{NEG}  \\______________________________________________/{RE}
    {CI}    ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~{RE}''')

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
            elif valor == 'X':
                celulas.append(f'{VERM}{NEG}X{RE}')
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
    while True:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        acertou = tabuleiro_pessoa[linha][coluna]
        if acertou != 'X':
            break

    if acertou == 0:
        print(f'{AZ}>> O inimigo acertou a água{RE}')
    elif acertou in [1, 2, 3, 4, 5]:
        navio = NAVIOS_INDICE[acertou]
        tabuleiro_pessoa[linha][coluna] = 'X'
        print(f'{VERM}>> O inimigo acertou o seu {navio}!{RE}')

def tiro_player(tabuleiro_cpu, linha, coluna):
    acertou = tabuleiro_cpu[linha][coluna]
    if acertou == 'X':
        print(f'{AMA}>> Você já atirou nessa coordenada!{RE}')
        time.sleep(1.5)
        return False

    if acertou == 0:
        print(f'{AZ}>> Você acertou a água{RE}')
    else:
        navio = NAVIOS_INDICE[acertou]
        tabuleiro_cpu[linha][coluna] = 'X'
        print(f'{VERD}>> Você acertou o {navio}!{RE}')
        if verifica_navio_tabuleiro(tabuleiro_cpu):
            print(f'{AMA}   Ainda restam inimigos nesta frota.{RE}')
        else:
            print(f'{VERM}   O último {navio} foi totalmente destruído!{RE}')
    return True

def fase_de_combate(tabuleiro_pessoa, tabuleiro_cpu):
    limpar_tela()
    print(f'{VERM}{NEG}{"A tropa inimiga já posicionou suas tropas!":^50}{RE}')
    nome_pessoa = input('>> Digite o seu nome\n> ')
    time.sleep(1.5)

    modo_sonar = False

    while verifica_navio_tabuleiro(tabuleiro_pessoa) and verifica_navio_tabuleiro(tabuleiro_cpu):
        limpar_tela()

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
                continue
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

        if not (0 <= linha <= 9 and 0 <= coluna <= 9):
            print(f'{VERM}Coordenadas fora do limite! Escolha números entre 0 e 9.{RE}')
            time.sleep(1.5)
            continue

        if not tiro_player(tabuleiro_cpu, linha, coluna):
            continue

        if not verifica_navio_tabuleiro(tabuleiro_cpu):
            time.sleep(2)
            break

        tiro_inimigo(tabuleiro_pessoa)
        tabuleiro_limpo(tabuleiro_pessoa)
        time.sleep(2.5)

    limpar_tela()
    venceu = verifica_navio_tabuleiro(tabuleiro_pessoa)
    if venceu:
        print(f'''{VERD}{NEG}
    /==========================================\\
   /                                            \\
  <                V I T O R I A                  >
  <          FROTA INIMIGA DESTRUIDA              >
   \\                                            /
    \\==========================================/
          {CI}~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~{RE}''')
    else:
        print(f'''{VERM}{NEG}
    /==========================================\\
   /                                            \\
  <                D E R R O T A                 >
  <            SUA FROTA FOI AFUNDADA            >
   \\                                            /
    \\==========================================/
          {CI}~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~{RE}''')
    time.sleep(3)
    return venceu, nome_pessoa

def main():
    while True:
        limpar_tela()
        print(f'''
{AZ}{NEG}         /\\{RE}
{AZ}{NEG} _______/  \\_________________________{RE}
{AZ}{NEG}/  {RE}{TITULO}B A T A L H A   N A V A L{AZ}{NEG}         \\{RE}
{AZ}{NEG}\\____________________________________/{RE}
{AZ}{NEG}  \\________________________________/{RE}
{CI}     ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~{RE}

{AZ}{NEG}   /{RE}{NUMERO}  [1]{RE}{TEXTO}  Jogar                   {AZ}{NEG}\\{RE}
{AZ}{NEG}  /{RE}{NUMERO}   [2]{RE}{TEXTO}  Ver as regras           {AZ}{NEG} \\{RE}
{AZ}{NEG} /  {CI}~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  {AZ}\\{RE}
''')
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

            venceu, nome_pessoa = fase_de_combate(tabuleiro_pessoa, tabuleiro_cpu)

            # Dados reais da partida para o placar
            nome_pessoa = (nome_pessoa or 'Jogador')[:28]
            vencedor = nome_pessoa if venceu else 'Inimigo (CPU)'
            cor_v = VERD if venceu else VERM

            limpar_tela()
            print(f'''
{AMA}{NEG}  _______________________________________________
 /   P L A C A R   F I N A L                     \\
|  _____________________________________________  |
| /                                             \\ |{RE}
{AMA}{NEG}| |{RE} {CI}Jogador  :{RE} {TEXTO}{nome_pessoa:<28}{RE} {AMA}{NEG}| |{RE}
{AMA}{NEG}| |{RE} {CI}Inimigo  :{RE} {TEXTO}{"CPU":<28}{RE} {AMA}{NEG}| |{RE}
{AMA}{NEG}| |{RE} {CI}───────────────────────────────────────{RE} {AMA}{NEG}| |{RE}
{AMA}{NEG}| |{RE} {cor_v}{NEG}Vencedor :{RE} {cor_v}{NEG}{vencedor:<28}{RE} {AMA}{NEG}| |{RE}
{AMA}{NEG}| \\_____________________________________________/ |
 \\_______________________________________________/{RE}

{VERD}   Obrigado por jogar!{RE}
{CI}   Desenvolvido por:{RE}
{AZ}   Joao Beltrae{RE}
{VERD}   Caio Alvez{RE}
{AMA}   Gabriel Alasca{RE}''')
            time.sleep(2)

            if not jogar_novamente():
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
