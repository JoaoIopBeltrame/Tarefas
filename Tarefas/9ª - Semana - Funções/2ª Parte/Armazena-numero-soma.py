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


def soma_elementos(lista):
   return sum(lista)

def main():
    lista = []
    while True:
        entrada = input('Digite numero | Pressione (K) para calcular a nota\n> ')
        if entrada == 'k'.lower():
            print(f'Numeros usados\n> {list(lista)}')
            print(soma_elementos(lista))
            break
        try:
            lista.append(float(entrada.replace(',', '.')))
        except ValueError:
            print('Digite algo')
            time.sleep(1.5)
            anim_reiniciar()
            continue
        


if __name__ == '__main__':
    main()
