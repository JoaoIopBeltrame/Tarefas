# Sistema de Cadastro e Classificação de Alunos em C

Um programa desenvolvido em **C** para cadastrar estudantes, armazenar suas matrículas e notas semestrais, determinar automaticamente sua situação acadêmica e exibir um relatório final formatado.

O programa utiliza **structs, ponteiros e alocação dinâmica de memória** para armazenar os dados dos estudantes. Cada aluno é classificado como **Aprovado** ou **Reprovado** de acordo com sua nota semestral.

---

## Funcionalidades

* **Cadastro de Estudantes:** Permite informar a matrícula e a nota semestral de cada aluno.
* **Uso de `struct`:** Armazena matrícula, nota e situação acadêmica dentro da estrutura `InfoAluno`.
* **Alocação Dinâmica:** Utiliza `malloc` para reservar memória para os estudantes durante a execução.
* **Uso de Ponteiros:** Os dados dos estudantes são acessados através de ponteiros para estruturas.
* **Classificação Automática:** Alunos com nota maior ou igual a `7.0` são classificados como aprovados.
* **Uso de `bool`:** A situação do estudante é armazenada utilizando os valores `true` e `false`.
* **Relatório Final:** Exibe matrícula, nota e situação de cada estudante em formato de tabela.
* **Liberação de Memória:** Utiliza `free` para liberar a memória alocada após o término do programa.

---

## Tecnologias Utilizadas

* **Linguagem C**
* **Bibliotecas Padrão:** `<stdio.h>`, `<stdlib.h>`, `<stdbool.h>`
* **Structs**
* **Ponteiros**
* **Alocação dinâmica com `malloc`**
* **Operador ternário**
* **Booleanos**
* **Funções**
* **Laços de repetição**

---

## Código Completo

```c
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct
{
    int matricula;
    float notaSemes;
    bool aprovado;
} InfoAluno;

void ler_dados_dos_estudantes(InfoAluno *ptrr, int quantidade);
void classificar(InfoAluno *ptrr, int quantidade);
void imprimir_relatorio(InfoAluno *ptrr, int quantidade);

int main(void)
{
    int quantidade = 3;

    InfoAluno *Estudante = malloc(quantidade * sizeof(InfoAluno));

    if (Estudante == NULL)
    {
        puts("Memoria insuficiente");
        return 1;
    }

    ler_dados_dos_estudantes(Estudante, quantidade);
    classificar(Estudante, quantidade);
    imprimir_relatorio(Estudante, quantidade);

    free(Estudante);
    Estudante = NULL;

    return 0;
}

void ler_dados_dos_estudantes(InfoAluno *ptrr, int quantidade)
{
    for (int i = 0; i < quantidade; i++)
    {
        printf("Cadastro estudante %d\n", i + 1);

        printf("Matricula\n>> ");
        scanf("%d", &(ptrr + i)->matricula);

        printf("Nota\n>> ");
        scanf("%f", &(ptrr + i)->notaSemes);
    }
}

void classificar(InfoAluno *ptrr, int quantidade)
{
    for (int i = 0; i < quantidade; i++)
    {
        if ((ptrr + i)->notaSemes >= 7)
        {
            (ptrr + i)->aprovado = true;
        }
        else
        {
            (ptrr + i)->aprovado = false;
        }
    }
}

void imprimir_relatorio(InfoAluno *ptrr, int quantidade)
{
    puts("============================================");
    puts("           RELATORIO FINAL");
    puts("============================================");

    printf("%-12s %-15s %-15s\n",
           "Matricula", "Nota", "Situacao");

    puts("--------------------------------------------");

    for (int i = 0; i < quantidade; i++)
    {
        printf("%-12d %-15.2f %-15s\n",
               (ptrr + i)->matricula,
               (ptrr + i)->notaSemes,
               (ptrr + i)->aprovado ? "Aprovado" : "Reprovado");
    }

    puts("============================================");
}
```

---

## Como Compilar e Executar

Para compilar o programa utilizando o **GCC**, salve o código em um arquivo chamado `main.c`.

No terminal, execute:

```bash
gcc main.c -o estudantes
```

Depois execute o programa:

### Linux / macOS

```bash
./estudantes
```

### Windows

```bash
estudantes.exe
```

---

## Entrada

O programa está configurado para cadastrar:

```c
int quantidade = 3;
```

Portanto, serão solicitados os dados de **3 estudantes**.

Para cada estudante são informados:

* Matrícula
* Nota semestral

Exemplo:

```text
Cadastro estudante 1
Matricula
>> 1001
Nota
>> 8.5

Cadastro estudante 2
Matricula
>> 1002
Nota
>> 6.0

Cadastro estudante 3
Matricula
>> 1003
Nota
>> 7.5
```

---

## Exemplo de Saída

Após o cadastro e a classificação dos estudantes, o programa gera um relatório semelhante a:

```text
============================================
           RELATORIO FINAL
============================================
Matricula    Nota            Situacao
--------------------------------------------
1001         8.50            Aprovado
1002         6.00            Reprovado
1003         7.50            Aprovado
============================================
```

---

## Estrutura do Código

