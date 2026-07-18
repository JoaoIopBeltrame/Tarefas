import time
import os

def limpar_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def calcular_total(quantidade_carro, valor=100):
    return quantidade_carro * valor

while True:
    try:
        limpar_terminal()
        print("          LOJA DE CARROS")
        print("="*45)
        print("Preço: 100 reais por carro")
        print("-"*45)

        quantidade_carro = input("Digite quanto(s) carro(s) você gostaria de comprar, sabendo que cada carro está custando (R$ 100)\n").replace(",", ".").strip()
        
        if quantidade_carro == "":
             print("\nVocê não digitou nada, tente novamente")
             time.sleep(1)
             continue

        quantidade_carro_int = int(quantidade_carro)

        total = calcular_total(quantidade_carro_int)
        time.sleep(0.2)
        
        print("Processando compra.")
        time.sleep(0.5)
        limpar_terminal()
        print("Processando compra..")
        time.sleep(0.5)
        limpar_terminal()
        print("Processando compra...")
        time.sleep(0.5)
        limpar_terminal()
        print("Processando compra....")
        time.sleep(0.9)

        limpar_terminal()
        print("="*45)
        print(f"Você comprou: {quantidade_carro_int} carro(s)")
        print("-"*45)
        print(f"Preço do carro: R$ 100")
        print("-"*45)
        print(f"Total pra pagar: {total}")
        print("="*45)
    
        while True:
            continuar = input("\nDeseja continuar comprando pressione (s/n) para prosseguir!\n").lower().strip()
            if continuar == "s":
                time.sleep(0.5)
                print("\n\tOlá novamente, quantos carro(s) você gostaria de comprar hojê")
                break
            elif continuar == "n":
                print("Até logo, obrigado pela compra! :D")
                time.sleep(0.5)
                exit()
            else:
                print("Só é possível a utilização do (s/n) tente novamente")

    except(ValueError):
        time.sleep(0.7)
        print(f"ERRO!!! {quantidade_carro} não é considerado um número valido para efetuar a compra do carro, tente novamente!\n")
        continue


