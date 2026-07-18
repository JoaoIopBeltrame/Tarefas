import time
import os

def limpar_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def calculadora_media(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

while True:
    limpar_terminal() 
    print("="*35)
    print("      CALCULADOR DE MÉDIAS")
    print("="*35)
    lista_notas = []
    
    while True:
        try:
            digitar_notas = input("\nDigite as suas notas, e quando terminar pressione (f) para calcular sua média\n").replace(",", ".").lower().strip()
            limpar_terminal()
            if digitar_notas == "f":
                time.sleep(1)
                print("Calculando média... Aguarde")
                break 
            else:
                digitar_notas != "f"
                print(f"\n \t \t \t \t \t \t \t \t \t Você deve precionar a letra (f) para calcular a média, ou introduzir nota")
                
                digitar_notas_float = float(digitar_notas) 
                if 0 <= digitar_notas_float <= 10:
                    lista_notas.append(digitar_notas_float)
                    print(f"\n\tA nota {digitar_notas_float} foi salva!")
                else:
                    print("\nSó é pemitido o envio de notas que estão entre 0 e 10. Tente novamente...")
                    
        
        except ValueError:
            print("ERRO: Digite apenas números")
            continue
        
    if len(lista_notas) > 0:
        resultado = calculadora_media(lista_notas) 
        print("="*90)
        print("      RESUMO DO ESTUDANTE")
        print("="*90)
        print(f"      Quais notas foram cauculadas:  {lista_notas}")
        print(f"      Notas registradas:  {len(lista_notas)}")
        print(f"      A média do aluno foi de:  {resultado:.1f}")
        print("="*90)
        
    else: 
        print("Você precisa adicionar números para calcular a sua média")

    while True:
        novo_envio_notas = input("\nOlá, você deseja calcular mais notas? Precione(s/n): ").strip().lower()
        if novo_envio_notas == "s":
            break
        elif novo_envio_notas == "n":
            print("Encerrando sistema... Por hojê é só pessoal")
            exit()
        else:
            novo_envio_notas != "s" or "n"
            print("Só é possível o envio de (s) ou (n). Tente novamente")


