https://github.com/JoaoIopBeltrame/Tarefas/blob/main/Tarefas/PjBL%20-%20Batalha-Naval/PjBL%20-%20Batalha-Naval.py# add o negocio de selecionar onde vai as embarcações 
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

CATALOGO = {
    1: {"nome": "Porta-aviões",     "sigla": "P"},
    2: {"nome": "Navio-tanque",     "sigla": "T"},
    3: {"nome": "Contratorpedeiro", "sigla": "C"},
    4: {"nome": "Submarino",        "sigla": "S"},
    5: {"nome": "Destroier",        "sigla": "D"},
}
 
def seleceiona_navios(escolhidos):        
    borda = "─" * 51
    print(f"\n{NEG}{CI}  ╔{borda}╗{RE}")
    print(f"{NEG}{CI}  ║{RE}{'  EMBARCAÇÕES'.ljust(51)}{NEG}{CI}║{RE}")
    print(f"{NEG}{CI}  ╠{borda}╣{RE}")
    print(f"{NEG}{CI}  ║{RE}  {NEG}{'Nº':<4}{'Embarcação':<22}{'Espaç.':<10}{'Status':<13}{RE}{NEG}{CI}║{RE}")
    print(f"{NEG}{CI}  ║{RE}  {'─'*4}{'─'*22}{'─'*10}{'─'*13}  {NEG}{CI}║{RE}")

    navios_info = [
        (1, "Porta-aviões",      5),
        (2, "Navio-tanque",      4),
        (3, "Contratorpedeiro",  3),
        (4, "Submarino",         2),
        (5, "Destroier",         1),
    ]
    for nid, nome, esp in navios_info:
        if nid in escolhidos:
            #cor diferente se o navio ja teiver sido escolhjido
            num_str = f"{AMA}{NEG}{nid}{RE}"
            status  = f"{VERD}✔ Adicionado{RE}"
        else:
            num_str = f"{ROSA}{nid}{RE}"
            status  = f"{AZ}Disponível{RE}"
        print(f"{NEG}{CI}  ║{RE}  {num_str}   {nome:<22}{esp:<10}{status:<22}{NEG}{CI}║{RE}")
 
    total = len(escolhidos)
    cor_total = VERD if total >= 5 else VERM
    print(f"{NEG}{CI}  ╠{borda}╣{RE}")
    print(f"{NEG}{CI}  ║{RE}  {cor_total}{NEG}Selecionados: {total}/5{RE}{'':<33}{NEG}{CI}║{RE}")
    print(f"{NEG}{CI}  ╚{borda}╝{RE}")

    #cores
    print(f"\n  {NEG}Legenda de cores:{RE}")
    print(f"  {ROSA}■{RE} Disponível   {AMA}■{RE} Já escolhido   {VERD}✔{RE} Adicionado")
 
def lista_batalha_naval():
    matriz_principal = []
    for i in range(1, 11):
        linha = []
        for j in range(1, 11):
            linha.append(0)
        matriz_principal.append(linha)
    return matriz_principal

#tabuleiro (ascii)
def exibir_tabuleiro(tab, titulo):
    borda = "─" * 43
    print(f"\n{NEG}{CI}  ╔{borda}╗{RE}")
    print(f"{NEG}{CI}  ║{RE}{NEG}{titulo.center(43)}{RE}{NEG}{CI}║{RE}")
    print(f"{NEG}{CI}  ╠{borda}╣{RE}")
 
    # cabeçalho de colunas
    cab = "    " + "  ".join(f"{CI}{NEG}{j}{RE}" for j in range(10))
    print(f"  {NEG}{CI}║{RE} {cab}   {NEG}{CI}║{RE}")
    print(f"  {NEG}{CI}║{RE}    {'─'*33}    {NEG}{CI}║{RE}")
 
    for i, linha in enumerate(tab):
        celulas = []
        for c in linha:
            if c == 0 or c == "~":
                celulas.append(f"{AZ}~{RE}")   # água
            elif c == "X":
                celulas.append(f"{VERM}{NEG}X{RE}")  # acerto
            elif c == "O":
                celulas.append(f"{AMA}O{RE}")   # erro
            else:
                celulas.append(f"{VERD}{NEG}{c}{RE}")  # navio
        linha_str = "  ".join(celulas)
        print(f"  {NEG}{CI}║{RE} {AMA}{NEG}{i}{RE} │ {linha_str}   {NEG}{CI}║{RE}")
 
    print(f"  {NEG}{CI}╚{borda}╝{RE}")
 
