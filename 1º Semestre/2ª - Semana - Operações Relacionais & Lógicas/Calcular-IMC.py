import time
import os

def limpar_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def imc_calculadora(peso, altura):
    return peso / (altura ** 2)

while True:
    limpar_terminal()
    print("="*35)
    print("       CALCULADORA DE IMC")
    print("="*35)

    try:
        digitar_peso = input("Digite o seu peso em (KG): \n").replace(",", ".").strip()
        digitar_altura = input("Digite a sua altura em (M): \n").replace(",", ".").strip()
        
        float_peso = float(digitar_peso)
        float_altura = float(digitar_altura)
        
        resultado = imc_calculadora(float_peso, float_altura)
        
        time.sleep(0.5)
        print("Calculando IMC.")    
        time.sleep(0.3)
        print("Calculando IMC..")
        time.sleep(0.3)
        print("Calculando IMC...")
        time.sleep(0.5)
        
        limpar_terminal()
        print("="*35)
        print(f"\t  SEU IMC É {resultado:.1f}")
        print("="*35)

       
        while True:
            time.sleep(0.7)
            continuar = input("\nGostaria de calcular um novo IMC? (s/n): ").lower().strip()
            
            if continuar == "s":
                print("\nReiniciando...")
                time.sleep(0.5)
                break 
            elif continuar == "n":
                print("Encerrando sistema... Até logo!")
                time.sleep(0.5)
                limpar_terminal()
                exit() 
            else:
                print("Opção inválida! Digite apenas 's' ou 'n'.")

    except ValueError:        
        print("\nERRO: Só é possível a utilização de números... Tente novamente")
        time.sleep(2)
