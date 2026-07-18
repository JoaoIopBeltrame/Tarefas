import random

alfabeto = list("abcdefghijklmnopqrstuvwxyz")
random.shuffle(alfabeto)

for i, letra in enumerate(alfabeto):
    print(f"[{i:2}] {letra}", end="   ")
    if (i + 1) % 5 == 0:
        print()
print()

letra = random.choice(alfabeto)
palpite = int(input(f"Qual a posicao da letra '{letra}'? "))

if palpite == alfabeto.index(letra):
    print("Acertou!")
else:
    print(f"Errou! A posicao correta era {alfabeto.index(letra)}.")