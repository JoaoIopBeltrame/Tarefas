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

def maior_elemento(lista):
    return max(lista)

def main():
    lista = []
    while True:
        palavra = input('Digite numero | Pressione (k) para finalizar sistema\n> ')
        if palavra.lower() == 'k':
            if not lista:
                print('Lista vazia')
            else:
                print(f'A lista\n> {lista}')
                print(f'O maior numero\n> {maior_elemento(lista)}')
            time.sleep(1)
            anim_reiniciar('Finalizando sistema')
            break
        try:
            lista.append(int(palavra))
        except ValueError:
            print('Digite numeros')

if __name__ == '__main__':
    main()