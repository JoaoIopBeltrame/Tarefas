vetor = [0] * 6
for entrada in range(6):
    vetor[entrada] = int(input(f'Digite o {entrada + 1}° numero\n> '))
contador_par = 0
contador_impar = 0
for par_impar in vetor:
    if par_impar % 2 == 0:
        print(f'O numero {par_impar} é par')
        contador_par += 1
    else:    
        print(f'O numero {par_impar} é impar')
        contador_impar += 1
print(f'Tem {contador_par} numeros pares')
print(f'Tem {contador_impar} numeros impares')