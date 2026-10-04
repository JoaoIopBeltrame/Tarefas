# Problema A - Achando os Monótonos Não-Triviais Maximais em C

Um programa desenvolvido em **C** para analisar uma sequência composta pelos caracteres `a` e `b` e determinar quantos caracteres `a` pertencem a **trechos monótonos maximais não-triviais**.

Um trecho é considerado **monótono** quando todos os seus caracteres são iguais. Ele é **não-trivial** quando possui pelo menos dois caracteres e é **maximal** quando não pode ser aumentado para a esquerda ou para a direita mantendo os mesmos caracteres.

---

## Funcionalidades

* **Leitura dos Dados:** Recebe o tamanho da sequência e a string formada por `a` e `b`.
* **Uso de `struct`:** Armazena o tamanho e a sequência dentro da estrutura `InfoSequencia`.
* **Alocação Dinâmica:** Utiliza `malloc` para reservar memória de acordo com o tamanho informado.
* **Uso de Ponteiros:** As funções recebem um ponteiro para a estrutura.
* **Detecção de Sequências:** Identifica grupos consecutivos formados pelo caractere `a`.
* **Verificação de Trechos Não-Triviais:** Considera apenas grupos que possuem pelo menos dois caracteres.
* **Contagem dos Caracteres:** Soma todos os `a` pertencentes aos trechos encontrados.
* **Liberação de Memória:** Utiliza `free` ao final da execução.

---

## Tecnologias Utilizadas

* **Linguagem C**
* **Bibliotecas Padrão:** `<stdio.h>`, `<stdlib.h>`
* **Structs**
* **Strings**
* **Ponteiros**
* **Alocação dinâmica com `malloc`**
* **Funções**
* **Laços `for` e `while`**
* **Condicionais**

---

## Código Completo

```c
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
```

---

## Como Compilar e Executar

Para compilar o programa utilizando o **GCC**, salve o código em um arquivo chamado `main.c`.

No terminal, execute:

```bash
gcc main.c -o monotonos
```

Depois execute o programa:

### Linux / macOS

```bash
./monotonos
```

### Windows

```bash
monotonos.exe
```

---

## Entrada

A entrada possui duas linhas.

A primeira contém um número inteiro:

```text
N
```

Onde `N` representa a quantidade de caracteres da sequência.

A segunda linha contém uma string com exatamente `N` caracteres, formada apenas por:

```text
a
b
```

Exemplo:

```text
10
aababaaabb
```

---

## Saída

O programa imprime a quantidade total de caracteres `a` que pertencem a trechos monótonos maximais não-triviais.

Exemplo:

```text
5
```

---

## Exemplo de Uso

### Entrada

```text
10
aababaaabb
```

A sequência pode ser separada em seus trechos consecutivos:

```text
aa | b | a | b | aaa | bb
```

Os trechos formados por `a` são:

```text
aa
a
aaa
```

O trecho:

```text
a
```

possui apenas um caractere e, portanto, é **trivial**.

Os trechos não-triviais são:

```text
aa
aaa
```

Assim:

```text
2 + 3 = 5
```

### Saída

```text
5
```

---

## Outros Exemplos

### Exemplo 1

Entrada:

```text
7
abababa
```

Todos os caracteres `a` aparecem isoladamente:

```text
a | b | a | b | a | b | a
```

Nenhum trecho de `a` possui pelo menos dois caracteres.

Saída:

```text
0
```

### Exemplo 2

Entrada:

```text
10
bbaababaaa
```

Os trechos podem ser separados como:

```text
bb | aa | b | a | b | aaa
```

Os trechos não-triviais formados por `a` são:

```text
aa
aaa
```

Portanto:

```text
2 + 3 = 5
```

Saída:

```text
5
```

---

## Estrutura do Código

| Função | Tipo de Retorno | Descrição |
| --- | --- | --- |
| `main` | `int` | Controla o fluxo principal, realiza a alocação e libera a memória. |
| `ler_dados` | `void` | Lê e armazena a sequência de caracteres. |
| `contar_a_monotonos` | `int` | Encontra os trechos consecutivos de `a` e retorna a quantidade pertencente aos trechos não-triviais. |

---

## Estrutura `InfoSequencia`

As informações utilizadas pelo programa são armazenadas na estrutura:

```c
typedef struct
{
    int tamanho;
    char *sequencia;
} InfoSequencia;
```

| Campo | Tipo | Significado |
| --- | --- | --- |
| `tamanho` | `int` | Quantidade de caracteres da sequência (`N`). |
| `sequencia` | `char *` | Ponteiro para a memória onde a string é armazenada. |

---

## Alocação Dinâmica

Como o tamanho da string é informado durante a execução, o programa utiliza:

```c
Sequencia.sequencia = malloc(
    (Sequencia.tamanho + 1) * sizeof(char)
);
```

É necessário reservar:

```text
N + 1
```

posições.

A posição adicional é necessária por causa do caractere especial:

```text
\0
```

que indica o final de uma string em C.

Por exemplo:

```text
N = 5

String:
a a b b a

Memória:
[a][a][b][b][a][\0]
```

Depois de utilizar a memória, o programa executa:

```c
free(Sequencia.sequencia);
Sequencia.sequencia = NULL;
```

---

## Lógica da Verificação

A função:

```c
int contar_a_monotonos(InfoSequencia *ptrr)
```

percorre a sequência utilizando:

```c
for (int i = 0; i < ptrr->tamanho;)
```

Quando encontra um `a`:

```c
if (ptrr->sequencia[i] == 'a')
```

é criado um contador:

```c
int quantidadeA = 0;
```

Em seguida, o programa continua avançando enquanto encontrar caracteres `a` consecutivos:

```c
while (i < ptrr->tamanho &&
       ptrr->sequencia[i] == 'a')
{
    quantidadeA++;
    i++;
}
```

Por exemplo:

```text
aaa
^^^
```

resulta em:

```text
quantidadeA = 3
```

Depois é verificado se o trecho é não-trivial:

```c
if (quantidadeA >= 2)
```

Caso seja, todos os caracteres desse trecho são adicionados ao total:

```c
totalA += quantidadeA;
```

---

## Trechos Triviais e Não-Triviais

Um trecho com apenas um elemento é considerado **trivial**:

```text
a
```

Portanto:

```text
quantidadeA = 1
```

não é contabilizado.

Já:

```text
aa
```

possui:

```text
quantidadeA = 2
```

e é contabilizado.

Da mesma forma:

```text
aaaa
```

possui:

```text
quantidadeA = 4
```

e todos os quatro caracteres são adicionados ao resultado.

---

## Complexidade

Cada caractere da sequência é analisado uma única vez.

Portanto:

```text
Complexidade de tempo: O(N)
```

Como a sequência inteira é armazenada na memória:

```text
Complexidade de memória: O(N)
```

O limite fornecido pelo problema é:

```text
N <= 100000
```

---

# PROPOSTA

<!-- Coloque aqui as imagens da proposta -->

<img width="434" height="481" alt="image" src="https://github.com/user-attachments/assets/62ff88b2-70d5-460a-8440-0543ec935d82" />

## Enunciado Original

**Problema A — Achando os Monótonos Não-Triviais Maximais**

Maratona de Programação da SBC – ICPC – 2022.