def inputs(frase, tipo=str):
    entrada = input(f'{frase}\n> ')
    if tipo == str:
        return entrada.strip()
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

#linha e coluna requisitados

def posicionar_navios(escolhidos, tab):
    print(f"\n{NEG}{CI}  Agora posicione suas embarcações no tabuleiro, Big Boss.{RE}")
    print(f"  Índices válidos: {AMA}0 a 9{RE} (linha e coluna)\n")
 
    for nid in sorted(escolhidos):
        info = CATALOGO[nid]
        while True:
            exibir_tabuleiro(tab, " SEU TABULEIRO ")
            print(f"\n  Posicionando: {ROSA}{NEG}{info['nome']}{RE} [{info['sigla']}]")
            try:
                lin = int(input(f"  {AZ}Linha{RE}   (0-9): "))
                col = int(input(f"  {AZ}Coluna{RE}  (0-9): "))
            except ValueError:
                print(f"{VERM}  Digite apenas números!{RE}")
                time.sleep(1)
                continue
 
            if lin < 0 or lin > 9 or col < 0 or col > 9:
                print(f"{VERM}  Índice fora do range 0-9!{RE}")
                time.sleep(1)
                continue
 
            if tab[lin][col] != 0:
                print(f"{VERM}  Posição ({lin},{col}) já ocupada, Big Boss! Tente outra.{RE}")
                time.sleep(1)
                continue

                #aq coloca a sigla do naviao na coluna
                tab[lin][col] = info['sigla']
                print(f"{VERD}  ✔ {info['nome']} posicionado em ({lin},{col})!{RE}")
                time.sleep(0.8)
                break
def main():
    while True:

        #p guardar retoirno input em entrada
        entrada = inputs('Digite (1) para ver as informações do jogo e (2) para jogar')
 
        if entrada == '1':
            escolhidos = set()      # set vazio no inicio
 
            while True:
                limp_term()
                seleceiona_navios(escolhidos)
 
                print(f"\n  {ROSA}[1-5]{RE} Selecionar embarcação")
                print(f"  {AMA}[P]  {RE} Posicionar navios no tabuleiro")
                print(f"  {VERM}[0]  {RE} Voltar ao menu\n")
                cmd = input('> ').strip()
 
                if cmd in ('1', '2', '3', '4', '5'):
                    nid = int(cmd)
                     #nloqueia se ja tiver sendo escolhido aq
                    if nid in escolhidos:
                        print(f"\n{VERM}  Essa embarcação já foi adicionada. Escolha outra, Big Boss {RE}")
                        time.sleep(1.2)
                    else:
                        escolhidos.add(nid)
                        print(f"\n{VERD}  {CATALOGO[nid]['nome']} adicionado!{RE}")
                        time.sleep(0.8)
 
                elif cmd.upper() == 'P':
                    if len(escolhidos) < 5:
                        print(f"\n{VERM}  Selecione pelo menos {5 - len(escolhidos)} embarcação(ões) ainda!{RE}")
                        time.sleep(1.2)
                    else:
                        # ── NOVO: cria tabuleiro e posiciona os navios
                        tab = lista_batalha_naval()
                        posicionar_navios(escolhidos, tab)
                        limp_term()
                        exibir_tabuleiro(tab, " SEU TABULEIRO FINAL ")
                        inputs('Pressione ENTER para voltar ao menu')
                        terminal_voltando('Voltando')
                        break
 
                elif cmd == '0':
                    terminal_voltando('Voltando')
                    break
 
                else:
                    print(f'{VERM}  Opção inválida.{RE}')
                    time.sleep(0.8)
 
        else:
            print('Digite 1 para as informações e 0 para iniciar o jogo')
 
if __name__ == '__main__':
    main()






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
