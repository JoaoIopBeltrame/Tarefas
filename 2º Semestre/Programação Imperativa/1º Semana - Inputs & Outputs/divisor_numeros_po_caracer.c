#include <stdio.h>
#include <string.h>

void pegar_char(char* num[6]);
int char_numero(char n1, char n2, char n3);
void divisao(int num1, int num2, float* resposta);
int main()
{
    
    char n1, n2, n3, n4, n5, n6;
    float resposta;

    char* todos_char[6] = {&n1, &n2, &n3,
                &n4, &n5, &n6};
    
    pegar_char(todos_char);
    
    int num1 = char_numero(n1, n2, n3);
    int num2 = char_numero(n4, n5, n6);
    
    if (num2 != 0){
        divisao(num1, num2, &resposta);
        return 0;
    }
    printf("Erro: Divisão por zero.\n");
}

void pegar_char(char* num[6])
{
    char buffer[10]; // nao  6 pq o fgets vai guardar o \n e \0
    if (fgets(buffer, sizeof(buffer), stdin) != NULL) {
        buffer[strcspn(buffer, "\n")] = '\0';
        for (int i = 0; i < 6; i++) {
            *num[i] = buffer[i];
        }
    }
}
int char_numero(char n1, char n2, char n3)
{
    return (n1 - '0')*100 + (n2 - '0')*10 + (n3 - '0');
}
void divisao(int num1, int num2, float* resposta)
{
    *resposta = (float)num1 / (float)num2;
    printf("%.3f\n", *resposta);
}


//     ASCII   NUM      
//      48	   	0 	    
//      49	   	1 	    
//      50	   	2 	    
//      51	   	3 	    
//      52	   	4 	      
//      53	   	5 	    
//      54	   	6 	    
//      55	   	7 	    
//      56	   	8 	    
//      57	   	9 	    
