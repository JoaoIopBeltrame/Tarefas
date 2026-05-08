import os
import time
from datetime import datetime

def limpar_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def calcular_meses_vida(anos):
    mes_atual = datetime.now().month
    return (anos * 12) + mes_atual

while True:
    try:
        limpar_terminal()
        print("="* 45)
        print("      CALCULADORA DE ANOS VIVIDOS EM MESES")
        print("="* 45)

        digitar_idade = input("Digite a sua idade em anos: \n").strip()

        if digitar_idade == "":
            print("Erro: Você não digitou nada!")
            time.sleep(1)
            continue
            
        idade_int = int(digitar_idade) 
        resultado = calcular_meses_vida(idade_int)


        time.sleep(0.4)
        limpar_terminal()
        print("Processando.")
        time.sleep(0.4)
        limpar_terminal()
        print("Processando..")
        time.sleep(0.4)
        limpar_terminal()
        print("Processando...")
        time.sleep(0.6)
        limpar_terminal()

        print("+" + "=" * 43 + "+")
        print(f"   VOCÊ TEM {resultado} MESES DE IDADE")
        print("+" + "=" * 43 + "+")

        while True:
            opcao = input("\nDeseja calcular outra idade? (s/n): ").strip().lower()
            
            if opcao == "n":
                print("Encerrando... Até logo!")
                time.sleep(1)
                exit()
            elif opcao == "s":
                print("Reiniciando...")
                time.sleep(0.8)
                break 
            else:
                print("Apenas 's' ou 'n'!")
    except (ValueError, TypeError):
        print("Erro: Digite apenas números inteiros!")
        time.sleep(2)
