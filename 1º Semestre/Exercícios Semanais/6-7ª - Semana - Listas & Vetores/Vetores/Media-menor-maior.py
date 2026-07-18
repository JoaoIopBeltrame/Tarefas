vetor = [0] * 5
for i in range(5):
    while True:
        try:
            entrada = input(f'Digite o {i + 1}° numero\n> ').strip().replace(',', '.')
            vetor[i] = int(entrada)
            break
        except ValueError:
            print('Digite apenas numeros reais')
print(f'Os valores lidos, foram\n> {vetor}')
print(f'O menor valor lido for \n> {min(vetor)}')
print(f'O maior valor lido for \n> {max(vetor)}')
print(f'A media entre o menor numero e o maior é\n> {(min(vetor) + max(vetor)) / 2}')


