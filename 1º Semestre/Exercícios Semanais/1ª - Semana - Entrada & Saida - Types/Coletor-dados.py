import os
import time

from datetime import datetime
ano_atual = datetime.now().year

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_idade(ano_atual_def, ano_input):
    return ano_atual_def - ano_input

def encerrar_sistema_animacao():
    print("Reiniciando", end="", flush=True)
    for i in range(4):
        time.sleep(0.5)
        print(".", end="", flush=True)


while True:
    try:
        limpar_terminal()
        print("=" * 35)
        print("          COLETOR DE DADOS")
        print("=" * 35)
        time.sleep(1)


        while True:

            digitar_nome = input("Digite seu nome\n").strip().capitalize()
            
            print(f"{digitar_nome} foi armazenado")
            limpar_terminal()
            time.sleep(0.7)
            
            while True:
                digitar_cpf = int(input("Digite o seu CPF\n"))
                
                parte1 = digitar_cpf[0:3]
                parte2 = digitar_cpf[3:6]
                parte3 = digitar_cpf[6:9]
                parte4 = digitar_cpf[9:11]
                

                if len(digitar_cpf) != 11:
                    print("ERRO: O CPF deve conter 11 números. Tente novamente")
                    continue
                else:
                    resultado_cpf = print(f"{parte1}.{parte2}.{parte3}-{parte4}")
                    limpar_terminal()
                    time.sleep(0.7)

                    while True:
                        digitar_telefone = int(input("Digite seu telefone junto com o seu DDD\n"))

                        parte1_telefone = digitar_telefone[0:2]
                        parte2_telefone = digitar_telefone[2:7]
                        parte3_telefone = digitar_telefone[7:11]
                        
                        if len(digitar_telefone) != 11:
                            print("ERRO: O telefone deve conter 11 números. Tente novamente")
                            continue
                        else:
                            resultado_telefone = print(f"({parte1_telefone}) {parte2_telefone}-{parte3_telefone} armazenado")
                            limpar_terminal()
                            time.sleep(0.7)


                            while True:
                                digite_ano = int(input("Digite seu ano de nascimento\n"))
                                
                                if len(digite_ano) != 4:
                                    print("ERRO: O ano de nascimento deve ter 4 digitos. Tente novamente")
                                    time.sleep(1.4)
                                
                                elif digite_ano < 1900:
                                    print("ERRO: O ano de nascimento minimo é (1900). Tente novamente")
                                    time.sleep(1.4)

                                else:
                                    print(f"{digite_ano} armazenado")
                                    break




                                resultado_final = print(f"Olá {digitar_nome}, você nasceu  no ano de {digite_ano}, seu numero de telefone é {resultado_telefone}, e seu CPF é {resultado_cpf}")
                        
                        

                        

    except (ValueError, TypeError):
        print("\n[ERRO]: Digite apenas números para CPF e Telefone!")
        time.sleep(2)
