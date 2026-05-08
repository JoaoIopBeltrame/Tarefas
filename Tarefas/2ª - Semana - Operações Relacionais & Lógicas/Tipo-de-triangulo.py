import time
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def triang_ret(numero_organizados):
    if numero_organizados[2] ** 2 == numero_organizados[1] ** 2 + numero_organizados[0] ** 2:
        print("O triangulo tambem é retangulo")
    else:
        print("Triangulo não é retangulo")
        limpar()

n1 = int(input("Digite o primeiro lado: "))
n2 = int(input("Digite o segundo lado: "))
n3 = int(input("Digite o terceiro lado: "))

lista_numeros = [n1, n2, n3]
maior_menor = sorted(lista_numeros)

print(f"{lista_numeros} foram os numeros digitados")
time.sleep(2)
limpar()

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print("ISSO É UM TRIANGULO")
    if n1 == n2 == n3:
        print("Tipo: Equilátero (todos iguais)")
        triang_ret(maior_menor)

    elif n1 == n2 or n1 == n3 or n2 == n3:
        print("Tipo: Isósceles (dois iguais)")
        triang_ret(maior_menor)

    else:
        print("Tipo: Escaleno (todos diferentes)")
        triang_ret(maior_menor)
else:
    print("Isso não e um triangulo")
    time.sleep(1.5)
    







