vetor = [0] * 5
for i in range(5):
    while True:
        try:
            entrada = input(f'Digite o {i + 1}° numero\n> ').strip().replace(',', '.')
            vetor[i] = int(entrada)
            break
        except ValueError:
            print('Digite apenas numeros reais')
print(vetor)
maior = max(vetor)
menor = min(vetor)

for i in range(5):
    if vetor[i] == maior:
        posmaior =  i
    if vetor[i] == menor:
        posmenor =  i

print (f"posição do maior {posmaior} e posição menor {posmenor}") 
 

    