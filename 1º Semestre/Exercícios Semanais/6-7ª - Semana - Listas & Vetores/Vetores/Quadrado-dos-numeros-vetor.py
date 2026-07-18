vetor = [0] * 10
for i in range(10):
    vetor[i] = int(input(f'Digite o {i + 1}° numero\n> '))
quadrado = [v ** 2 for v in vetor]
print(quadrado)
print(vetor)    
    


