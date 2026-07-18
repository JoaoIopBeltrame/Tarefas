# Pedra, Papel e Tesoura — Jogo em Python
<img width="1366" height="494" alt="image" src="https://github.com/user-attachments/assets/2dab91fa-cc8b-47e1-ba7f-ab38f4df279c" />


Jogo de Pedra, Papel e Tesoura desenvolvido em Python puro, rodando direto no terminal com interface colorida usando códigos ANSI. O projeto possui três modos de jogo: **Jogador vs Jogador**, **Jogador vs Computador** e **Computador vs Computador**.

---

## Sumário

- [Funcionalidades](#funcionalidades)
- [Bibliotecas utilizadas](#bibliotecas-utilizadas)
- [Cores e estilização no terminal](#cores-e-estilização-no-terminal)
- [Lógica da jogada do computador](#lógica-da-jogada-do-computador)
- [Etapas e fluxo do jogo](#etapas-e-fluxo-do-jogo)
- [Validações de entrada](#validações-de-entrada)
- [Problemas enfrentados](#problemas-enfrentados)

---

## Funcionalidades

- Três modos de jogo: JxJ (Jogador vs Jogador), JxC (Jogador vs Computador) e CxC (Computador vs Computador).
- Sistema de pontuação com placar acumulado entre rodadas.
- Mural de resultados com tabela colorida ao final de cada rodada.
- Animação de "Reiniciando..." com pontinhos no terminal.
- Limpeza automática de tela entre jogadas.
- Ocultação e exibição do cursor durante animações.

---

## Bibliotecas utilizadas

O projeto utiliza apenas bibliotecas nativas do Python, sem instalação externa.

### `os` — Interação com o sistema operacional

Usado para limpar a tela do terminal:

```python
os.system('cls' if os.name == 'nt' else 'clear')
```

`os.system()` executa um comando do terminal de dentro do Python. `os.name` verifica o sistema operacional: se for `'nt'` (Windows), executa `cls`; caso contrário (Linux/Mac), executa `clear`. Ambos apagam o conteúdo visível da tela.

### `sys` — Escrita direta na saída padrão

Usado para criar a animação dos pontinhos sem pular linha:

```python
sys.stdout.write(f'\r{AMA}{NEG}Reiniciando{pontos:<3}{RE}')
sys.stdout.flush()
```

`sys.stdout.write()` escreve texto na tela **sem pular linha** (diferente do `print`). O `\r` retorna o cursor ao início da linha, permitindo sobrescrever o texto anterior — é isso que faz os pontinhos "animarem" no mesmo lugar. O `flush()` força a exibição imediata do texto, sem esperar o buffer do Python.

### `time` — Controle de pausas

```python
time.sleep(1)
```

Pausa a execução pelo número de segundos informado. No jogo, serve para dar tempo do jogador ler as mensagens antes da tela ser limpa e para controlar a velocidade da animação.

### `random` — Geração de números aleatórios

```python
n = random.randint(0, 2)
```

`randint(0, 2)` retorna um número inteiro aleatório entre 0 e 2. Esse número é mapeado para uma jogada: `0 = pedra`, `1 = papel`, `2 = tesoura`. É assim que o computador "escolhe" sua jogada.

---

## Cores e estilização no terminal

A interface colorida é feita com **sequências de escape ANSI**, que são códigos especiais interpretados pelo terminal para alterar cor e estilo do texto.

```python
AZ   = "\033[34m"   # Azul
VERD = "\033[32m"   # Verde
VERM = "\033[31m"   # Vermelho
CI   = "\033[36m"   # Ciano
AMA  = "\033[33m"   # Amarelo
ROSA = "\033[35m"   # Rosa/Magenta
NEG  = "\033[1m"    # Negrito
RE   = "\033[0m"    # Reset (volta ao normal)
HIDE = "\033[?25l"  # Esconde o cursor
SHOW = "\033[?25h"  # Mostra o cursor
```
<img width="695" height="189" alt="image" src="https://github.com/user-attachments/assets/20317d21-ded2-4b54-a1c4-8c10dbc43dd7" />

Para usar, basta colocar a variável da cor antes do texto e o `RE` (reset) depois:

```python
print(f"{VERD}Você venceu!{RE}")
```

**Resultado no terminal:** o texto "Você venceu!" aparece em verde, e o reset garante que o próximo texto volte à cor padrão.

`HIDE` e `SHOW` controlam a visibilidade do cursor — o cursor é escondido durante animações para não ficar piscando no meio do texto.

---

## Lógica da jogada do computador

O computador não usa listas, tuplas ou dicionários para escolher sua jogada. Em vez disso, um número inteiro aleatório é gerado com `random.randint(0, 2)` e depois mapeado com `if/elif`:

```python
n = random.randint(0, 2)

if n == 0:
    jogada_pc = "pedra"
elif n == 1:
    jogada_pc = "papel"
else:
    jogada_pc = "tesoura"
```

Cada número inteiro (0, 1 ou 2) corresponde diretamente a uma jogada. O `randint` garante distribuição igual entre as três opções.

---

## Etapas e fluxo do jogo

### 1. Tela inicial

O terminal exibe o nome do jogo e as opções de modo: **JxJ**, **JxC** ou **CxC**. O jogador escolhe qual modo quer jogar.

### 2. Cadastro de nomes

Os jogadores inserem seus nomes. Duas validações são aplicadas aqui:

- **Nome em branco:** um `while` loop impede que o jogador prossiga sem digitar um nome.
- **Nomes repetidos (modo JxJ):** outro `while` loop verifica se o nome do Jogador 2 é igual ao do Jogador 1. Se for, pede um nome diferente.
 
<img width="1366" height="679" alt="image" src="https://github.com/user-attachments/assets/cf7e28fb-666d-4b50-a234-cab130df2ea5" />
<img width="1366" height="231" alt="image" src="https://github.com/user-attachments/assets/a2cf29a1-9aaa-4a91-9f22-d71e56a3de7c" />

### 3. Entrada das jogadas

Cada jogador digita sua jogada (`pedra`, `papel` ou `tesoura`). O input passa por dois tratamentos:

- `.lower()` — converte tudo para minúscula, evitando erro por digitação tipo "Pedra" ou "PEDRA".
- `.strip()` — remove espaços extras antes e depois, evitando erro por um espaço acidental.

Se o jogador digitar algo diferente de `pedra`, `papel` ou `tesoura`, o jogo pede para digitar novamente.

### 4. Resolução da rodada

A lógica de vitória segue as regras clássicas:

- Pedra vence Tesoura
- Papel vence Pedra
- Tesoura vence Papel

<img width="1366" height="679" alt="image" src="https://github.com/user-attachments/assets/342fe14e-bc32-4ee2-9246-b8041f42b7ff" />
Em caso de empate (mesma jogada), cada jogador recebe 1 ponto. O vencedor da rodada recebe 1 ponto.

### 5. Mural de resultados

Ao final de cada rodada, é exibida uma tabela com o placar acumulado. As cores indicam o desempenho:

- **Azul** — jogador com mais pontos (líder).
- **Vermelho** — jogador com menos pontos.
- **Amarelo** — ambos, em caso de empate no placar.

O jogador pode então escolher **continuar** (permanecendo no mesmo modo) ou **sair**.

---

## Problemas enfrentados

O projeto tinha a restrição de não utilizar **listas, tuplas, sets ou criar bibliotecas**. A solução para a jogada do computador foi usar `random.randint()` (biblioteca nativa) para gerar um número inteiro de 0 a 2, e então atribuir cada número a uma jogada com `if/elif/else`, sem precisar de nenhuma estrutura de dados.

---

<img width="490" height="171" alt="image" src="https://github.com/user-attachments/assets/d9f08fe6-4de6-40f3-b5f9-fbfd3aa9f5fa" />


