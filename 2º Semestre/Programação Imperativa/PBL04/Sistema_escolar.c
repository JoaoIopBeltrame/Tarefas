#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define QntArmazenamento 100

typedef struct
{
	int matricula; 
	float notaSemes;
	bool aprovado;
} InfoAluno;


void ler_dados_dos_estudantes(InfoAluno* ptrr);
void classificar(InfoAluno* ptrr);
void imprimir_relatorio(InfoAluno* ptrr);

int main(void)
{
	int quantidade = 3;
	InfoAluno* Estudante = malloc(3 * sizeof(InfoAluno));
	if (Estudante == NULL) 
	{
		puts("Memoria insuficiente\n");
		return 1;	
	}
	ler_dados_dos_estudantes(Estudante, quantidade);
	classificar(Estudante, quantidade);
	imprimir_relatorio(Estudante, quantidade);
	
	free(Estudante);
	Estudante = NULL;

	return 0;
}

void ler_dados_dos_estudantes(InfoAluno* ptrr, int quantidade)
{	
	for(int i = 0; i < quantiade; i++)
	{
		printf("Cadastro estudante %d", i + 1)
		printf("Matricula\n>> ");
		scanf("%d", &(ptrr + i)->matricula);

		printf("Nota\n>> ");
		scanf("%d", &(ptrr + i)->notaSemes);

	}
	
}

void classificar(InfoAluno* ptrr, int quantidade)
{
	for(int i = 0; i < quantidade; i++)
	{
		if((ptrr + i)->notaSemes >= 7)
		{
			(ptrr + i)->aprovado = true;
		}	
		else
		{
			(ptrr + i)->aprovado = false;
		}
	}
}

void imprimir_relatorio(InfoAluno* ptrr, int quantidade)
{
	puts("============================================\n");
	puts("           RELATÓRIO FINAL\n");
	puts("============================================\n");
	printf("%-12s %-15s %-15s\n", "Matrícula", "Nota", "Situação");
	puts("--------------------------------------------\n");
	
	for (int i = 0; i < quantidade; i++)
	{
		printf("%-12d %-15.2f %-15s\n",
		       (ptrr + i)->matricula,
		       (ptrr + i)->notaSemes,
		       (ptrr + i)->aprovado ? "Aprovado" : "Reprovado");
		   
	}
	puts("============================================\n");
