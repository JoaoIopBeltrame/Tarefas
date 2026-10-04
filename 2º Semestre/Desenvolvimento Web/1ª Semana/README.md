# Sistema de Cinema em HTML

Uma página desenvolvida utilizando **HTML** para simular uma interface simples de seleção de filmes e cadastro para um cinema.

O projeto utiliza diferentes elementos HTML para criar campos de formulário, opções de comida, seleção de horários, visualização de filmes e uma tabela contendo informações sobre cada filme disponível.

A página foi desenvolvida com foco na prática dos principais componentes HTML, como `input`, `select`, `fieldset`, `details`, `radio`, `table` e `img`.

---

## Funcionalidades

* **Cadastro do Usuário:** Permite informar nome, email e senha.
* **Seleção de Cor:** Permite escolher uma cor para o ticket utilizando `input type="color"`.
* **Seleção de Comida:** Permite selecionar refrigerante e pipoca.
* **Tipos de Refrigerante:** Disponibiliza Pepsi, Coca-Cola e Guaraná.
* **Tamanhos de Pipoca:** Permite escolher entre Grande, Média e Pequena.
* **Seleção de Horário:** Disponibiliza diferentes horários para a sessão.
* **Visualização de Filmes:** Utiliza `details` e `summary` para mostrar os filmes disponíveis.
* **Seleção de Filme:** Utiliza botões `radio` para permitir a escolha de apenas um filme.
* **Tabela de Filmes:** Exibe informações sobre classificação indicativa, preço e combo promocional.
* **Imagens:** Exibe os cartazes dos filmes disponíveis.
* **Envio:** Possui um botão para envio do formulário.

---

## Tecnologias Utilizadas

* **HTML5**
* **Formulários HTML**
* **Inputs**
* **Fieldset e Legend**
* **Select e Option**
* **Checkbox**
* **Radio Button**
* **Details e Summary**
* **Tabelas**
* **Imagens**
* **Validação HTML com `required`**
* **Limitação de caracteres com `minlength` e `maxlength`**

---

## Estrutura do Projeto

```text
projeto/
│
├── index.html
├── README.md
│
└── imagem/
    ├── jurassic_park_lll.jpg
    ├── homem_aranha_ll.webp
    └── DragonballEvolution.jpg
```

As imagens utilizadas na página ficam armazenadas dentro da pasta:

```text
imagem/
```

E são acessadas no HTML utilizando caminhos como:

```html
<img src="imagem/jurassic_park_lll.jpg" alt="Jurassic Park">
```

---

## Cadastro

A primeira parte da página possui um formulário de cadastro.

```html
<fieldset>
    <legend>Cadastro</legend>

    <label for="nome">Nome: </label>
    <input
        type="text"
        id="nome"
        placeholder="Nome aqui"
        minlength="3"
        maxlength="45"
        required
    >

    <label for="mail">Email: </label>
    <input
        type="text"
        id="mail"
        placeholder="Email aqui"
        minlength="3"
        maxlength="45"
        required
    >

    <label for="password">Senha: </label>
    <input
        type="password"
        id="password"
        placeholder="Senha aqui"
        minlength="3"
        maxlength="45"
        required
    >
</fieldset>
```

O `fieldset` é utilizado para agrupar campos relacionados.

O título desse grupo é definido utilizando:

```html
<legend>Cadastro</legend>
```

---

## Campos de Entrada

O projeto utiliza diferentes tipos de `input`.

### Texto

```html
<input type="text">
```

Utilizado para receber informações em formato de texto.

No projeto, ele é utilizado para:

```text
Nome
Email
```

### Senha

```html
<input type="password">
```

O campo de senha oculta visualmente os caracteres digitados pelo usuário.

### Cor

```html
<input type="color">
```

Abre o seletor de cores do navegador.

No projeto, ele é utilizado para selecionar a cor do ticket.

### Checkbox

```html
<input type="checkbox">
```

Permite marcar ou desmarcar uma opção.

É utilizado para selecionar:

```text
Refrigerante
Pipoca
```

### Radio

```html
<input type="radio" name="filme">
```

Os três filmes utilizam o mesmo:

```html
name="filme"
```

Isso faz com que apenas um filme possa ser selecionado por vez.

As opções disponíveis são:

```text
Jurassic Park
Homem-Aranha
Dragon Ball
```

---

## Seleção de Comida

A página possui um `fieldset` específico para as opções de comida.

```html
<fieldset>
    <legend>Comida</legend>

    <input type="checkbox">Refrigerante

    <select>
        <option>Pepsi</option>
        <option>Coca-Cola</option>
        <option>Guaraná</option>
    </select>

    <input type="checkbox">Pipoca

    <select>
        <option>Grande</option>
        <option>Média</option>
        <option>Pequena</option>
    </select>
</fieldset>
```

O elemento:

```html
<select>
```

cria uma caixa de seleção.

Cada possibilidade é definida utilizando:

```html
<option>
```

---

## Seleção de Horário

Os horários disponíveis são armazenados dentro de um `select`.

```html
<select>
    <option>19:00</option>
    <option>19:30</option>
    <option>20:00</option>
    <option>20:30</option>
    <option>21:00</option>
    <option>21:30</option>
    <option>22:00</option>
</select>
```

O usuário pode abrir a caixa de seleção e escolher um dos horários disponíveis.

---

## Visualização dos Filmes

Os filmes podem ser visualizados utilizando:

