lista = []
for l in range(3):
    try:
        lista.append(int(input(f'Digite o seu {l + 1}° numero\n> ')))
    except ValueError:
        print('Digite apenas nueros inteiros')    
print(lista)