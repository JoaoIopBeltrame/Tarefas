#include <stdio.h>

#define MAX_REF 1000 

typedef struct
{
    int temp_deSono; // T
    int duracaoVoo;  // D
    int qntRefeicao; // M
    int horaRefe[MAX_REF]; // H ref
} InfoVoo;

void lerInpt(InfoVoo *ptrr);
void lerComida(InfoVoo *ptrr);
void retorYorN(InfoVoo *ptrr);

int main(void)
{
    InfoVoo Katmanu;
    puts("Digite primeiro |TEMPO DE SONO| |DURACAO DO VOO| |QUANTAS REFEICOES TERAO|\n");
    lerInpt(&Katmanu);
    puts("Digite os horarios de refeicao\n");
    lerComida(&Katmanu);
    retorYorN(&Katmanu);         

    return 0;
}

void lerInpt(InfoVoo *ptrr)
{
    scanf("%d %d %d", &ptrr->temp_deSono, &ptrr->duracaoVoo, &ptrr->qntRefeicao);
}

void lerComida(InfoVoo *ptrr)
{
    for (int i = 0; i < ptrr->qntRefeicao; i++)    {
        scanf(" %d", ptrr->horaRefe + i);
    }
}

void retorYorN(InfoVoo *ptrr)
{
    int detGap = 0;
    int* pRef = ptrr->horaRefe;
    int* pRefSob = ptrr->horaRefe + ptrr->qntRefeicao;
                                               
    for (int i = 0; i <= ptrr->duracaoVoo; i++)   
    {
        if (pRef < pRefSob && i == * pRef)
        {
            detGap = i;
            pRef++; 
        }
        else if (i - detGap == ptrr->temp_deSono)
        {
            puts("Y");
            return;                             
        }
    }
    puts("N");
    return;
}
