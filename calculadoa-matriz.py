#escolhe operador primeiro pq a matriz tem que seguir a logica das regras
def valores_tamnho():
    while True:
        try:
        
            op = input("Operação (soma/subtração/multiplicação/divisao)\n> ").lower()
            l = int(input("Linhas\n> "))
            j = int(input("Colunas\n> "))
            return l, j, op  
        
        except ValueError:
            print("Digite valores inteiros")

def criar_matriz(l, j):
    matriz = [[0 for _ in range(j)] for _ in range(l)]
    return matriz

def pergunta_operacao(op):
    match op:
        case "soma":
            print("Soma escolhida")
            return lambda a, b: a + b
        case "subtração":
            print("Subtração escolhida")
            return lambda a, b: a - b
        case "divisao":
            print("Divisão escolhida")
            return lambda a, b: a / b
        case "multiplicação":
            print("Multiplicação escolhida")
            return lambda a, b: a * b
        case _:
            print("Comando desconhecido")
            return None
            
def preencherA(matrizA, nome="A"):
    for i in range(len(matrizA)):
        while True:
            try:
                valores = list(map(float, input(f"Digite os numeros da {i+1}ª linha")))
                if len(valores) != len(matrizA[0]):
                    print(f"Voce deve digitar somente {len(matrizA[0])}")
                    continue
                matrizA[i] = valores
                break
            except ValueError:
                print("Digite números válidos!")



def soma_matriz(matrizA, matrizB):
    return [
        [matrizA[i][j] + matrizB[i][j] for j in range(len(matrizA[0]))] for i in range(len(matrizA))
        ]

def subtracao_matriz():
    return [
        [matrizA[i][j] - matrizB[i][j] for j in range(len(matrizA[0]))] for i in range(len(matrizA))
        ]

def checa_pode(m1, m2):
    if m1[i][j] == m2[i][j]:
        return True
    else:
        return False

def main():
    pass

if __name__ == '__main__':
    main()
