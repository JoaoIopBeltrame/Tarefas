def operacao(ma, mb, verRegras=None):
    op = input("Digite a operação das matrizes\n> ") #especificar
    if op == "soma":
        if (len(ma) and len(ma[0])) == (len(mb) and len(mb[0])):
            print("Metodo: Soma")
            return lambda ma, mb: ma + mb
        while True:
            verInfo = input("Não é possivel somar matrizes. Pressione ENTER para ver as regras em geral das matrizes\n> ")
            match verInfo:
                case "":
                    return verRegras
                    break
                case _:
                    print("Vai ver as regras meu fi")
                    continue

def definirMatrizA():
    while True:
        try:
            l = int(input("Diite uantas linhas a matriz deve ter\n> "))
            j = int(input("Diite uantas colunas a matriz deve ter\n> "))
            
            mA = [[0 for co in range(j)] for lin in range(l)]
        except ValueError:
            print("Digite um numero inteiro")
        return mA

def definirMatrizB():
    while True:
        try:
            l = int(input("Diite uantas linhas a matriz deve ter\n> "))
            j = int(input("Diite uantas colunas a matriz deve ter\n> "))
            
            mB = [[0 for co in range(j)] for lin in range(l)]
        except ValueError:
            print("Digite um numero inteiro")
        return mB

def matrizMenos(mA, mB, valorI, valorJ): #colocar dentro do main e o inpt de quantoQUANTO vai colocar o valor dentro disso
    if len(mA[valorI][valorJ]) == len(mB[valorI][valorJ]):
        return [
            [mA[valorI][valorJ] - mB[valorI][valorJ] for _ in range(len(mA[0]))
            ] for _ in range(len(mA))  
        ]
    print("As matrizes devem ser de tamanhosiguais")
    return None



def matrizSoma():
    pass

def main():
    mA = definirMatrizA()
    print(f"=====A=====")
    print(*mA, sep="\n")
    mB = definirMatrizB()
    print(f"=====B=====")
    print(*mB, sep="\n")
    print(operacao(mA, mB))

    

if __name__ == '__main__':
    main()

















# #escolhe operador primeiro pq a matriz tem que seguir a logica das regras
# def opcao():
#     print(f'''
#     1 - Soma (matriz devem ter linhas e colunas iguais)
#     2 - subtração (matriz devem ter linhas e colunas iguais)
#     3 - Multiplicação (número de colunas da primeira matriz for igual ao número de linhas da segunda matriz)
#     4 - vou escrever ainda
#     ''')
    
# def valores_tamnho():
#     while True:
#         try:
        
#             op = input("Operação (soma/subtração/multiplicação/divisao)\n> ").lower().strip()
#             l = int(input("Linhas\n> "))
#             j = int(input("Colunas\n> "))
            
#             return l, j, op  
        
#         except ValueError:
#             print("Digite valores inteiros")

# def criar_matriz(l, j):
#     matriz = [[0 for _ in range(j)] for _ in range(l)]
#     return matriz

# def pergunta_operacao(op): # op vai ser um um input dentro do main
#     match op:
#         case "soma":
#             print("Soma escolhida")
#             return lambda a, b: a + b
#         case "subtração":
#             print("Subtração escolhida")
#             return lambda a, b: a - b
#         case "divisao":
#             print("Divisão escolhida")
#             return lambda a, b: a / b
#         case "multiplicação":
#             print("Multiplicação escolhida")
#             return lambda a, b: a * b
#         case _:
#             print("Comando desconhecido")
#             return None
            


# def preencherB(matrizB, nome="B"):
#     for i in range(len(matrizB)):
#         while True:
#             try:
#                 valores = list(map(float, input(f"Digite os numeros da {i+1}ª linha")))
#                 if len(valores) != len(matrizB[0]):
#                     print(f"Voce deve digitar somente {len(matrizB[0])}")
#                     continue
#                 matrizB[i] = valores
#                 break
#             except ValueError:
#                 print("Digite números válidos!")




# def soma_matriz(matrizA, matrizB):
#     return [
#         [matrizA[i][j] + matrizB[i][j] for j in range(len(matrizA[0]))] for i in range(len(matrizA))
#         ]

# def subtracao_matriz():
#     return [
#         [matrizA[i][j] - matrizB[i][j] for j in range(len(matrizA[0]))] for i in range(len(matrizA))
#         ]


# #tentarpor isso dentro das proprias matrizes 
# def checa_pode(m1, m2):
#     if m1[i][j] == m2[i][j]:
#         return True
#     else:
#         return False

# def main():
#     pass

# if __name__ == '__main__':
#     main()
