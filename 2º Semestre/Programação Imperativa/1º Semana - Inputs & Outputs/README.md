```markdown
# Leitor e Divisor de Números em C

Um programa em C desenvolvido para ler caracteres individuais via entrada padrão, convertê-los em números inteiros de 3 dígitos utilizando aritmética ASCII e realizar uma operação segura de divisão com formatação de saída de ponto flutuante.

---

## Funcionalidades

* **Leitura Segura:** Utiliza `fgets` junto com a biblioteca `<string.h>` para capturar a entrada do usuário de forma segura através de um buffer temporário.
* **Leitura com Ponteiros:** Armazena múltiplos caracteres inseridos utilizando um array de ponteiros (`char*`).
* **Conversão ASCII:** Converte caracteres numéricos (`'0'` a `'9'`) em seus respectivos valores inteiros utilizando subtrações baseadas na tabela ASCII.
* **Tratamento de Erros:** Previne falhas de execução ao verificar se o divisor é zero antes de efetuar a operação matemática.
* **Saída Formatada:** Exibe o resultado da divisão com precisão de três casas decimais (`%.3f`).

---

## Tecnologias Utilizadas

* **Linguagem C** (Padrão C99 ou superior)
* **Biblioteca Padrão:** `<stdio.h>`, `<string.h>`

---

## Código Completo

```c
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
    char buffer[10]; // não 6 pois o fgets guarda o \n e \0
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

```

---

## Como Compilar e Executar

Siga os passos abaixo para compilar e executar o código em sua máquina utilizando o **GCC**:

1. Clone o repositório ou salve o código em um arquivo chamado `main.c`.
2. Abra o terminal na pasta do arquivo e execute o comando de compilação:

```bash
gcc main.c -o programa

```

3. Execute o programa gerado:

```bash
./programa

```

---

## Exemplo de Uso

O programa espera que você insira os caracteres correspondentes. Os três primeiros formarão o primeiro número e os três últimos formarão o segundo número.

**Entrada:**

```text
120040

```

*(Isso equivale a dividir 120 por 040, ou seja, 120 / 40)*

**Saída:**

```text
3.000

```

---

## Estrutura do Código

| Função | Tipo de Retorno | Descrição |
| --- | --- | --- |
| `main` | `int` | Função principal que gerencia o fluxo e chamadas do programa. |
| `pegar_char` | `void` | Lê os caracteres da entrada usando `fgets` e os distribui por ponteiros. |
| `char_numero` | `int` | Converte três caracteres em um único número inteiro de 3 dígitos via aritmética ASCII. |
| `divisao` | `void` | Realiza a divisão entre os números e imprime o resultado formatado. |

---

# **PROPOSTA**
<img width="755" height="902" alt="imagem" src="https://github.com/user-attachments/assets/a1e5d8f6-ab77-4b00-a486-63e8d9f48336" />
<img width="771" height="792" alt="imagem" src="https://github.com/user-attachments/assets/bd2b6e68-8f9d-45ea-82b6-75d8aa1f23f8" />
---


