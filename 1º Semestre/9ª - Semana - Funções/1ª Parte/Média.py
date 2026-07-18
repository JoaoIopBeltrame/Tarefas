def calcular_media(notas):
    return sum(notas) / len(notas)

def perguntar_nota():
    return float(input('Digite a nota\n> '))

def main():
   x = perguntar_nota()
   y = perguntar_nota()
   z = perguntar_nota()
   
   media = calcular_media([x, y, z])
   print(f'A média é {media}')

if __name__ == "__main__":
    main()