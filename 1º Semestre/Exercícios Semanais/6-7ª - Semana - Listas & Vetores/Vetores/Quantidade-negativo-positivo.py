vetor = [0.0] * 10
for i in range(10):
    while True:
        try:
            entrada = input(f'Digite o {i + 1}° numero\n> ').strip().replace(',', '.')
            vetor[i] = float(entrada)
            break
        except ValueError:
            print('Digite apenas numeros reais')

contador_negativos = 0
soma_positivos = 0
for v in vetor:
    if v < 0:
        contador_negativos += 1
    elif v > 0:
        soma_positivos += v

print(f'Vetor: {vetor}')
print(f'Quantidade de negativos: {contador_negativos}')
print(f'Soma dos positivos: {soma_positivos}')