| Função | Tipo de Retorno | Descrição |
| --- | --- | --- |
| `main` | `int` | Controla o fluxo principal, realiza a alocação e libera a memória. |
| `ler_dados_dos_estudantes` | `void` | Lê a matrícula e a nota de cada estudante. |
| `classificar` | `void` | Determina se cada estudante foi aprovado ou reprovado. |
| `imprimir_relatorio` | `void` | Exibe os dados e a situação dos estudantes em formato de tabela. |

---

## Estrutura `InfoAluno`

Cada estudante é representado pela estrutura:

```c
typedef struct
{
    int matricula;
    float notaSemes;
    bool aprovado;
} InfoAluno;
```

A estrutura reúne todas as informações relacionadas a um aluno.

| Campo | Tipo | Significado |
| --- | --- | --- |
| `matricula` | `int` | Número de matrícula do estudante. |
| `notaSemes` | `float` | Nota semestral do estudante. |
| `aprovado` | `bool` | Armazena `true` se aprovado e `false` se reprovado. |

---

## Alocação Dinâmica

O programa utiliza:

```c
InfoAluno *Estudante = malloc(
    quantidade * sizeof(InfoAluno)
);
```

O `malloc` reserva memória suficiente para armazenar a quantidade definida de estruturas `InfoAluno`.

Para:

```c
int quantidade = 3;
```

a memória pode ser representada como:

```text
Estudante
    |
    v
+-----------+-----------+-----------+
| Aluno 0   | Aluno 1   | Aluno 2   |
+-----------+-----------+-----------+
```

Cada posição possui:

```text
Aluno
├── matricula
├── notaSemes
└── aprovado
```

O programa também verifica se a alocação foi realizada corretamente:

```c
if (Estudante == NULL)
{
    puts("Memoria insuficiente");
    return 1;
}
```

---

## Acesso com Ponteiros

Os estudantes são acessados utilizando aritmética de ponteiros.

Por exemplo:

```c
(ptrr + i)->matricula
```

`ptrr` aponta para o primeiro estudante.

Então:

```text
(ptrr + 0) -> primeiro estudante
(ptrr + 1) -> segundo estudante
(ptrr + 2) -> terceiro estudante
```

Assim:

```c
(ptrr + i)->matricula
```

acessa a matrícula do estudante atual.

Da mesma forma:

```c
(ptrr + i)->notaSemes
```

acessa sua nota e:

```c
(ptrr + i)->aprovado
```

acessa sua situação.

---

## Classificação dos Estudantes

A função:

```c
void classificar(InfoAluno *ptrr, int quantidade)
```

percorre todos os estudantes.

A condição utilizada é:

```c
if ((ptrr + i)->notaSemes >= 7)
```

Caso a nota seja maior ou igual a `7`:

```c
(ptrr + i)->aprovado = true;
```

Caso contrário:

```c
(ptrr + i)->aprovado = false;
```

Portanto:

```text
Nota >= 7.0  -> Aprovado
Nota <  7.0  -> Reprovado
```

---

## Uso do Operador Ternário

Na impressão do relatório é utilizado:

```c
(ptrr + i)->aprovado ? "Aprovado" : "Reprovado"
```

Essa expressão verifica o valor de `aprovado`.

Se for:

```c
true
```

o resultado será:

```text
Aprovado
```

Se for:

```c
false
```

o resultado será:

```text
Reprovado
```

É uma forma reduzida de escrever:

```c
if ((ptrr + i)->aprovado)
{
    printf("Aprovado");
}
else
{
    printf("Reprovado");
}
```

---

## Formatação do Relatório

O programa utiliza:

```c
printf("%-12d %-15.2f %-15s\n",
       (ptrr + i)->matricula,
       (ptrr + i)->notaSemes,
       (ptrr + i)->aprovado ? "Aprovado" : "Reprovado");
```

Onde:

```text
%-12d
```

imprime a matrícula ocupando um espaço de 12 caracteres.

```text
%-15.2f
```

imprime a nota com duas casas decimais em um espaço de 15 caracteres.

```text
%-15s
```

imprime a situação em um espaço de 15 caracteres.

O sinal:

```text
-
```

faz o conteúdo ficar alinhado à esquerda.

---

## Liberação de Memória

Como a memória foi criada utilizando:

```c
malloc()
```

ela deve ser liberada quando não for mais necessária:

```c
free(Estudante);
```

Depois:

```c
Estudante = NULL;
```

remove do ponteiro o endereço da região de memória que já foi liberada.

---

## Fluxo do Programa

O funcionamento geral pode ser representado por:

```text
main
 |
 +--> cria quantidade
 |
 +--> malloc
 |      |
 |      +--> reserva memoria para os estudantes
 |
 +--> ler_dados_dos_estudantes()
 |      |
 |      +--> matricula
 |      +--> nota
 |
 +--> classificar()
 |      |
 |      +--> nota >= 7
 |              |
 |              +--> true
 |              |
 |              +--> false
 |
 +--> imprimir_relatorio()
 |
 +--> free()
 |
 +--> return 0
```

---

# PROPOSTA

<!-- Coloque aqui as imagens da proposta/exercício -->

<img src="https://github.com/user-attachments/assets/5a2e86a2-c657-4d48-88bb-2a895a5b7d8b" />

<img src="https://github.com/user-attachments/assets/3eacf189-54c4-40a0-aa31-f7e0b3dcaa95" />

