def tiroUsuario(matrizInimiga, linha, coluna):


    tipoNavio = matrizInimiga[linha][coluna]
    if tipoNavio == 0:                       
        print('Voce acertou a agua')
        return None
    navioAcerto = NAVIOS_INDICE[tipoNavio]
    print(f'Voce acertou um navio {navioAcerto}')
    matrizInimiga[linha][coluna] = 0        
    
    if not barcoDestruido(matrizInimiga):   
        print(f'{AMA}Há um pedaço restante do {navioAcerto}{RE}')
    else:
        print(f'{VERM}O {navioAcerto} foi totalmente destruido{RE}')

def tiroCPU(matrizFinalUsuario):
    tiroRandomLinha = random.randint(0, 9)
    tiroRandomColuna = random.randint(0, 9)
    randomTiroNaMatrz = matrizFinalUsuario[tiroRandomLinha][tiroRandomColuna]
    if randomTiroNaMatrz == 0:
        print('O inimigo acerttou a agua')
    else:
        nome = NAVIOS_INDICE[randomTiroNaMatrz]
        print(f'O inimigo acertou {nome}')
        matrizFinalUsuario[tiroRandomLinha][tiroRandomColuna] = 0
    return matrizFinalUsuario
        
def faseDeCombate(matrizFinalUsuario):
    print(f'{VERM}A tropa inimiga ja posicionou suas tropas{RE}')
    matrizDoInimigo = tabuleiroCPU()          
    while not barcoDestruido(matrizDoInimigo):  
        tiroPermitidos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        mostrarTabulero(matrizFinalUsuario)  
 
        try:
            tiroLinha = int(input(f'{CI}\nDigite a linha do tiro (0-9)\n> {RE}'))
            tiroColuna = int(input(f'{CI}Digite a coluna do tiro (0-9)\n> {RE}'))
            tiro = input(f'{CI}Digite o codigo secreto (ou ENTER para atirar)\n> {RE}') 
        except ValueError:
            print('Digite apenas numeros inteiros')
            continue
        
        if tiroLinha < 0 or tiroLinha > 9 or tiroColuna < 0 or tiroColuna > 9:   
            print('Digite um numero entre (0 - 9)')
            continue
        
        if tiro == 'ccbededba':        
            print(f'{ROSA}Codigo secreto ativado{RE}')
            palavraAnimada('Usando sonar')                  
            palavraAnimada('Avaliando tropas inimigas')     
            print(f'{ROSA}Localização inimiga{RE}')
            mostrarTabulero(matrizDoInimigo)       
            tiroUsuario(matrizDoInimigo, tiroLinha, tiroColuna)   # 
            matrizFinalUsuario = tiroCPU(matrizFinalUsuario)
            mostrarTabulero(matrizDoInimigo)      
            input(f'{AMA}Pressione ENTER para continuar\n> {RE}')
            
        else:
            tiroUsuario(matrizDoInimigo, tiroLinha, tiroColuna)  
            matrizFinalUsuario = tiroCPU(matrizFinalUsuario)       # Correção do BUG 5
            mostrarTabulero(matrizFinalUsuario)
 
        # Correção da Indentação quebrada que fechava o jogo do nada
        if barcoDestruido(matrizDoInimigo):   
            print('O jogador venceu')
            if not jogarNovamente():            
                palavraAnimada('Saindo')
                sys.exit()
            else:
                break
        else:
            if barcoDestruido(matrizFinalUsuario):
                print('O adiversario venceu')
                if not jogarNovamente():            
                    palavraAnimada('Saindo')
                    sys.exit()
                else:
                    break
        continue
 
 
