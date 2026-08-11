import os, sys, time, random

AZ   = "\033[34m"; VERD = "\033[32m"; VERM = "\033[31m"
CI   = "\033[36m"; AMA  = "\033[33m"; ROSA = "\033[35m"
NEG  = "\033[1m";  RE   = "\033[0m"
HIDE = "\033[?25l"; SHOW = "\033[?25h"

modo_jogo = True
while modo_jogo:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
                        ,~-.                            
                       (  ) )_                          
                      ( ` ')  )                  ,~-.   {AZ}
               .--..-{RE}(_(_.~~~'{AZ}..--..--..--..-- {RE} (  ) )_ {AZ}
              / .. \.. \.. \.. \.. \.. \.. \.. {RE}( ` ')  ){AZ}
              \ \/\ `'\ `'\ `'\ `'\ `'\ `'\ `'{RE}(_(_.~~~' {AZ}
               \/ /`--'`--'`--'`--'`--'`--'`--'\/ /     
               / /\                            / /\     
              / /\ \  {VERM}pedra{RE} x {AMA}papel{RE} x {VERD}tesoura{RE} {AZ}/ /\ \    
              \ \/ /         o jogo           \ \/ /    
               \/ /                            \/ /     
               / /\.--..--..--..--..--..--..--./ /\     {RE}
   ,~-.  {AZ}     / /\ \.. \.. \.. \.. \.. \.. \.. \/\ \ {RE}   
  (  ) )_  {AZ}   \ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /  {RE}  
 ( ` ')  )  {AZ}   `--'`--'`--'`--'`--'`--'`--'`--'`--'   {RE}  
(_(_.~~~'                                               
      
      {NEG}{VERD}[0]{RE} {AZ}JOGADOR{RE} {AMA}VS{RE} {VERM}JOGADOR{RE}
      {NEG}{VERD}[1]{RE} {AZ}JOGADOR{RE} {AMA}VS{RE} {ROSA}COMPUTADOR{RE}
      {NEG}{VERD}[2]{RE} {ROSA}COMPUTADOR{RE} {AMA}VS{RE} {ROSA}COMPUTADOR{RE}''')

    entrada = input(f'{VERD}\n{NEG}> {RE}').strip().upper()

    if entrada != '0' and entrada != '1' and entrada != '2':
        print(f'{NEG}{VERM}Opção inválida{RE}')
        sys.stdout.write(HIDE)
        for ciclo in range(2):
            for i in range(1, 4):
                pontos = '.' * i
                sys.stdout.write(f'\r{AMA}{NEG}Reiniciando{pontos:<3}{RE}')
                sys.stdout.flush()
                time.sleep(0.2)
        sys.stdout.write(SHOW) 
        print() 
    modo_jogo = False

#MODO 0: JOGADOR VS JOGADOR
if entrada == '0':
    print(f"""
            {CI}╔══════════════════════════════════╗
            {CI}║  {AMA}{'MODO DE JOGO'.center(32)}{CI}║
            {CI}╠══════════════════════════════════╣
            {CI}║         {NEG}{AZ}JOGADOR{RE} {CI}VS{RE} {VERM}JOGADOR{RE}{CI}       ║
            {CI}╚══════════════════════════════════╝{RE}""")

    jogador1 = True
    while jogador1:
        os.system('cls' if os.name == 'nt' else 'clear')
        jogado_1 = input(f'\n{NEG}{AZ}Nome do Jogador 1{RE}\n{AMA}>{RE} ').capitalize().strip()
        if jogado_1 == '':
            print(f'{NEG}{VERM}Voce deve digitar um nome{RE}')
            time.sleep(1)
            sys.stdout.write(HIDE)
            for ciclo in range(2):
                for i in range(1, 4):
                    pontos = '.' * i
                    sys.stdout.write(f'\r{AMA}{NEG}Reiniciando{pontos:<3}{RE}')
                    sys.stdout.flush()
                    time.sleep(0.2)
            sys.stdout.write(SHOW)
            continue
        jogador1 = False

    jogador2 = True
    while jogador2:
        os.system('cls' if os.name == 'nt' else 'clear')
        jogado_2 = input(f'\n{NEG}{VERM}Nome do Jogador 2{RE}\n{AMA}>{RE} ').capitalize().strip()
        if jogado_2 == '':
            print(f'{NEG}{VERM}Voce deve digitar um nome{RE}')
            time.sleep(1)
            sys.stdout.write(HIDE)
            for ciclo in range(2):
                for i in range(1, 4):
                    pontos = '.' * i
                    sys.stdout.write(f'\r{AMA}{NEG}Reiniciando{pontos:<3}{RE}')
                    sys.stdout.flush()
                    time.sleep(0.2)
            sys.stdout.write(SHOW)
            continue
        elif jogado_2 == jogado_1:
            print(f'{NEG}{VERM}Voce deve digitar um nome que ainda não foi usado{RE}')
            time.sleep(1)
            sys.stdout.write(HIDE)
            for ciclo in range(2):
                for i in range(1, 4):
                    pontos = '.' * i
                    sys.stdout.write(f'\r{AMA}{NEG}Reiniciando{pontos:<3}{RE}')
                    sys.stdout.flush()
                    time.sleep(0.2)
            sys.stdout.write(SHOW)
            continue
        jogador2 = False

    ponto_jogador1 = 0
    ponto_jogador2 = 0

    rodando = True
    while rodando:
        escolha1 = True
        while escolha1:
            os.system('cls' if os.name == 'nt' else 'clear')
            entrada1 = input(f'{NEG}{AZ}|{jogado_1}|{RE} {CI}deve escolher entre:{RE} {VERM}PEDRA{RE} {CI}ou{RE} {AMA}PAPEL{RE} {CI}ou{RE} {VERD}TESOURA{RE}\n{AMA}>{RE} ').lower().strip()
            if entrada1 != 'pedra' and entrada1 != 'papel' and entrada1 != 'tesoura':
                print(f'{NEG}{VERM}Você deve escolher entre:{RE} {VERM}PEDRA{RE} {CI}ou{RE} {AMA}PAPEL{RE} {CI}ou{RE} {VERD}TESOURA{RE}')
                time.sleep(1.5)
                sys.stdout.write(HIDE)
                for ciclo in range(2):
                    for i in range(1, 4):
                        pontos = '.' * i
                        sys.stdout.write(f'\r{AMA}{NEG}Reiniciando{pontos:<3}{RE}')
                        sys.stdout.flush()
                        time.sleep(0.2)
                sys.stdout.write(SHOW)
                continue
            print(f'{NEG}{VERD}✔ JOGADA VALIDA{RE}')
            time.sleep(1.2)
            escolha1 = False

        escolha2 = True
        while escolha2:
            os.system('cls' if os.name == 'nt' else 'clear')
            entrada2 = input(f'{NEG}{VERM}|{jogado_2}|{RE} {CI}deve escolher entre:{RE} {VERM}PEDRA{RE} {CI}ou{RE} {AMA}PAPEL{RE} {CI}ou{RE} {VERD}TESOURA{RE}\n{AMA}>{RE} ').lower().strip()
            if entrada2 != 'pedra' and entrada2 != 'papel' and entrada2 != 'tesoura':
                print(f'{NEG}{VERM}Você deve escolher entre:{RE} {VERM}PEDRA{RE} {CI}ou{RE} {AMA}PAPEL{RE} {CI}ou{RE} {VERD}TESOURA{RE}')
                time.sleep(1.5)
                sys.stdout.write(HIDE)
                for ciclo in range(2):
                    for i in range(1, 4):
                        pontos = '.' * i
                        sys.stdout.write(f'\r{AMA}{NEG}Reiniciando{pontos:<3}{RE}')
                        sys.stdout.flush()
                        time.sleep(0.2)
                sys.stdout.write(SHOW)
                continue
            print(f'{NEG}{VERD}✔ JOGADA VALIDA{RE}')
            time.sleep(1.2)
            escolha2 = False

        os.system('cls' if os.name == 'nt' else 'clear')

        if entrada1 == entrada2:
            print(f'''
            ,~-.                                        ,~-.
            (  ) )_   {AMA}~  ~  ~  ~  ~  ~  ~  ~  ~  ~{RE}   (  ) )_
            ( ` ')  )  {AMA}.--..--..--..--..--..--..--.{RE}   ( ` ')  )
            (_(_.~~~'{AMA}  / .. \.. \.. \.. \.. \.. \.. \  {RE}(_(_.~~~'
                    {AMA}   \ `'\ `'\ `'\ `'\ `'\ `'\ `'\ {RE}
                    {AMA}    `--'`--'`--'`--'`--'`--'`--' {RE}
                                                    
                    {ROSA}    ,~-.  {VERM}{NEG}E M P A T E !{RE}{ROSA}  ,~-.
                    {ROSA}   (  ) )_  {CI}ninguem venceu{RE}{ROSA}  (  ) )_
                    {ROSA}  ( ` ')  )  ~ ~ ~ ~ ~ ~ ~  ( ` ')  )
                    {ROSA} (_(_.~~~'..--..--..--..-.. (_(_.~~~'
                    {ROSA}          \.. \.. \.. \.. \ 
                    {ROSA}           \`'\ `'\ `'\ `'\  
                    {ROSA}            `--'`--'`--'`--' {RE}''')
            ponto_jogador1 += 1
            ponto_jogador2 += 1
        elif (entrada1 == 'pedra'   and entrada2 == 'tesoura') or \
             (entrada1 == 'papel'   and entrada2 == 'pedra')   or \
             (entrada1 == 'tesoura' and entrada2 == 'papel'):
            print(f'\n  {AMA}{entrada1}{RE} vence {VERM}{entrada2}{RE}')
            print(f'{NEG}{VERD}  {jogado_1.upper()} VENCEU!{RE}')
            ponto_jogador1 += 1
        else:
            print(f'\n{AMA}{entrada2}{RE} vence {VERM}{entrada1}{RE}')
            print(f'{NEG}{VERD}{jogado_2.upper()} VENCEU!{RE}')
            ponto_jogador2 += 1

        print(f'\n  {AZ}{jogado_1}{RE}: {ponto_jogador1} pt(s)  |  {VERM}{jogado_2}{RE}: {ponto_jogador2} pt(s)')

        jogar_novamente_flag = True
        while jogar_novamente_flag:
            print(f'\n{CI}  [{VERD}CONTINUAR{CI}]{RE} ou {CI}[{VERM}SAIR{CI}]{RE}')
            continuar = input(f'{AMA}> {RE}').strip().lower()
            if continuar == 'continuar':
                sys.stdout.write(HIDE)
                for ciclo in range(2):
                    for i in range(1, 4):
                        pontos = '.' * i
                        sys.stdout.write(f'\r{AZ}{NEG}Reiniciando{pontos:<3}{RE}')
                        sys.stdout.flush()
                        time.sleep(0.2)
                sys.stdout.write(SHOW)
                jogar_novamente_flag = False
            elif continuar == 'sair':
                os.system('cls' if os.name == 'nt' else 'clear')
                if ponto_jogador1 > ponto_jogador2:
                    ven, cor_v = jogado_1, AZ
                elif ponto_jogador2 > ponto_jogador1:
                    ven, cor_v = jogado_2, VERM
                else:
                    ven, cor_v = 'EMPATE', AMA
                titulo = 'PLACAR FINAL'.center(32)
                l1 = f'{jogado_1}: {ponto_jogador1} pt(s)'
                l2 = f'{jogado_2}: {ponto_jogador2} pt(s)'
                lv = f'Vencedor: {ven}'
                pad1 = ' ' * (32 - len(l1))
                pad2 = ' ' * (32 - len(l2))
                padv = ' ' * (32 - len(lv))
                print(f"""
{CI}╔══════════════════════════════════╗
║  {AMA}{titulo}{CI}║
╠══════════════════════════════════╣
║  {AZ}{jogado_1}{CI}: {AMA}{ponto_jogador1} pt(s){CI}{pad1}║
║  {VERM}{jogado_2}{CI}: {AMA}{ponto_jogador2} pt(s){CI}{pad2}║
╠══════════════════════════════════╣
║  Vencedor: {cor_v}{ven}{CI}{padv}║
╚══════════════════════════════════╝{RE}
{VERD}  Obrigado por jogar!{RE}
{CI}  Desenvolvido por:{RE}
{AZ}  Joao Beltrae{RE}
{VERD}  Caio Alvez{RE}
{AMA}  Gabriel Alasca{RE}""")
                jogar_novamente_flag = False
                rodando = False
            else:
                print(f'{NEG}{VERM}  Digite CONTINUAR ou SAIR{RE}')

#MODO 1: JOGADOR VS COMPUTADOR
elif entrada == '1':
    print(f"""
            {CI}╔══════════════════════════════════╗
            {CI}║  {AMA}{'MODO DE JOGO'.center(32)}{CI}║
            {CI}╠══════════════════════════════════╣
            {CI}║       {NEG}{AZ}JOGADOR{RE} {CI}VS{RE} {ROSA}COMPUTADOR{RE}{CI}        ║
            {CI}╚══════════════════════════════════╝{RE}""")

    jogador1 = True
    while jogador1:
        os.system('cls' if os.name == 'nt' else 'clear')
        jogado_1 = input(f'\n{NEG}{AZ}Seu nome{RE}\n{AMA}>{RE} ').capitalize().strip()
        if jogado_1 == '':
            print(f'{NEG}{VERM}Voce deve digitar um nome{RE}')
            time.sleep(1)
            sys.stdout.write(HIDE)
            for ciclo in range(2):
                for i in range(1, 4):
                    pontos = '.' * i
                    sys.stdout.write(f'\r{AMA}{NEG}Reiniciando{pontos:<3}{RE}')
                    sys.stdout.flush()
                    time.sleep(0.2)
            sys.stdout.write(SHOW)
            continue
        jogador1 = False

    ponto_jogador1 = 0
    ponto_ia = 0

    rodando = True
    while rodando:
        escolha1 = True
        while escolha1:
            os.system('cls' if os.name == 'nt' else 'clear')
            entrada1 = input(f'{NEG}{AZ}|{jogado_1}|{RE} {CI}deve escolher entre:{RE} {VERM}PEDRA{RE} {CI}ou{RE} {AMA}PAPEL{RE} {CI}ou{RE} {VERD}TESOURA{RE}\n{AMA}>{RE} ').lower().strip()
            if entrada1 != 'pedra' and entrada1 != 'papel' and entrada1 != 'tesoura':
                print(f'{NEG}{VERM}Você deve escolher entre:{RE} {VERM}PEDRA{RE} {CI}ou{RE} {AMA}PAPEL{RE} {CI}ou{RE} {VERD}TESOURA{RE}')
                time.sleep(1.5)
                sys.stdout.write(HIDE)
                for ciclo in range(2):
                    for i in range(1, 4):
                        pontos = '.' * i
                        sys.stdout.write(f'\r{AMA}{NEG}Reiniciando{pontos:<3}{RE}')
                        sys.stdout.flush()
                        time.sleep(0.2)
                sys.stdout.write(SHOW)
                continue
            print(f'{NEG}{VERD}✔ JOGADA VALIDA{RE}')
            time.sleep(1.2)
            escolha1 = False

        n = random.randint(0, 2)
        if n == 0:
            entrada_ia = 'pedra'
        elif n == 1:
            entrada_ia = 'papel'
        else:
            entrada_ia = 'tesoura'

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\n  {ROSA}Computador escolheu: {NEG}{entrada_ia}{RE}')
        time.sleep(0.8)

        if entrada1 == entrada_ia:
            print(f'''
            ,~-.                                        ,~-.
            (  ) )_   {AMA}~  ~  ~  ~  ~  ~  ~  ~  ~  ~{RE}   (  ) )_
            ( ` ')  )  {AMA}.--..--..--..--..--..--..--.{RE}   ( ` ')  )
            (_(_.~~~'{AMA}  / .. \.. \.. \.. \.. \.. \.. \  {RE}(_(_.~~~'
                    {AMA}   \ `'\ `'\ `'\ `'\ `'\ `'\ `'\ {RE}
                    {AMA}    `--'`--'`--'`--'`--'`--'`--' {RE}
                                                    
                    {ROSA}    ,~-.  {VERM}{NEG}E M P A T E !{RE}{ROSA}  ,~-.
                    {ROSA}   (  ) )_  {CI}ninguem venceu{RE}{ROSA}  (  ) )_
                    {ROSA}  ( ` ')  )  ~ ~ ~ ~ ~ ~ ~  ( ` ')  )
                    {ROSA} (_(_.~~~'..--..--..--..-.. (_(_.~~~'
                    {ROSA}          \.. \.. \.. \.. \ 
                    {ROSA}           \`'\ `'\ `'\ `'\  
                        {ROSA}            `--'`--'`--'`--' {RE}''')
            ponto_jogador1 += 1
            ponto_ia += 1
        elif (entrada1 == 'pedra'   and entrada_ia == 'tesoura') or \
             (entrada1 == 'papel'   and entrada_ia == 'pedra')   or \
             (entrada1 == 'tesoura' and entrada_ia == 'papel'):
            print(f'\n  {AMA}{entrada1}{RE} vence {VERM}{entrada_ia}{RE}')
            print(f'{NEG}{VERD}  {jogado_1.upper()} VENCEU!{RE}')
            ponto_jogador1 += 1
        else:
            print(f'\n  {AMA}{entrada_ia}{RE} vence {VERM}{entrada1}{RE}')
            print(f'{NEG}{ROSA}  COMPUTADOR VENCEU!{RE}')
            ponto_ia += 1

        print(f'\n  {AZ}{jogado_1}{RE}: {ponto_jogador1} pt(s)  |  {ROSA}Computador{RE}: {ponto_ia} pt(s)')

        jogar_novamente_flag = True
        while jogar_novamente_flag:
            print(f'\n{CI}  [{VERD}CONTINUAR{CI}]{RE} ou {CI}[{VERM}SAIR{CI}]{RE}')
            continuar = input(f'{AMA}> {RE}').strip().lower()
            if continuar == 'continuar':
                sys.stdout.write(HIDE)
                for ciclo in range(2):
                    for i in range(1, 4):
                        pontos = '.' * i
                        sys.stdout.write(f'\r{AZ}{NEG}Reiniciando{pontos:<3}{RE}')
                        sys.stdout.flush()
                        time.sleep(0.2)
                sys.stdout.write(SHOW)
                jogar_novamente_flag = False
            elif continuar == 'sair':
                os.system('cls' if os.name == 'nt' else 'clear')
                if ponto_jogador1 > ponto_ia:
                    ven, cor_v = jogado_1, AZ
                elif ponto_ia > ponto_jogador1:
                    ven, cor_v = 'Computador', ROSA
                else:
                    ven, cor_v = 'EMPATE', AMA
                titulo = 'PLACAR FINAL'.center(32)
                l1 = f'{jogado_1}: {ponto_jogador1} pt(s)'
                l2 = f'Computador: {ponto_ia} pt(s)'
                lv = f'Vencedor: {ven}'
                pad1 = ' ' * (32 - len(l1))
                pad2 = ' ' * (32 - len(l2))
                padv = ' ' * (32 - len(lv))
                print(f"""
{CI}╔══════════════════════════════════╗
║  {AMA}{titulo}{CI}║
╠══════════════════════════════════╣
║  {AZ}{jogado_1}{CI}: {AMA}{ponto_jogador1} pt(s){CI}{pad1}║
║  {ROSA}Computador{CI}: {AMA}{ponto_ia} pt(s){CI}{pad2}║
╠══════════════════════════════════╣
║  Vencedor: {cor_v}{ven}{CI}{padv}║
╚══════════════════════════════════╝{RE}
{VERD}  Obrigado por jogar!{RE}
{CI}  Desenvolvido por:{RE}
{AZ}  Joao Beltrae{RE}
{VERD}  Caio Alvez{RE}
{AMA}  Gabriel Alasca{RE}""")
                jogar_novamente_flag = False
                rodando = False
            else:
                print(f'{NEG}{VERM}  Digite CONTINUAR ou SAIR{RE}')

#MODO 2: COMPUTADOR VS COMPUTADOR
elif entrada == '2':
    print(f"""
            {CI}╔══════════════════════════════════╗
            {CI}║  {AMA}{'MODO DE JOGO'.center(32)}{CI}║
            {CI}╠══════════════════════════════════╣
            {CI}║     {NEG}{ROSA}COMPUTADOR{RE} {CI}VS{RE} {ROSA}COMPUTADOR{RE}{CI}       ║
            {CI}╚══════════════════════════════════╝{RE}""")

    ponto_ia1 = 0
    ponto_ia2 = 0

    rodando = True
    while rodando:
        n1 = random.randint(0, 2)
        if n1 == 0:
            entrada_ia1 = 'pedra'
        elif n1 == 1:
            entrada_ia1 = 'papel'
        else:
            entrada_ia1 = 'tesoura'

        n2 = random.randint(0, 2)
        if n2 == 0:
            entrada_ia2 = 'pedra'
        elif n2 == 1:
            entrada_ia2 = 'papel'
        else:
            entrada_ia2 = 'tesoura'

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\n  {ROSA}CPU 1{RE} escolheu {NEG}{entrada_ia1}{RE}  |  {ROSA}CPU 2{RE} escolheu {NEG}{entrada_ia2}{RE}')
        time.sleep(1)

        if entrada_ia1 == entrada_ia2:
            print(f'''

                ,~-.                                        ,~-.
                (  ) )_   {AMA}~  ~  ~  ~  ~  ~  ~  ~  ~  ~{RE}   (  ) )_
                ( ` ')  )  {AMA}.--..--..--..--..--..--..--.{RE}   ( ` ')  )
                (_(_.~~~'{AMA}  / .. \.. \.. \.. \.. \.. \.. \  {RE}(_(_.~~~'
                        {AMA}   \ `'\ `'\ `'\ `'\ `'\ `'\ `'\ {RE}
                        {AMA}    `--'`--'`--'`--'`--'`--'`--' {RE}
                                                        
                        {ROSA}    ,~-.  {VERM}{NEG}E M P A T E !{RE}{ROSA}  ,~-.
                        {ROSA}   (  ) )_  {CI}ninguem venceu{RE}{ROSA}  (  ) )_
                        {ROSA}  ( ` ')  )  ~ ~ ~ ~ ~ ~ ~  ( ` ')  )
                        {ROSA} (_(_.~~~'..--..--..--..-.. (_(_.~~~'
                        {ROSA}          \.. \.. \.. \.. \ 
                        {ROSA}           \`'\ `'\ `'\ `'\  
                        {ROSA}            `--'`--'`--'`--' {RE}''')
            ponto_ia1 += 1
            ponto_ia2 += 1
        elif (entrada_ia1 == 'pedra'   and entrada_ia2 == 'tesoura') or \
             (entrada_ia1 == 'papel'   and entrada_ia2 == 'pedra')   or \
             (entrada_ia1 == 'tesoura' and entrada_ia2 == 'papel'):
            print(f'\n  {AMA}{entrada_ia1}{RE} vence {VERM}{entrada_ia2}{RE}')
            print(f'{NEG}{ROSA}  CPU 1 VENCEU!{RE}')
            ponto_ia1 += 1
        else:
            print(f'\n  {AMA}{entrada_ia2}{RE} vence {VERM}{entrada_ia1}{RE}')
            print(f'{NEG}{ROSA}  CPU 2 VENCEU!{RE}')
            ponto_ia2 += 1

        print(f'\n  {ROSA}CPU 1{RE}: {ponto_ia1} pt(s)  |  {ROSA}CPU 2{RE}: {ponto_ia2} pt(s)')

        jogar_novamente_flag = True
        while jogar_novamente_flag:
            print(f'\n{CI}  [{VERD}CONTINUAR{CI}]{RE} ou {CI}[{VERM}SAIR{CI}]{RE}')
            continuar = input(f'{AMA}> {RE}').strip().lower()
            if continuar == 'continuar':
                sys.stdout.write(HIDE)
                for ciclo in range(2):
                    for i in range(1, 4):
                        pontos = '.' * i
                        sys.stdout.write(f'\r{AZ}{NEG}Reiniciando{pontos:<3}{RE}')
                        sys.stdout.flush()
                        time.sleep(0.2)
                sys.stdout.write(SHOW)
                jogar_novamente_flag = False
            elif continuar == 'sair':
                os.system('cls' if os.name == 'nt' else 'clear')
                if ponto_ia1 > ponto_ia2:
                    ven, cor_v = 'CPU 1', ROSA
                elif ponto_ia2 > ponto_ia1:
                    ven, cor_v = 'CPU 2', ROSA
                else:
                    ven, cor_v = 'EMPATE', AMA
                titulo = 'PLACAR FINAL'.center(32)
                l1 = f'CPU 1: {ponto_ia1} pt(s)'
                l2 = f'CPU 2: {ponto_ia2} pt(s)'
                lv = f'Vencedor: {ven}'
                pad1 = ' ' * (32 - len(l1))
                pad2 = ' ' * (32 - len(l2))
                padv = ' ' * (32 - len(lv))
                print(f"""
{CI}╔══════════════════════════════════╗
║  {AMA}{titulo}{CI}║
╠══════════════════════════════════╣
║  {ROSA}CPU 1{CI}: {AMA}{ponto_ia1} pt(s){CI}{pad1}║
║  {ROSA}CPU 2{CI}: {AMA}{ponto_ia2} pt(s){CI}{pad2}║
╠══════════════════════════════════╣
║  Vencedor: {cor_v}{ven}{CI}{padv}║
╚══════════════════════════════════╝{RE}
{VERD}  Obrigado por jogar!{RE}
{CI}  Desenvolvido por:{RE}
{AZ}   Joao Beltrae{RE}
{VERD}   Caio Alvez{RE}
{AMA}   Gabriel Alasca{RE}''')
                jogar_novamente_flag = False
                rodando = False
            else:
                print(f'{NEG}{VERM}  Digite CONTINUAR ou SAIR{RE}') 
