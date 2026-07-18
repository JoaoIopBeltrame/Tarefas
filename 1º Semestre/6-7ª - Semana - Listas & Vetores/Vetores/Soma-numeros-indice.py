vetor = [0] * 8
for i in range(8):
    vetor[i] = int(input(f'Digte o {i + 1}° numero\n> '))
print(f'O primeiro valor é o numero do indicie{list(enumerate(vetor))}')
while True:
    x = int(input('Digite o 1° indice\n> '))
    print(vetor[x])
    y = int(input('Digite o 2° indice\n> '))
    print(vetor[y])
    if 0 <= X < len(vetor) and 0 <= Y < len(vetor):
        print(vetor[x] + vetor[y])
