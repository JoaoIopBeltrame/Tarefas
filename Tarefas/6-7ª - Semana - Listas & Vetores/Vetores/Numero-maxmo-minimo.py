vetor = [0] * 10
for pedido in range(10):
    while True:
        try:
            vetor[pedido] = float(input(f'Digite o {pedido + 1}°\n> ')).replace(',', '.').strip()
            break
        except ValueError:
            print('Digite numeros inteiros')
print(f' O maior valor escrito foi {max(vetor)}')
print(f' O menor valor escrito foi {min(vetor)}')