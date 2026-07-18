def inverter(frase):
    return frase[::-1]

def digitar_string():
    return input('Digite uma frase\n> ')
    
def main():
    print(inverter(digitar_string()))

if __name__ == '__main__':
    main()