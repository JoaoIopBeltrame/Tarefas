matriz = []
for aluno in range(5):
    matricula = int(input('Digite a matrícula\n> '))
    provas = []
    while True:
        entrada = input(f'Digite a {len(provas) + 1}ª nota de prova (ou "c" para encerrar)\n> ')
        if entrada == 'c':
            break
        provas.append(int(entrada))
    media_provas = sum(provas) / len(provas)
    trabalhos = []
    while True:
        entrada = input(f'Digite a {len(trabalhos) + 1}ª nota de trabalho (ou "c" para encerrar)\n> ')
        if entrada == 'c':
            break
        trabalhos.append(int(entrada))
    media_trabalhos = sum(trabalhos) / len(trabalhos)
    nota_final = media_provas + media_trabalhos
    matriz.append([matricula, media_provas, media_trabalhos, nota_final])

for linha in matriz:
    print(linha)

maior = matriz[0]
for linha in matriz:
    if linha[3] > maior[3]:
        maior = linha
print(f'Matrícula com maior nota: {maior[0]}')