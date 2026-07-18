def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return None
    return a / b

def mostrar_menu():
    print('\n===== Calculadora =====')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('5 - Sair')

def pegar_numeros():
    a = float(input('Primeiro número: '))
    b = float(input('Segundo número: '))
    return a, b

def main():
    while True:
        mostrar_menu()
        opcao = input('Escolha: ')

        if opcao == '5':
            print('Tchau!')
            break

        if opcao not in ('1', '2', '3', '4'):
            print('Opção inválida')
            continue

        try:
            a, b = pegar_numeros()
        except ValueError:
            print('Digite apenas números')
            continue

        if opcao == '1':
            resultado = somar(a, b)
        elif opcao == '2':
            resultado = subtrair(a, b)
        elif opcao == '3':
            resultado = multiplicar(a, b)
        else:
            resultado = dividir(a, b)
            if resultado is None:
                print('Não dá pra dividir por zero')
                continue

        print(f'Resultado: {resultado}')

if __name__ == '__main__':
    main()