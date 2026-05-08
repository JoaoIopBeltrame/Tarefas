import os
import time
import sys

def recomeco(frase_erro):
    print(f"{frase_erro}. Pressione 'ENTER' para reiniciar o sistema\n> ").strip()

def animacao(palavra):
    sys.stdout.write(f'{palavra}')
    for _ in range(3):   
        time.sleep(0.5)
        sys.stdout.write('.')
        sys.stdout.flush()
    print()
    
lista_numeros = []
par = 0
impar = 0
while len(lista_numeros) < 10:
    try:
    
        print(f"\nProgresso: {len(lista_numeros)}/10")
        print(f"Lista atual: {lista_numeros}")
        
        numero = input('Digite 10 números para saber se é impar ou par\n> ').strip()
        
        if not numero.isnumeric():
            recomeco('ERRO! Só é possível usar números')
            animacao('Reiniciando')
            continue
            
        numero_float = float(numero)
        lista_numero = lista_numeros.append(numero_float)
        
        if numero_float % 2 == 0:
            print(f'O número {numero_float} é PAR')
            par += 1
        else:
            print(f'O número {numero_float} é ÍMPAR')
            impar += 1
            
            print(f'{par} nueros par e {impar} numeros impar')
        
    except Exception as e:
        print(f'Um erro do tipo {e} ocorreu')
