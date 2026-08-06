<img width="771" height="792" alt="imagem" src="https://github.com/user-attachments/assets/7304a349-3438-40c6-af40-fa95745d5955" /># Leitor e Divisor de Números em C

Um programa em C desenvolvido para ler caracteres individuais via entrada padrão, convertê-los em números inteiros de 3 dígitos utilizando aritmética ASCII e realizar uma operação segura de divisão com formatação de saída de ponto flutuante.

---

## Funcionalidades

* **Leitura com Ponteiros:** Armazena múltiplos caracteres inseridos pelo usuário utilizando um array de ponteiros (`char*`).
* **Conversão ASCII:** Converte caracteres numéricos (`'0'` a `'9'`) em seus respectivos valores inteiros utilizando subtrações baseadas na tabela ASCII.
* **Tratamento de Erros:** Previne falhas de execução ao verificar se o divisor é zero antes de efetuar a operação matemática.
* **Saída Formatada:** Exibe o resultado da divisão com precisão de três casas decimais (`%.3f`).

---

## Tecnologias Utilizadas

* **Linguagem C** (Padrão C99 ou superior)
* **Biblioteca Padrão:** `<stdio.h>`

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

O programa espera que você insira 6 caracteres (que podem ser separados por espaços ou quebras de linha). Os três primeiros formarão o primeiro número e os três últimos formarão o segundo número.

**Entrada:**

```text
1 2 0 0 4 0

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
| `pegar_char` | `void` | Lê 6 caracteres da entrada padrão utilizando um loop e ponteiros. |
| `char_numero` | `int` | Converte três caracteres em um único número inteiro de 3 dígitos. |
| `divisao` | `void` | Realiza a divisão entre os números e imprime o resultado formatado. |

---
<img width="755" height="902" alt="imagem" src="https://github.com/user-attachments/assets/a1e5d8f6-ab77-4b00-a486-63e8d9f48336" />
<img width="771" height="792" alt="imagem" src="https://github.com/user-attachments/assets/bd2b6e68-8f9d-45ea-82b6-75d8aa1f23f8" />
---


