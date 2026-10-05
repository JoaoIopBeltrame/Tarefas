# Lista de Aplicativos com Template Strings

Uma aplicação desenvolvida em **HTML, CSS e JavaScript** para exibir uma lista de aplicativos de forma dinâmica.

Os dados são armazenados em um **array de objetos** no JavaScript e utilizados para gerar automaticamente uma tabela e cards através de `map()`, **template strings**, `join()` e `innerHTML`.

O mesmo conjunto de dados é reaproveitado para criar diferentes elementos na página, evitando a repetição manual de código HTML.

---

## Funcionalidades

* **Lista de Aplicativos:** Armazena informações de diferentes aplicativos.
* **Array de Objetos:** Cada aplicativo possui ID, nome, descrição e imagem.
* **Tabela Dinâmica:** As linhas da tabela são geradas automaticamente pelo JavaScript.
* **Cards Dinâmicos:** Os cards também são criados automaticamente a partir do mesmo array.
* **Template Strings:** Utilizadas para montar elementos HTML dentro do JavaScript.
* **Uso de `map()`:** Percorre todos os objetos do array.
* **Uso de `join()`:** Junta os elementos HTML gerados pelo `map()`.
* **Uso de `innerHTML`:** Insere os elementos gerados dentro da página.
* **Tabela Zebrada:** Linhas pares e ímpares possuem cores diferentes.
* **Efeito Hover:** Linhas e cards possuem alteração visual ao passar o mouse.
* **Flexbox:** Utilizado para organizar os cards.

---

## Tecnologias Utilizadas

* **HTML5**
* **CSS3**
* **JavaScript**
* **Arrays**
* **Objetos**
* **DOM**
* **Template Strings**
* **`map()`**
* **`join()`**
* **`innerHTML`**
* **Flexbox**
* **`:nth-child()`**
* **`:hover`**

---

## Estrutura do Projeto

```text
projeto/
│
├── index.html
├── style.css
└── script.js
```

---

## Código HTML

O arquivo `index.html` contém a estrutura principal da aplicação.

```html
<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Lista de Aplicativos</title>

    <link rel="stylesheet" href="style.css">
</head>

<body>

    <main class="container">

        <h1>Lista de Aplicativos</h1>

        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Descrição</th>
                </tr>
            </thead>

            <tbody id="corpo-tabela"></tbody>
        </table>

        <h2>Cards</h2>

        <div id="lista-cards"></div>

    </main>

    <script src="script.js"></script>

</body>

</html>
```

A tabela possui apenas o cabeçalho escrito diretamente no HTML.

O corpo:

```html
<tbody id="corpo-tabela"></tbody>
```

começa vazio, pois será preenchido automaticamente pelo JavaScript.

O mesmo acontece com:

```html
<div id="lista-cards"></div>
```

que receberá os cards.

---

## Array de Aplicativos

Os aplicativos são armazenados dentro de um array de objetos:

```javascript
const aplicativos = [
    {
        id_aplicativo: 1,
        nome: "WhatsApp",
        descricao: "Mensagens instantâneas.",
        imagem: "https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg"
    },

    {
        id_aplicativo: 2,
        nome: "Spotify",
        descricao: "Streaming de músicas.",
        imagem: "https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg"
    },

    {
        id_aplicativo: 3,
        nome: "Google Maps",
        descricao: "Mapas e navegação.",
        imagem: "https://upload.wikimedia.org/wikipedia/commons/a/aa/Google_Maps_icon_%282020%29.svg"
    },

    {
        id_aplicativo: 4,
        nome: "Notion",
        descricao: "Notas e projetos.",
        imagem: "https://raw.githubusercontent.com/lobehub/lobe-icons/refs/heads/master/packages/static-png/light/notion.png"
    }
];
```

Cada objeto possui quatro propriedades:

| Propriedade | Função |
|---|---|
| `id_aplicativo` | Identificação do aplicativo |
| `nome` | Nome do aplicativo |
| `descricao` | Pequena descrição |
| `imagem` | Endereço da imagem utilizada no card |

---

## Geração da Tabela

Primeiro, o JavaScript seleciona o corpo da tabela:

```javascript
const corpoTabela = document.getElementById("corpo-tabela");
```

Depois utiliza:

```javascript
corpoTabela.innerHTML = aplicativos.map((app) => {
    return `
        <tr>
            <td>${app.id_aplicativo}</td>
            <td>${app.nome}</td>
            <td>${app.descricao}</td>
        </tr>
    `;
}).join("");
```

Cada objeto do array gera automaticamente uma nova linha:

```html
<tr>
    <td>ID</td>
    <td>Nome</td>
    <td>Descrição</td>
</tr>
```

Assim, as linhas não precisam ser escritas manualmente no HTML.

---

## Geração dos Cards

Os mesmos dados são reaproveitados para criar os cards:

```javascript
const listaCards = document.getElementById("lista-cards");

listaCards.innerHTML = aplicativos.map((app) => {
    return `
        <div class="card">

            <img
                src="${app.imagem}"
                alt="${app.nome}"
            >

            <h3>${app.nome}</h3>

            <p>${app.descricao}</p>

        </div>
    `;
}).join("");
```

Cada aplicativo gera:

```text
Card
│
├── Imagem
├── Nome
└── Descrição
```

Dessa forma, o mesmo array é utilizado tanto para a tabela quanto para os cards.

---

## Funcionamento do `map()`

O método:

```javascript
map()
```

percorre todos os elementos do array.

Neste projeto:

```javascript
aplicativos.map((app) => {
```

cada aplicativo é representado temporariamente por:

```javascript
app
```

Permitindo acessar:

