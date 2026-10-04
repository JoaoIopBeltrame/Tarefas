# Problema K - Katmandu — Verificador de Tempo de Sono em C - https://maratona.sbc.org.br/hist/2021/primeira-fase/maratona.pdf

Um programa desenvolvido em **C** para determinar se uma pessoa consegue dormir por pelo menos **T minutos consecutivos** durante um voo, sem perder nenhuma das refeições servidas.

O programa recebe a duração necessária de sono, a duração total do voo e os horários das refeições. A partir dessas informações, verifica se existe algum intervalo suficientemente grande para dormir.

---

## Funcionalidades

* **Leitura dos Dados:** Recebe o tempo necessário de sono, a duração do voo e a quantidade de refeições.
* **Uso de `struct`:** Armazena todas as informações relacionadas ao voo dentro de uma estrutura `InfoVoo`.
* **Uso de Ponteiros:** As funções recebem um ponteiro para a estrutura, permitindo acessar e modificar seus dados diretamente.
* **Array de Horários:** Os horários das refeições são armazenados em um vetor de inteiros.
* **Percorrimento com Ponteiros:** Utiliza ponteiros para percorrer os horários das refeições.
* **Detecção de Intervalos:** Verifica o tempo disponível entre o início do voo, as refeições e o final do voo.
* **Saída Simples:** Exibe `Y` caso seja possível dormir pelo tempo necessário ou `N` caso não seja possível.

---

## Tecnologias Utilizadas

* **Linguagem C**
* **Biblioteca Padrão:** `<stdio.h>`
* **Structs**
* **Arrays**
* **Ponteiros**
* **Funções**

---

## Código Completo

```c
#include <stdio.h>

#define MAX_REF 1000

typedef struct
{
    int temp_deSono;       // T
    int duracaoVoo;        // D
    int qntRefeicao;       // M
    int horaRefe[MAX_REF]; // H
} InfoVoo;

void lerInpt(InfoVoo *ptrr);
void lerComida(InfoVoo *ptrr);
void retorYorN(InfoVoo *ptrr);

int main(void)
{
    InfoVoo Katmanu;

    lerInpt(&Katmanu);
    lerComida(&Katmanu);
    retorYorN(&Katmanu);

    return 0;
}

void lerInpt(InfoVoo *ptrr)
{
    scanf("%d %d %d",
          &ptrr->temp_deSono,
          &ptrr->duracaoVoo,
          &ptrr->qntRefeicao);
}

void lerComida(InfoVoo *ptrr)
{
    for (int i = 0; i < ptrr->qntRefeicao; i++)
    {
        scanf("%d", &ptrr->horaRefe[i]);
    }
}

void retorYorN(InfoVoo *ptrr)
{
    int detGap = 0;

    int *pRef = ptrr->horaRefe;
    int *pRefSob = ptrr->horaRefe + ptrr->qntRefeicao;

    for (int i = 0; i <= ptrr->duracaoVoo; i++)
    {
        if (pRef < pRefSob && i == *pRef)
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
}
```

---

## Como Compilar e Executar

Para compilar o programa utilizando o **GCC**, salve o código em um arquivo chamado `main.c`.

No terminal, execute:

```bash
gcc main.c -o katmandu
```

Depois execute o programa:

### Linux / macOS

```bash
./katmandu
```

### Windows

```bash
katmandu.exe
```

---

## Entrada

A primeira linha contém três números inteiros:

```text
T D M
```

Onde:

* `T` representa a quantidade de minutos consecutivos necessários para descansar.
* `D` representa a duração total do voo.
* `M` representa a quantidade de refeições servidas durante o voo.

Depois são informados os horários das `M` refeições.

---

## Exemplo de Uso

### Entrada

```text
30 120 2
40 90
```

Nesse exemplo:

* São necessários `30` minutos consecutivos de sono.
* O voo possui duração de `120` minutos.
* Existem `2` refeições.
* As refeições acontecem nos minutos `40` e `90`.

O programa verifica os intervalos disponíveis entre esses horários.

### Saída

```text
Y
```

Isso significa que existe pelo menos um intervalo no qual é possível dormir durante `30` minutos consecutivos sem perder uma refeição.

---

## Estrutura do Código

| Função | Tipo de Retorno | Descrição |
| --- | --- | --- |
| `main` | `int` | Controla o fluxo principal do programa. |
| `lerInpt` | `void` | Lê o tempo de sono, duração do voo e quantidade de refeições. |
| `lerComida` | `void` | Lê e armazena os horários das refeições. |
| `retorYorN` | `void` | Verifica se existe um intervalo suficiente para dormir e imprime `Y` ou `N`. |

---

## Estrutura `InfoVoo`

As informações necessárias para resolver o problema são armazenadas em uma única estrutura:

```c
typedef struct
{
    int temp_deSono;
    int duracaoVoo;
    int qntRefeicao;
    int horaRefe[MAX_REF];
} InfoVoo;
```

| Campo | Significado |
| --- | --- |
| `temp_deSono` | Tempo consecutivo necessário para descansar (`T`). |
| `duracaoVoo` | Duração total do voo (`D`). |
| `qntRefeicao` | Quantidade de refeições durante o voo (`M`). |
| `horaRefe` | Vetor contendo os horários das refeições. |

---

## Lógica da Verificação

A função `retorYorN()` percorre os minutos do voo e mantém registrado o último momento que impede a continuação do sono.

Os ponteiros:

```c
int *pRef = ptrr->horaRefe;
int *pRefSob = ptrr->horaRefe + ptrr->qntRefeicao;
```

são utilizados para percorrer o vetor de horários das refeições.

Quando o programa encontra uma refeição:

```c
if (pRef < pRefSob && i == *pRef)
{
    detGap = i;
    pRef++;
}
```

o início do intervalo disponível é atualizado.

Depois é verificado se o intervalo já possui o tempo necessário de sono:

```c
else if (i - detGap == ptrr->temp_deSono)
{
    puts("Y");
    return;
}
```

Caso seja encontrado um intervalo suficientemente grande, o programa imprime:

```text
Y
```

Caso todo o voo seja analisado sem encontrar esse intervalo:

```text
N
```

---

# PROPOSTA

<img src="<img width="550" height="599" alt="image" src="https://github.com/user-attachments/assets/fc0e9fbc-f777-4986-bff0-8e2af3b2a533" />
<img src="<img width="581" height="166" alt="image" src="https://github.com/user-attachments/assets/b81330db-890a-402b-9d55-deb87d41d437" />
<img src="<img width="561" height="182" alt="image" src="https://github.com/user-attachments/assets/03fedca4-fb88-4a83-9d16-b0244c3e084d" />
---
