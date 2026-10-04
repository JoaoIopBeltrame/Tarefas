# Tarefa 3 - Seu Primeiro JavaScript

Projeto desenvolvido utilizando **HTML, CSS e JavaScript** com o objetivo de praticar os conceitos iniciais de programação para páginas web.

A aplicação permite comparar dois números, realizar operações matemáticas básicas e limpar os campos e resultados da tela.

---

## Funcionalidades

* **Comparação de Valores:** Recebe dois números e informa qual deles é o maior.
* **Verificação de Valores Iguais:** Caso os números sejam iguais, uma mensagem é exibida.
* **Calculadora Simples:** Realiza soma, subtração, multiplicação e divisão.
* **Divisão por Zero:** Impede a divisão quando o segundo número é zero.
* **Exibição de Resultados:** Os resultados são mostrados diretamente na página.
* **Botão de Limpeza:** Limpa os campos e resultados da aplicação.
* **Interação com JavaScript:** Os botões executam funções através de eventos de clique.
* **Estilização com CSS:** A interface utiliza cards, Flexbox, efeitos `hover` e campos estilizados.

---

## Tecnologias Utilizadas

* **HTML5**
* **CSS3**
* **JavaScript**
* **DOM**
* **Flexbox**
* **Eventos**
* **Condicionais**
* **Laço `for`**
* **`data-*` Attributes**
* **`querySelectorAll`**
* **`getElementById`**
* **`addEventListener`**

---

## Estrutura do Projeto

```text
Tarefa3/
│
├── index.html
├── style.css
└── script.js
```

---

# HTML

O arquivo `index.html` é responsável pela estrutura da aplicação.

Ele contém três partes principais:

```text
1. Maior valor
2. Calculadora
3. Limpar a tela
```

O JavaScript é conectado ao HTML através de:

```html
<script src="script.js"></script>
```

E o CSS através de:

```html
<link rel="stylesheet" href="style.css">
```

---

# 1. Maior Valor

A primeira parte recebe dois números:

```html
<input type="number" id="valor1" placeholder="Primeiro valor">
<input type="number" id="valor2" placeholder="Segundo valor">
```

O botão:

```html
<button type="button" id="btnComparar">
    Comparar
</button>
```

executa a comparação.

O resultado é exibido dentro de:

```html
<p id="resultadoComparar"></p>
```

---

## Comparação com JavaScript

Primeiro, o botão é selecionado:

```javascript
var btnComparar = document.getElementById("btnComparar");
```

Depois é criado um evento:

```javascript
btnComparar.addEventListener("click", function () {
```

Isso significa que o código dentro da função será executado quando o botão for clicado.

Os valores são obtidos através de:

```javascript
var v1 = Number(document.getElementById("valor1").value);
var v2 = Number(document.getElementById("valor2").value);
```

O:

```javascript
.value
```

obtém o conteúdo digitado no campo.

Já:

```javascript
Number()
```

converte esse conteúdo para número.

---

## Condições

A comparação é feita utilizando:

```javascript
if (v1 > v2) {
    mensagem = "O maior valor é " + v1;
}
else if (v2 > v1) {
    mensagem = "O maior valor é " + v2;
}
else {
    mensagem = "Os valores são iguais";
}
```

A lógica pode ser representada como:

```text
v1 > v2
   |
   ├── verdadeiro → v1 é maior
   |
   └── falso
         |
         v
      v2 > v1
         |
         ├── verdadeiro → v2 é maior
         |
         └── falso → valores iguais
```

Depois, a mensagem é colocada na página:

```javascript
resultadoComparar.textContent = mensagem;
```

---

# 2. Calculadora Simples

A segunda parte possui dois campos:

```html
<input type="number" id="numero1" placeholder="Digite o número 1">
<input type="number" id="numero2" placeholder="Digite o número 2">
```

E quatro botões:

```html
<button type="button" data-op="+">+</button>
<button type="button" data-op="-">-</button>
<button type="button" data-op="/">/</button>
<button type="button" data-op="*">*</button>
```

Cada botão possui o atributo:

```html
data-op
```

Ele informa qual operação aquele botão representa.

---

## Selecionando os Botões

Todos os elementos que possuem:

```html
data-op
```

são selecionados com:

```javascript
var botoesOperacao = document.querySelectorAll("[data-op]");
```

Isso cria uma coleção contendo os quatro botões.

Depois:

```javascript
for (var i = 0; i < botoesOperacao.length; i++)
```

percorre todos eles.

Para cada botão é adicionado um evento:

```javascript
botoesOperacao[i].addEventListener("click", function () {
```

Assim, todos os botões conseguem executar uma operação quando clicados.

---

## Identificando a Operação

