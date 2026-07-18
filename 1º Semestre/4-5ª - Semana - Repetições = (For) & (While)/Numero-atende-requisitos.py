requisitos = []
requisitos_false = []
for numero in range(1, 101):
    if (numero % 3 == 0) and (numero % 5 != 0):
        requisitos.append(numero)
    
    else:
        requisitos_false.append(numero)

print(f'{len(requisitos)} numeros atenderam ao requisitos')
print(requisitos)
print(f'{len(requisitos_false)} numeros nao atenderam ao requisitos')
print(requisitos_false)
