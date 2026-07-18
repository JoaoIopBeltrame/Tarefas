par =[]
impar =[]
for impar_par in range(1, 11):
    if impar_par % 2 == 0:
        par.append(impar_par)
    else:
        impar.append(impar_par)
print(f'Pares\n> {par}')
print(f'Impares\n> {impar}')
print(f'As duas juntas\n> {sorted(impar + par)}')