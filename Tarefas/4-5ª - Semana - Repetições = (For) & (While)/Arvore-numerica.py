while True:
    entrada = input('Digite um numero\n> ')

    try:
        valor = int(entrada)
    except ValueError:
        print('Digite apenas numeros')
        continue
    
    for linha in range(1, valor + 1):
        for i in range(1, linha + 1):
            print(i, end=" ")
        print('\n')
