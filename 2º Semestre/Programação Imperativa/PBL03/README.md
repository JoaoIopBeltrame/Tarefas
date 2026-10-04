# Problema A - Alimentação Saudável — Cálculo do Número Mínimo de Alunos em C

Um programa desenvolvido em **C** para determinar o **menor número possível de alunos em uma escola**, utilizando os resultados de uma pesquisa sobre preferência por frutas.

A escola possui **N tipos de frutas** e **M turmas**. Para cada fruta, é informado quantos alunos de cada turma gostam dela. Como um mesmo aluno pode gostar de várias frutas, o programa encontra o maior valor registrado em cada turma e utiliza esses valores para calcular a quantidade mínima possível de alunos na escola.

---

## Funcionalidades

* **Leitura dos Dados:** Recebe a quantidade de frutas, a quantidade de turmas e os resultados da pesquisa.
* **Uso de `struct`:** Armazena as informações da escola dentro da estrutura `InfoEscola`.
* **Alocação Dinâmica:** Utiliza `malloc` para reservar memória de acordo com a quantidade de frutas e turmas.
* **Uso de Ponteiros:** As funções recebem um ponteiro para a estrutura, permitindo acessar seus dados diretamente.
* **Matriz em Memória Linear:** Os valores da pesquisa são armazenados em um vetor alocado dinamicamente.
* **Análise por Turma:** Percorre todas as frutas de cada turma procurando o maior valor.
* **Quantidade Mínima:** Considera o maior número registrado em cada turma como a quantidade mínima possível de alunos.
* **Tratamento de Turmas Vazias:** Caso todos os valores de uma turma sejam `0`, considera pelo menos `1` aluno.
* **Liberação de Memória:** Utiliza `free` após o término do processamento.

---

## Tecnologias Utilizadas

* **Linguagem C**
* **Bibliotecas Padrão:** `<stdio.h>`, `<stdlib.h>`
* **Structs**
* **Ponteiros**
* **Alocação dinâmica com `malloc`**
* **Arrays em memória dinâmica**
* **Funções**
* **Laços de repetição**

---

## Código Completo

```c
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
```

---

## Como Compilar e Executar

Para compilar o programa utilizando o **GCC**, salve o código em um arquivo chamado `main.c`.

No terminal, execute:

```bash
gcc main.c -o alimentacao
```

Depois execute o programa:

### Linux / macOS

```bash
./alimentacao
```

### Windows

```bash
alimentacao.exe
```

---

## Entrada

A primeira linha contém dois números inteiros:

```text
N M
```

Onde:

* `N` representa a quantidade de tipos de frutas.
* `M` representa a quantidade de turmas.

As próximas `N` linhas contêm `M` números inteiros.

Cada valor representa quantos alunos de determinada turma gostam daquela fruta.

Por exemplo:

```text
3 3
20 15 14
12 20 12
18 5 10
```

representa:

| Fruta | Turma 1 | Turma 2 | Turma 3 |
| --- | ---: | ---: | ---: |
| Fruta 1 | 20 | 15 | 14 |
| Fruta 2 | 12 | 20 | 12 |
| Fruta 3 | 18 | 5 | 10 |

---

## Exemplo de Uso

### Entrada

```text
3 3
20 15 14
12 20 12
18 5 10
```

Para a primeira turma:

```text
20
12
18
```

O maior valor é:

```text
20
```

Para a segunda turma:

```text
15
20
5
```

O maior valor é:

```text
20
```

Para a terceira turma:

```text
14
12
10
```

O maior valor é:

```text
14
```

Portanto:

```text
20 + 20 + 14 = 54
```

### Saída

```text
54
```

---

## Segundo Exemplo

### Entrada

```text
2 3
5 2 4
4 3 6
```

Os maiores valores de cada turma são:

```text
Turma 1 = 5
Turma 2 = 3
Turma 3 = 6
```

Portanto:

```text
5 + 3 + 6 = 14
```

### Saída

```text
14
```

---

## Estrutura do Código

