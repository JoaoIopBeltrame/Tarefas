caminho = input("Você está em uma floresta. Escolha um caminho (esquerda/direita): ").lower()

if caminho == "esquerda":
    print("Você encontrou um rio.")
    decisao = input("Deseja atravessar ou voltar?").lower()
    
    if decisao == "atravessar":
        print("Você chegou a uma vila.")
    else:
        decisao == "voltar"
        print("Você voltou e permanece perdido na floresta.")

elif caminho == "direita":
    print("Você encontrou uma montanha.")
    decisao = input("Deseja subir ou voltar?").lower()
    
    if decisao == "subir":
        print("Incrível! Você encontrou um tesouro no topo!")
    else:
        decisao == "voltar"
        print("Você voltou e permanece perdido na floresta.")
else:
    print("Escolha inválida. Você ficou parado e se perdeu.")

