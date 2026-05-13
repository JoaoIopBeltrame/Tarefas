vetor = [0.0] * 15
vetor_float = [0.0] * 15
for nota in range(15):
    while True:
        try:
            vetor[nota] = input(f'Digte sua {nota + 1}° nota\n> ').strip().replace(',', '.')
            if vetor[nota] == '':
                continue
            vetor_float[nota] = float(vetor[nota])
            break
        except ValueError:
            print('Dige apenas numeros')    
soma = 0
for v in vetor_float:
    soma += v
resultado = soma / 15
print(f'A sua media foi de {resultado:.2f}')