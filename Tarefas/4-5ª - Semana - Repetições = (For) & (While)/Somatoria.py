numeros = []
while True:
    entrada = input('Digite um numero inteiro positivo\n> ').strip()
    
    try:
        entrada_int = int(entrada)
        positivo_inteiro = abs(entrada_int)
        
        if positivo_inteiro > 0:
            break
        
    except ValueError:
        print('Digite apenas numeros')
        
lista_numeros = []
soma = 0

for i in range(1, positivo_inteiro + 1):
    soma += i
    lista_numeros.append(str(i))
  
expressao = ' + '.join(lista_numeros)
print(f'{expressao} = {soma}')
