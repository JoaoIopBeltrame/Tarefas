vetor = [0] * 6
for pedido in range(6):
    while True:
        try:
            vetor[pedido] = int(input(f'Digite o {pedido + 1}°\n> '))
            break
        except ValueError:
            print('Digite numeros inteiros')

print('Valores lidos:')
print(vetor)