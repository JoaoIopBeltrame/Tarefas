import sys
matriz = []                 # criei uma matriz vazia para conseguir armazenar a 'linha' que tera os 1 e 0 e uso o append para armazenar
for linha in range(4):     # criar um for loop, a cada loop lsita vazia chamada linha é criada
    l = []
    for coluna in range(4):      # para a coluna a cada 1 loop de linha 4 loops ocorrem dentro do C
        valor = int(input(f'Digite o valor da coordenada [{linha}, {coluna}]\n> '))
        l.append(valor)   # armazenar um os valores de input denntro da lista l e no final do loop coluna a lista 'l' coloca os valores dentro da lista matriz
    matriz.append(l)
for l in matriz:  # para ca elemento 'l' dento da lista matriz cai no loop = 'para cada 'i' presentes na lista 'l' vai ipriir o valor 'i' com um espaçamento de 7 etre elas e o 'sys.stdout.write' pq ele naopula liha e evita usar o end=''
    for i in l:
        sys.stdout.write(f'{i:15},')
    print()

max_valor = matriz[0][0]  # começa assumindo que o primeiro elemento é o maior, será substituído se achar algo maior
maior_linha = 0           # guarda o índice da linha onde está o maior valor, inicia em 0
maior_coluna = 0          # guarda o índice da coluna onde está o maior valor, inicia em 0

for i in range(4):        # percorre cada linha da matriz (0 até 3)
    for j in range(4):    # para cada linha, percorre cada coluna (0 até 3) = 16 comparações no total
        if matriz[i][j] > max_valor:  # compara o elemento atual com o maior encontrado até agora
            maior_linha = i           # registra em qual linha ele está
            maior_coluna = j          # registra em qual coluna ele está
            max_valor = matriz[i][j]  # atualiza o maior valor

print(f'O maior valor é da matriz é \n> {max_valor}')                          # imprime o maior número encontrado
print(f'Os indices do valor são\n> Linha: [{maior_linha}], Coluna: [{maior_coluna}]')  # imprime onde ele está na matriz
 