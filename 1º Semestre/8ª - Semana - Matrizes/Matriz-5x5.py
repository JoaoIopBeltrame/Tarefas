matriz = []         # criei uma matriz vazia para conseguir armazenar a 'linha' que tera os 1 e 0 e uso o append para armazenar
for l in range(5):  # criar um for loop, a cada loop lsita vazia chamada linha é criada
    linha = []
    for c in range(5): # para a coluna a cada 1 loop de L 5 loops ocorrem dentro do C
        if l == c:      # aqui funciona no incio os 2 loops vao estar com 5 depois o L loop vai estar 4 e o C 5 até 1 ai caso o loop L seja igual ao loop C vai aparecer o 1 nessa coordenada, a mesma coisa acontece com o 0 
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)   # armazenar todos os valores dentro da lista Matriz, ela ficara todo reta na mesma linha
for linha in matriz:   #para cada linha esse caso 5 que estiverem armazendadas dentro da matriz é usado o print() pq ele temm o break '\n'
    print(linha)
    