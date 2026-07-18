def colocar_numero():
    return int(input('Digite um nuero\n> '))

def main():
   x =  colocar_numero()
   y =  colocar_numero()
   z =  colocar_numero()
   
   if x >= y and x >= z:
    print(f'O numero {x} é o maior')
   elif y >= z and y >= x:
    print(f'O numero {y} é o maior')
   else:
    z >= y and z >= x
    print(f'O numero {z} é o maior')

    
if __name__ == "__main__":
    main()