| Função | Tipo de Retorno | Descrição |
| --- | --- | --- |
| `main` | `int` | Controla o fluxo principal, realiza a alocação e libera a memória. |
| `ler_dados` | `void` | Lê os resultados da pesquisa e os armazena na memória alocada. |
| `calcular_alunos` | `long long` | Calcula e retorna o menor número possível de alunos na escola. |

---

## Estrutura `InfoEscola`

As informações utilizadas pelo programa são armazenadas em uma única estrutura:

```c
typedef struct
{
    int qntFrutas;
    int qntTurmas;
    int *pesquisa;
} InfoEscola;
```

| Campo | Significado |
| --- | --- |
| `qntFrutas` | Quantidade de tipos diferentes de frutas (`N`). |
| `qntTurmas` | Quantidade de turmas da escola (`M`). |
| `pesquisa` | Ponteiro para a região de memória que armazena os resultados da pesquisa. |

---

## Alocação Dinâmica

A memória necessária para armazenar a pesquisa depende dos valores de `N` e `M`.

Por isso, o programa utiliza:

```c
Escola.pesquisa = malloc(
    Escola.qntFrutas * Escola.qntTurmas * sizeof(int)
);
```

A quantidade de posições necessárias é:

```text
N × M
```

Por exemplo, para:

```text
N = 3
M = 3
```

são necessárias:

```text
3 × 3 = 9 posições
```

A memória pode ser representada como:

```text
[20][15][14][12][20][12][18][5][10]
```

Após o término do programa, essa memória é liberada:

```c
free(Escola.pesquisa);
Escola.pesquisa = NULL;
```

---

## Armazenamento da Matriz

Apesar dos dados representarem uma matriz, eles são armazenados em uma região linear de memória.

Para acessar uma posição correspondente a uma linha e uma coluna, o programa utiliza:

```c
i * ptrr->qntTurmas + j
```

Assim:

```c
ptrr->pesquisa[i * ptrr->qntTurmas + j]
```

possui função equivalente ao acesso:

```c
matriz[i][j]
```

de uma matriz tradicional.

Por exemplo:

```text
20 15 14
12 20 12
18  5 10
```

é armazenado como:

```text
Índice:  0   1   2   3   4   5   6  7   8
Valor:  20  15  14  12  20  12  18  5  10
```

---

## Lógica da Verificação

Para cada turma, o programa percorre todas as frutas:

```c
for (int i = 0; i < ptrr->qntTurmas; i++)
```

e procura o maior número de alunos registrado naquela turma:

```c
if (valor > maior)
{
    maior = valor;
}
```

Isso funciona porque um mesmo aluno pode gostar de várias frutas.

Por exemplo:

```text
20 alunos gostam de uma fruta
12 alunos gostam de outra
18 alunos gostam de outra
```

É possível que os `12` e os `18` alunos façam parte dos mesmos `20` alunos.

Portanto, o menor número possível de alunos nessa turma é:

```text
20
```

Depois, o maior valor de cada turma é adicionado ao total:

```c
totalAlunos += maior;
```

---

## Caso Especial

O enunciado determina que:

```text
Cada turma tem pelo menos um aluno.
```

Portanto, se uma turma apresentar:

```text
0
0
0
```

o programa não pode considerar que ela possui `0` alunos.

Por isso existe:

```c
if (maior == 0)
{
    maior = 1;
}
```

Dessa forma, cada turma sempre terá pelo menos um aluno.

---

## Complexidade

O programa precisa analisar todos os valores fornecidos.

Como existem `N` frutas e `M` turmas:

```text
Complexidade de tempo: O(N × M)
```

Como os limites são:

```text
N ≤ 1000
M ≤ 1000
```

o programa analisa no máximo:

```text
1.000.000
```

valores.

A memória utilizada para armazenar a pesquisa também é:

```text
Complexidade de memória: O(N × M)
```

---

# PROPOSTA

<!-- Coloque aqui as imagens da proposta -->

<img src="<img width="476" height="609" alt="image" src="https://github.com/user-attachments/assets/c9fef4b1-15d3-4702-90bf-ef0c651052ad" />
" />



## Enunciado Original

Problema A — **Alimentação Saudável**

Maratona de Programação da SBC 2025:

https://maratona.sbc.org.br/hist/2025/subbr-2025/maratona.pdf
