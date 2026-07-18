import time
from datetime import datetime
import os

def limpar_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def ano_de_def(ano_nascimento):
    ano_atual = datetime.today().year
    return ano_atual - ano_nascimento

while True:
    try:
        limpar_terminal()
        print("="*35)
        print("     CALCULADOR DE IDADE")
        print("="*35)
        
        condições = "O ano deve ter 4 números e estar entre 1900 e 2026"
        print(condições)
        time.sleep(0.72)
        
        digitar_idade = input("Digite o ano em que você nasceu: \n").strip() 

        if digitar_idade == "":
            print("\nVocê não digitou nada! Tente novamente.")
            time.sleep(0.5)
            continue

        digitar_idad_int = int(digitar_idade)

        if len(digitar_idade) == 4 and digitar_idad_int >= 1900 and digitar_idad_int <= 2026:
            resultado = ano_de_def(digitar_idad_int)
            
            time.sleep(1)
            limpar_terminal()
            print("Carregando.")
            time.sleep(0.4)
            limpar_terminal()
            print("Carregando..")
            time.sleep(0.4)
            limpar_terminal()
            print("Carregando...")
            time.sleep(0.5)
            limpar_terminal()

            print("="*35)
            print(f"         A SUA IDADE É {resultado}")
            print("="*35)

            while True:
                deseja_continuar = input("\nDeseja calcular uma nova idade? (s/n)\n").lower().strip()
                if deseja_continuar == "s":
                    time.sleep(0.5)
                    break
                elif deseja_continuar == "n":
                    print("\nAté logo! Encerrando sistema...")
                    time.sleep(1)
                    exit()
                else:
                    print("Só é permitido o uso de 's' ou 'n'.")

        else:
            print("\nERRO: O ano deve estar entre 1900 e 2026.")
            time.sleep(2)
            continue
            
    except (ValueError, TypeError):
        print("\nERRO!!! Digite apenas números inteiros (4 dígitos).")
        time.sleep(2)
