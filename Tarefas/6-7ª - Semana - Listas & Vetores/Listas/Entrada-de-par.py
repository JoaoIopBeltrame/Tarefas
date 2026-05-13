par = []
for impar_par in range(1, 101):
    if impar_par % 2 == 0:
        par.append(impar_par)
    else:
        pass
print(f'Pares\n> {par}')