Dentro do evento é utilizado:

```javascript
var operador = this.dataset.op;
```

O:

```javascript
this
```

representa o botão que foi clicado.

E:

```javascript
this.dataset.op
```

obtém o valor presente em:

```html
data-op
```

Por exemplo, ao clicar:

```html
<button data-op="+">+</button>
```

teremos:

```text
operador = "+"
```

---

# Operações Matemáticas

A operação é escolhida utilizando `if` e `else if`.

### Soma

```javascript
if (operador === "+") {
    resultado = n1 + n2;
}
```

### Subtração

```javascript
else if (operador === "-") {
    resultado = n1 - n2;
}
```

### Multiplicação

```javascript
else if (operador === "*") {
    resultado = n1 * n2;
}
```

### Divisão

```javascript
else if (operador === "/") {
    resultado = n1 / n2;
}
```

---

# Divisão por Zero

Antes de realizar a divisão, o programa verifica:

```javascript
if (n2 === 0) {
    resultadoCalculadora.textContent =
        "Não é possível dividir por zero";

    return;
}
```

Caso o segundo número seja zero, a divisão não é realizada.

O:

```javascript
return;
```

encerra a execução daquela função.

---

# Exibição do Resultado

Depois de realizar a operação:

```javascript
resultadoCalculadora.textContent =
    "Resultado: " + resultado;
```

Por exemplo:

```text
numero1 = 10
numero2 = 5
operador = +
```

O resultado será:

```text
Resultado: 15
```

---

# 3. Limpar a Tela

O HTML possui:

```html
<button type="reset" id="btnLimpar">
    Limpar Tela
</button>
```

Como o botão possui:

```html
type="reset"
```

os campos pertencentes ao formulário são limpos automaticamente.

O JavaScript também limpa os textos dos resultados:

```javascript
btnLimpar.addEventListener("click", function () {

    resultadoComparar.textContent = "";
    resultadoCalculadora.textContent = "";

});
```

Assim, tanto os campos quanto os resultados voltam ao estado inicial.

---

# Estilização

A aplicação utiliza CSS externo através do arquivo:

```text
style.css
```

Os elementos principais são apresentados como cards:

```css
.card,
.calculadora {
    background-color: #ffffff;

    border-radius: 12px;

    padding: 20px;

    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}
```

---

## Flexbox

O formulário utiliza:

```css
form {
    display: flex;
    flex-direction: column;
    gap: 20px;
}
```

Isso organiza os cards verticalmente.

Na calculadora, os botões são organizados com:

```css
.operacoes {
    display: flex;
    gap: 8px;
}
```

Assim, os quatro botões ficam lado a lado.

---

## Efeito Hover

Os botões possuem alteração visual quando o mouse passa sobre eles.

Por exemplo:

```css
#btnComparar:hover {
    background-color: #3448c5;
}
```

Também existe o efeito nos botões da calculadora:

```css
.operacoes button:hover {
    background-color: #d9e2f7;
}
```

---

# Principais Conceitos de JavaScript Utilizados

```text
JavaScript
│
├── var
│
├── Number()
│
├── getElementById()
│
├── querySelectorAll()
│
├── addEventListener()
│
├── .value
│
├── .textContent
│
├── .dataset
│
├── this
│
├── if
│
├── else if
│
├── else
│
├── for
└── return
```

---

# Fluxo da Aplicação

```text
                 TAREFA 3
                    |
        +-----------+-----------+
        |                       |
        v                       v
  Maior Valor              Calculadora
        |                       |
        v                       v
 valor1 + valor2          numero1 + numero2
        |                       |
        v                       v
    Comparar             escolhe operação
        |                  +  -  *  /
        v                       |
 if / else if / else            v
        |                   calcula
        v                       |
 mostra resultado               v
                         mostra resultado


                    |
                    v
               Limpar Tela
                    |
          +---------+---------+
          |                   |
          v                   v
     limpa campos       limpa resultados
```

---

# Exemplo

## Comparação

Valores:

```text
Primeiro valor: 15
Segundo valor: 8
```

Resultado:

```text
O maior valor é 15
```

## Calculadora

Valores:

```text
Número 1: 10
Número 2: 5
```

Ao clicar em:

```text
*
```

Resultado:

```text
Resultado: 50
```

---

# PROPOSTA

<img width="953" height="474" alt="image" src="https://github.com/user-attachments/assets/bfa393e4-d0ee-471a-b984-1bca877561f6" />

---

# RESULTADO

<!-- Coloque aqui uma imagem da aplicação funcionando -->

<img width="616" height="669" alt="image" src="https://github.com/user-attachments/assets/a31f8af6-3fec-4232-bf94-cbd52b17acb8" />

---
