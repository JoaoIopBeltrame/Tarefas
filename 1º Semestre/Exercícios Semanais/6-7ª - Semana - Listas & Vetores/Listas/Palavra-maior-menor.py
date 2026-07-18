palavras = []
for i in range(4):
    palavras.append(input("Palavra: "))

print(f"Mais longa: {max(palavras, key=len)}")
print(f"Mais curta: {min(palavras, key=len)}")