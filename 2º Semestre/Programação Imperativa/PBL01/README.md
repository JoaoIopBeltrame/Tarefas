# Conversão e Divisão de Números com Ponteiros em C

Um programa desenvolvido em **C** para ler dois números de três dígitos, armazenando cada dígito individualmente como um caractere dentro de uma `struct`.

Após a leitura, o programa utiliza **ponteiros e conversão de caracteres ASCII** para transformar os dígitos em números inteiros. Em seguida, realiza a divisão entre os dois valores e apresenta o resultado com três casas decimais.

O programa também verifica se o segundo número é zero, evitando uma divisão inválida.

---

## Funcionalidades

* **Leitura de Dígitos:** Recebe três caracteres para cada número.
* **Uso de `struct`:** Armazena os dois conjuntos de caracteres dentro da estrutura `NumeroArray`.
* **Arrays de Caracteres:** Cada número é inicialmente armazenado em um array de três posições.
* **Uso de Ponteiros:** Ponteiros percorrem os arrays durante a conversão.
* **Conversão ASCII:** Transforma caracteres como `'5'` no número inteiro `5`.
* **Construção dos Números:** Os três dígitos são combinados para formar um único número inteiro.
* **Divisão com Casas Decimais:** Utiliza `float` para realizar a divisão.
* **Tratamento de Divisão por Zero:** Verifica se o segundo número é diferente de zero antes do cálculo.
* **Saída Formatada:** Exibe o resultado com três casas decimais.

---

## Tecnologias Utilizadas

* **Linguagem C**
* **Biblioteca Padrão:** `<stdio.h>`
* **Structs**
* **Arrays**
* **Ponteiros**
* **Aritmética de ponteiros**
* **Conversão ASCII**
* **Casting**
* **Laços `for`**
* **Condicionais**

---

## Código Completo

```c
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

    for (int i = 0; i < 3; i++)
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

        printf("Calculo: %d / %d = %.3f\n",
               n1, n2, resposta);
    }
    else
    {
        puts("Erro: Divisao por zero!\n");
    }

    return 0;
}
```

---

## Como Compilar e Executar

Para compilar utilizando o **GCC**, salve o código em um arquivo chamado:

```text
main.c
```

Depois execute:

```bash
gcc main.c -o divisor
```

### Windows

```bash
divisor.exe
```

### Linux / macOS

```bash
./divisor
```

---

## Estrutura `NumeroArray`

Os dígitos dos dois números são armazenados na seguinte estrutura:

```c
typedef struct
{
    char num1[3];
    char num2[3];
} NumeroArray;
```

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `num1` | `char[3]` | Armazena os três dígitos do primeiro número. |
| `num2` | `char[3]` | Armazena os três dígitos do segundo número. |

Por exemplo, para o número:

```text
527
```

o array armazena:

```text
num1
+-----+-----+-----+
| '5' | '2' | '7' |
+-----+-----+-----+
   0     1     2
```

Nesse momento, os valores são **caracteres**, e não o número inteiro `527`.

---

## Leitura dos Dígitos

A leitura do primeiro número é feita utilizando:

```c
for (int i = 0; i < 3; i++)
{
    scanf(" %c", numeroInpt.num1 + i);
}
```

A expressão:

```c
numeroInpt.num1 + i
```

representa o endereço da posição atual do array.

Ela é equivalente a:

```c
&numeroInpt.num1[i]
```

Portanto:

```text
numeroInpt.num1 + 0 → endereço de num1[0]
numeroInpt.num1 + 1 → endereço de num1[1]
numeroInpt.num1 + 2 → endereço de num1[2]
```

O mesmo processo é realizado para `num2`.

---

## Uso dos Ponteiros

Depois da leitura, são criados dois ponteiros:

```c
char *pNum1 = numeroInpt.num1;
char *pNum2 = numeroInpt.num2;
```

Inicialmente, `pNum1` aponta para a primeira posição:

```text
 pNum1
   |
   v
+-----+-----+-----+
| '5' | '2' | '7' |
+-----+-----+-----+
```

Quando o programa executa:

```c
pNum1++;
```

o ponteiro avança para a próxima posição:

```text
       pNum1
         |
         v
+-----+-----+-----+
| '5' | '2' | '7' |
+-----+-----+-----+
```

Dessa maneira, o ponteiro percorre os três caracteres.

---

## Conversão de Caractere para Número

