import time
import os
import sys
import re
from collections import Counter


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

def contar_caracteres(string):
    letras = re.findall(r'[a-zA-ZÀ-ÿ]', string)
    return Counter(letras)

def main():
    while True:
        palavra = input('Digite uma palavra | Pressione (1) para finalizar\n> ')
        if palavra == '1':
            time.sleep(1)
            anim_reiniciar('Finalizando sistema')
            break
        contagem = contar_caracteres(palavra)
        for letra, qtd in contagem.items():
            print(f'|{letra}| aparece {qtd} vez(es)')

if __name__ == '__main__':
    main()