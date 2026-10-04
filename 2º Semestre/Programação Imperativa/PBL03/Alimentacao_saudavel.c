#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int qntFrutas;
    int qntTurmas;
    int *pesquisa;
} InfoEscola;

void ler_dados(InfoEscola *ptrr);
long long calcular_alunos(InfoEscola *ptrr);

int main(void)
{
    InfoEscola Escola;

    scanf("%d %d", &Escola.qntFrutas, &Escola.qntTurmas);

    Escola.pesquisa = malloc(
        Escola.qntFrutas * Escola.qntTurmas * sizeof(int)
    );

    if (Escola.pesquisa == NULL)
    {
        puts("Memoria insuficiente");
        return 1;
    }

    ler_dados(&Escola);

    long long totalAlunos = calcular_alunos(&Escola);

    printf("%lld\n", totalAlunos);

    free(Escola.pesquisa);
    Escola.pesquisa = NULL;

    return 0;
}

void ler_dados(InfoEscola *ptrr)
{
    for (int i = 0; i < ptrr->qntFrutas; i++)
    {
        for (int j = 0; j < ptrr->qntTurmas; j++)
        {
            scanf("%d",
                  &ptrr->pesquisa[i * ptrr->qntTurmas + j]);
        }
    }
}

long long calcular_alunos(InfoEscola *ptrr)
{
    long long totalAlunos = 0;

    for (int i = 0; i < ptrr->qntTurmas; i++)
    {
        int maior = 0;

        for (int j = 0; j < ptrr->qntFrutas; j++)
        {
            int valor = ptrr->pesquisa[
                j * ptrr->qntTurmas + i
            ];

            if (valor > maior)
            {
                maior = valor;
            }
        }

        if (maior == 0)
        {
            maior = 1;
        }

        totalAlunos += maior;
    }

    return totalAlunos;
}