Cada posição contém inicialmente um caractere.

Por exemplo:

```c
'5'
```

Para obter o valor inteiro `5`, o programa utiliza:

```c
int digito = *pNum1 - '0';
```

Isso funciona porque os caracteres numéricos possuem valores consecutivos na codificação utilizada pela linguagem.

Assim:

```text
'0' - '0' = 0
'1' - '0' = 1
'2' - '0' = 2
...
'9' - '0' = 9
```

Portanto:

```c
*pNum1 - '0'
```

converte o caractere apontado para seu valor numérico.

---

## Construção do Número Inteiro

Depois de converter cada caractere, o programa precisa juntar os dígitos.

Isso é feito com:

```c
n1 = (n1 * 10) + digito;
```

Por exemplo, para:

```text
'5' '2' '7'
```

inicialmente:

```text
n1 = 0
```

### Primeiro dígito

```text
digito = 5

n1 = (0 × 10) + 5
n1 = 5
```

### Segundo dígito

```text
digito = 2

n1 = (5 × 10) + 2
n1 = 52
```

### Terceiro dígito

```text
digito = 7

n1 = (52 × 10) + 7
n1 = 527
```

Resultado:

```text
'5' '2' '7'
      ↓
     527
```

O mesmo processo é realizado para `num2`.

---

## Divisão dos Números

Depois das conversões, o programa possui dois números inteiros:

```c
int n1;
int n2;
```

Antes da divisão é feita a verificação:

```c
if (n2 != 0)
```

Se o segundo número for diferente de zero, o cálculo é realizado:

```c
float resposta = (float)n1 / (float)n2;
```

O casting:

```c
(float)
```

transforma os valores em números de ponto flutuante antes da divisão.

Por exemplo:

```text
125 / 100
```

produz:

```text
1.250
```

---

## Tratamento de Divisão por Zero

Uma divisão por zero não é uma operação válida.

Por isso o programa verifica:

```c
if (n2 != 0)
```

Caso:

```text
n2 = 0
```

é executado:

```c
puts("Erro: Divisao por zero!\n");
```

Por exemplo, se o usuário informar:

```text
num2 = 000
```

a saída será:

```text
Erro: Divisao por zero!
```

---

## Saída Formatada

O resultado é exibido utilizando:

```c
printf("Calculo: %d / %d = %.3f\n",
       n1, n2, resposta);
```

Onde:

```text
%d
```

representa os números inteiros.

Já:

```text
%.3f
```

exibe o resultado da divisão com exatamente **três casas decimais**.

---

## Exemplo de Uso

### Entrada

```text
Digite os primeiros 3 numeros (num1):
1
2
0

Digite os outros 3 numeros (num2):
0
4
0
```

Os arrays armazenam:

```text
num1 = ['1', '2', '0']
num2 = ['0', '4', '0']
```

Após a conversão:

```text
n1 = 120
n2 = 40
```

O cálculo realizado será:

```text
120 / 40
```

### Saída

```text
Calculo: 120 / 40 = 3.000
```

---

## Fluxo do Programa

```text
main
 │
 ├── cria NumeroArray
 │
 ├── lê os 3 caracteres de num1
 │
 ├── lê os 3 caracteres de num2
 │
 ├── cria pNum1
 │      │
 │      └── percorre num1
 │             │
 │             ├── converte caractere para dígito
 │             └── constrói n1
 │
 ├── cria pNum2
 │      │
 │      └── percorre num2
 │             │
 │             ├── converte caractere para dígito
 │             └── constrói n2
 │
 ├── verifica n2
 │      │
 │      ├── n2 != 0 → realiza a divisão
 │      │
 │      └── n2 == 0 → exibe erro
 │
 └── return 0
```

---

## Complexidade

Como cada número possui exatamente três caracteres, os dois laços de conversão executam sempre três vezes.

Neste programa específico:

```text
Tempo: O(1)
Memória: O(1)
```

Isso ocorre porque a quantidade de dados processados é fixa.

---

# PROPOSTA

<!-- Coloque aqui as imagens da proposta/exercício -->

<img width="423" height="527" alt="image" src="https://github.com/user-attachments/assets/a11163f3-7e51-41c0-9b21-09d27005599e" />

<img width="426" height="482" alt="image" src="https://github.com/user-attachments/assets/4b837415-8388-4323-87a6-77597834cd4f" />

