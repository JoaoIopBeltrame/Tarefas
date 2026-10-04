#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int tamanho;
    char *sequencia;
} InfoSequencia;

void ler_dados(InfoSequencia *ptrr);
int contar_a_monotonos(InfoSequencia *ptrr);

int main(void)
{
    InfoSequencia Sequencia;

    scanf("%d", &Sequencia.tamanho);

    Sequencia.sequencia = malloc(
        (Sequencia.tamanho + 1) * sizeof(char)
    );

    if (Sequencia.sequencia == NULL)
    {
        puts("Memoria insuficiente");
        return 1;
    }

    ler_dados(&Sequencia);

    int totalA = contar_a_monotonos(&Sequencia);

    printf("%d\n", totalA);

    free(Sequencia.sequencia);
    Sequencia.sequencia = NULL;

    return 0;
}

void ler_dados(InfoSequencia *ptrr)
{
    scanf("%s", ptrr->sequencia);
}

int contar_a_monotonos(InfoSequencia *ptrr)
{
    int totalA = 0;

    for (int i = 0; i < ptrr->tamanho;)
    {
        if (ptrr->sequencia[i] == 'a')
        {
            int quantidadeA = 0;

            while (i < ptrr->tamanho &&
                   ptrr->sequencia[i] == 'a')
            {
                quantidadeA++;
                i++;
            }

            if (quantidadeA >= 2)
            {
                totalA += quantidadeA;
            }
        }
        else
        {
            i++;
        }
    }

    return totalA;
}
