import time
import os
import sys


def limpar_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def anim_reiniciar(palavra='Reiniciando'):
    for loop_maior in range(5):
        limpar_terminal()
        sys.stdout.write(palavra)
        for loop_menor in range(3):
            sys.stdout.write('.')    
            sys.stdout.flush()
            time.sleep(0.1)
        print('\n')

def eh_palindromo(palavra):
    limpa = palavra.lower().replace(' ', '')
    return limpa == limpa[::-1]

def main():
    while True:
        palavra = input('Digite uma palavra | Pressione (1) para finalizar sistema\n> ')
        if palavra == '1':
            time.sleep(1)
            anim_reiniciar('Finalizando sistema')
            break
        if eh_palindromo(palavra):
            print(f'|{palavra}| é um palindromo')
        else:
            print(f'A palavra |{palavra}| não é palindromo')

if __name__ == '__main__':
    main()