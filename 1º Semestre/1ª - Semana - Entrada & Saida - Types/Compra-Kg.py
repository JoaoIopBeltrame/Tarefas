import os
import time

def limpar_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def calcular_preco(fruta, peso):
    if fruta == "banana": return peso * 9
    elif fruta == "maçã": return peso * 14
    elif fruta == "uva": return peso * 21
    elif fruta == "pera": return peso * 15
    elif fruta == "coco ralado": return peso * 45
    elif fruta == "pinhão": return peso * 13
    return 0



while True:
    lista_frutas =  ["banana", "maçã", "uva", "pera", "coco ralado", "pinhão"]
    
    while True: 

        try:
            limpar_terminal()
            print("="*45)
            print("          COMPRAS POR PESO")
            print("="*45)
            print(f"Frutas na lista: {lista_frutas}")
            print("-" * 45)

            escolha_fruta = input(f"Qual item da lista |{lista_frutas}|, voce deseja comprar\n").strip().lower()
            if escolha_fruta not in lista_frutas:
                print(f"Erro!! o item {escolha_fruta} não esta em nossa lista")
                continue
                
                
            digite_peso = input(f"Digite quantos (Kg) de {escolha_fruta} voce deseja comprar\n").replace(",", ".").strip()
            if digite_peso == "":
                print("ERRO!!! Voce não digitou nenhum peso, tente novamente")
                time.sleep(1.5)
                continue
                

            digite_peso_float = float(digite_peso)

            resultado = calcular_preco(escolha_fruta, digite_peso_float)

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


            print("+" + "-" * 43 + "+")
            print(f" ITEM: {escolha_fruta.upper()}")
            print(f" PESO: {digite_peso_float} Kg")
            print(f" TOTAL A PAGAR: R$ {resultado:.2f}")
            print("+" + "-" * 43 + "+")

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

        except (ValueError, TypeError):
            print("\nERRO!!! Digite apenas números inteiros (4 dígitos).")
            time.sleep(2)
