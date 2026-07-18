import time
import os

def limpar_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def converter_farenheint(convertor_celsius):
    return (convertor_celsius * 9/5) + 32

while True: 
    limpar_terminal() 
    print("="*35)
    print("     CALCULADOR DE FAHRENHEIT")
    print("="*35)

    try:
        graus_celsius = input("Digite a temperatura em ºC: \n").replace(",", ".").strip()
        graus_celsius_float = float(graus_celsius)
        
        time.sleep(0.9)
        resultado = converter_farenheint(graus_celsius_float)
        
        time.sleep(0.7)
        limpar_terminal()
        print("="*64)
        print(f"\tA temperatura {graus_celsius_float:.1f} ºC em Fahrenheit é {resultado:.1f} ºF")
        print("="*64)
        
    except (TypeError, ValueError):
        print(f"ERRO!!! '{graus_celsius}' não é um número válido. Tente novamente.")
        time.sleep(2)
        continue
    while True:
        time.sleep(0.7)
        continuar = input("\nGostaria de calcular uma nova temperatura? (s/n): ").lower().strip()
        
        if continuar == "s":
            print("\nReiniciando...")
            time.sleep(0.5)
            break
            
        elif continuar == "n":
            print("Encerrando sistema... Até logo!")
            time.sleep(0.5)
            exit() 
            
        else:
            print("Opção inválida! Digite apenas 's' ou 'n'.")
