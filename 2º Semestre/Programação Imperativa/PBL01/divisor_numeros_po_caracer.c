#include <stdio.h>

typedef struct
{
    char num1[3];
    char num2[3];
} NumeroArray;

int main(void)
{
    NumeroArray numeroInpt;

    puts("Digite os primeiros 3 numeros (num1):");
    for (int i = 0; i < 3; i++)
    {
        scanf(" %c", numeroInpt.num1 + i);
    }

    puts("Digite os outros 3 numeros (num2):");
    for (int i = 0; i < 3; i++)
    {
        scanf(" %c", numeroInpt.num2 + i);
    }

    int n1 = 0;
    char *pNum1 = numeroInpt.num1; 
    {
        int digito = *pNum1 - '0';
        n1 = (n1 * 10) + digito;
        pNum1++; 
    }

    int n2 = 0;
    char *pNum2 = numeroInpt.num2; 
    for (int i = 0; i < 3; i++)
    {
        int digito = *pNum2 - '0';
        n2 = (n2 * 10) + digito; 
        pNum2++; 
    }

    if (n2 != 0)
    {
        float resposta = (float)n1 / (float)n2;
        printf("\nCalculo: %d / %d = %.3f\n", n1, n2, resposta);
    }
    else
    {
        puts("\nErro: Divisao por zero!");
    }

    return 0;
}