```html
<details>
    <summary>Ver filmes</summary>

    <img src="imagem/jurassic_park_lll.jpg" alt="Filme 1">
    <img src="imagem/homem_aranha_ll.webp" alt="Filme 2">
    <img src="imagem/DragonballEvolution.jpg" alt="Filme 3">
</details>
```

O elemento:

```html
<details>
```

cria uma área que pode ser aberta e fechada.

O texto clicável é definido pelo:

```html
<summary>
```

Quando o usuário clica em **Ver filmes**, as imagens são exibidas.

---

## Filmes Disponíveis

### Jurassic Park III

```html
<img
    src="imagem/jurassic_park_lll.jpg"
    height="225"
    width="150"
    alt="Filme 1"
>
```

### Homem-Aranha 2

```html
<img
    src="imagem/homem_aranha_ll.webp"
    width="150"
    alt="Filme 2"
>
```

### Dragonball Evolution

```html
<img
    src="imagem/DragonballEvolution.jpg"
    height="225"
    width="150"
    alt="Filme 3"
>
```

---

## Seleção do Filme

A escolha do filme é realizada utilizando `radio`.

```html
<input type="radio" name="filme"> Jurassic Park
<input type="radio" name="filme"> Homem-Aranha
<input type="radio" name="filme"> Dragon Ball
```

Todos possuem:

```html
name="filme"
```

Por isso, o navegador trata os três elementos como pertencentes ao mesmo grupo.

Dessa forma, selecionar um filme desmarca automaticamente o anterior.

---

## Tabela de Filmes

O projeto possui uma tabela para apresentar informações adicionais.

```html
<table>
    <tr>
        <th>Filme</th>
        <th>Idade indicativa</th>
        <th>Meia entrada</th>
        <th>Combo promocional</th>
    </tr>

    <tbody>
        ...
    </tbody>
</table>
```

A tabela possui quatro colunas:

| Filme | Idade indicativa | Meia entrada | Combo promocional |
| --- | --- | --- | --- |
| Jurassic Park III | 12 anos | R$ 15,00 | Pipoca + Refrigerante |
| Homem-Aranha 2 | 10 anos | R$ 15,00 | Pipoca Grande + Refrigerante |
| Dragonball Evolution | 10 anos | R$ 15,00 | Pipoca + Refrigerante |

---

## Estrutura da Tabela

O elemento:

```html
<table>
```

define a tabela.

Cada linha é criada utilizando:

```html
<tr>
```

Os títulos das colunas utilizam:

```html
<th>
```

Os dados utilizam:

```html
<td>
```

A estrutura utilizada é:

```text
table
│
├── tr
│   ├── th
│   ├── th
│   ├── th
│   └── th
│
└── tbody
    │
    ├── tr
    │   ├── td
    │   ├── td
    │   ├── td
    │   └── td
    │
    ├── tr
    │   └── ...
    │
    └── tr
        └── ...
```

---

## Validação dos Campos

Alguns campos utilizam:

```html
required
```

Isso informa ao navegador que o campo precisa ser preenchido antes do envio do formulário.

Também são utilizados:

```html
minlength="3"
maxlength="45"
```

O `minlength` determina a quantidade mínima de caracteres.

O `maxlength` determina a quantidade máxima.

Por exemplo:

```html
<input
    type="text"
    minlength="3"
    maxlength="45"
    required
>
```

significa que o campo:

```text
é obrigatório
mínimo = 3 caracteres
máximo = 45 caracteres
```

---

## Botão de Envio

No final da página existe:

```html
<button type="submit">Enviar</button>
```

O:

```html
type="submit"
```

define o botão como responsável pelo envio do formulário.

---

## Fluxo da Página

```text
Página
 │
 ├── Cadastro
 │    │
 │    ├── Nome
 │    ├── Email
 │    ├── Senha
 │    └── Cor do ticket
 │
 ├── Comida
 │    │
 │    ├── Refrigerante
 │    │     └── Tipo
 │    │
 │    └── Pipoca
 │          └── Tamanho
 │
 ├── Informações
 │
 ├── Horário
 │    │
 │    └── Seleção da sessão
 │
 ├── Filmes
 │    │
 │    ├── Jurassic Park III
 │    ├── Homem-Aranha 2
 │    └── Dragonball Evolution
 │
 ├── Seleção do filme
 │
 ├── Tabela
 │    │
 │    ├── Filme
 │    ├── Idade indicativa
 │    ├── Meia entrada
 │    └── Combo promocional
 │
 └── Enviar
```

---

## Objetivo da Atividade

A atividade tem como objetivo praticar a criação de uma página utilizando HTML e diferentes tipos de componentes.

Entre os principais conceitos utilizados estão:

```text
Formulários
Inputs
Labels
Fieldsets
Checkbox
Radio
Select
Option
Details
Summary
Imagens
Tabelas
Validação de campos
```

---

# PROPOSTA

A proposta da atividade consiste na criação individual de uma página utilizando apenas HTML.

Os principais requisitos apresentados são:

1. Criar um `<title>` para a página e um heading com um título visível.
2. Criar pelo menos 10 campos de formulário de tipos variados.
3. Utilizar componentes como `text`, `checkbox`, `radio`, `password`, `select` e `textarea`.
4. Abrir a página no navegador ou celular para validar os componentes.
5. Como extra, adicionar uma lista `<ul>` e uma imagem `<img>`.

<img width="757" height="525" alt="image" src="https://github.com/user-attachments/assets/3143e75c-f8c0-4868-b428-60835aca16e3" />


```
