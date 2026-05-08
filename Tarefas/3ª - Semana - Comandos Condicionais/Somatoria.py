while True:
    numero = input("Digite um número (ou 'sair')\n> ").strip()
    if numero.lower() == "sair":
        print("Encerrando...")
        break
    try:
        numero_int = int(numero)
        soma = 0
        for i in range(numero_int, 0, -1):
            soma += i
        print(f"Soma: {soma}")

    except:
        print("Digite apenas números inteiros!")