```javascript
app.id_aplicativo
app.nome
app.descricao
app.imagem
```

---

## Template Strings

As **template strings** são strings escritas utilizando crases:

```javascript
` `
```

Elas permitem inserir valores utilizando:

```javascript
${}
```

Por exemplo:

```javascript
<td>${app.nome}</td>
```

Se o nome do aplicativo for:

```javascript
"Spotify"
```

o HTML gerado será:

```html
<td>Spotify</td>
```

Isso permite misturar HTML com os dados armazenados nos objetos.

---

## Funcionamento do `join()`

Após o `map()` é utilizado:

```javascript
.join("")
```

O `map()` gera vários trechos de HTML.

O `join("")` junta todos esses trechos em uma única string.

O processo fica:

```text
map()
  ↓
HTML do WhatsApp
HTML do Spotify
HTML do Google Maps
HTML do Notion
  ↓
join("")
  ↓
uma única string HTML
```

---

## Funcionamento do `innerHTML`

Depois que o conteúdo é criado, o:

```javascript
innerHTML
```

insere esse conteúdo dentro da página.

Na tabela:

```javascript
corpoTabela.innerHTML = ...
```

Nos cards:

```javascript
listaCards.innerHTML = ...
```

Portanto, o fluxo principal é:

```text
Array
  ↓
map()
  ↓
Template Strings
  ↓
join("")
  ↓
innerHTML
  ↓
Página
```

---

## Reaproveitamento dos Dados

Uma das principais características do projeto é não precisar criar informações separadas para a tabela e para os cards.

O mesmo array:

```text
              aplicativos
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
        map()             map()
          │                 │
          ▼                 ▼
        <tr>              .card
          │                 │
          ▼                 ▼
       TABELA              CARDS
```

Por exemplo, ao adicionar:

```javascript
{
    id_aplicativo: 5,
    nome: "Novo App",
    descricao: "Novo aplicativo.",
    imagem: "imagem.png"
}
```

o novo aplicativo poderá aparecer automaticamente nas duas representações geradas a partir do array.

---

## Tabela Zebrada

Para diferenciar visualmente as linhas, o CSS utiliza:

```css
tbody tr:nth-child(even) {
    background-color: #e8eef3;
}

tbody tr:nth-child(odd) {
    background-color: white;
}
```

O:

```css
:nth-child(even)
```

seleciona as linhas pares.

O:

```css
:nth-child(odd)
```

seleciona as linhas ímpares.

O resultado é uma tabela com cores alternadas.

---

## Efeito Hover na Tabela

As linhas também possuem:

```css
tbody tr:hover {
    background-color: #d9e5ee;
}
```

Quando o mouse passa sobre uma linha, sua cor de fundo é alterada.

---

## Cards com Flexbox

Os cards são organizados através de:

```css
#lista-cards {
    display: flex;

    flex-direction: row;
    flex-wrap: wrap;

    gap: 20px;
}
```

### `display: flex`

Ativa o Flexbox.

### `flex-direction: row`

Organiza os cards horizontalmente.

### `flex-wrap: wrap`

Permite que os cards passem para a próxima linha quando não houver espaço.

### `gap: 20px`

Cria um espaço de `20px` entre os cards.

---

## Estilização dos Cards

Cada card possui:

```css
.card {
    width: 210px;

    background-color: white;

    border-radius: 10px;

    padding: 20px;

    text-align: center;

    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);

    transition: 0.2s;
}
```

Isso define a largura, fundo, arredondamento, espaçamento, alinhamento e sombra dos cards.

---

## Efeito Hover nos Cards

Quando o mouse passa sobre um card:

```css
.card:hover {
    transform: translateY(-5px);

    box-shadow: 0 5px 12px rgba(0, 0, 0, 0.20);
}
```

O:

```css
translateY(-5px)
```

move o card levemente para cima.

---

## Fluxo da Aplicação

```text
Página é aberta
       │
       ▼
HTML é carregado
       │
       ▼
script.js é executado
       │
       ▼
Array de aplicativos
       │
       ├──────────────────────┐
       │                      │
       ▼                      ▼
     map()                  map()
       │                      │
       ▼                      ▼
Template String        Template String
       │                      │
       ▼                      ▼
     <tr>                   .card
       │                      │
       ▼                      ▼
   join("")               join("")
       │                      │
       ▼                      ▼
  innerHTML              innerHTML
       │                      │
       ▼                      ▼
    TABELA                  CARDS
```

---

## Aplicativos Utilizados

| ID | Aplicativo | Descrição |
|---:|---|---|
| 1 | WhatsApp | Mensagens instantâneas |
| 2 | Spotify | Streaming de músicas |
| 3 | Google Maps | Mapas e navegação |
| 4 | Notion | Notas e projetos |

---

## Conceitos Praticados

```text
HTML
├── table
├── thead
├── tbody
├── tr
├── th
├── td
├── div
└── script

CSS
├── Flexbox
├── nth-child
├── hover
├── box-shadow
├── border-radius
├── transform
└── transition

JavaScript
├── const
├── Array
├── Objetos
├── getElementById()
├── map()
├── Template Strings
├── join()
└── innerHTML
```

---

## PROPOSTA

<!-- Coloque aqui a imagem da atividade -->

<img width="1101" height="540" alt="image" src="https://github.com/user-attachments/assets/32eb1d23-4867-4ada-ae02-d8b48815146d" />

---

## RESULTADO

<!-- Coloque aqui a imagem do projeto funcionando -->

<img width="1105" height="683" alt="image" src="https://github.com/user-attachments/assets/f17bb1e9-218c-49d1-98a1-28511bf87623" />

---
