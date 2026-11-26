# Formulário Dinâmico com Fetch e PHP

Uma aplicação desenvolvida em HTML, CSS, JavaScript e PHP para cadastrar dados de usuários através de um formulário gerado de forma dinâmica.

As configurações dos campos são armazenadas em um array de objetos no JavaScript e utilizadas para gerar automaticamente o formulário através de `forEach()`, `createElement()`, template strings, `innerHTML` e `appendChild()`.

Os dados preenchidos são enviados para o PHP via `fetch()` utilizando o método `POST`. No servidor, eles são validados e salvos em um arquivo JSON.

## Funcionalidades

- **Formulário de Usuário:** Solicita nome, e-mail, senha, CPF e idade.
- **Array de Objetos:** Cada campo possui ID, ícone, tipo, rótulo e limites.
- **Formulário Dinâmico:** Os campos são gerados automaticamente pelo JavaScript.
- **Template Strings:** Utilizadas para montar elementos HTML dentro do JavaScript.
- **Uso de forEach():** Percorre todos os objetos do array.
- **Uso de createElement():** Cria uma `div` para cada campo.
- **Uso de innerHTML:** Insere o ícone, o rótulo e o input dentro de cada `div`.
- **Uso de appendChild():** Adiciona cada `div` ao formulário.
- **Envio com fetch():** Envia os dados em formato JSON pelo método `POST`, sem recarregar a página.
- **Validação no Servidor:** O PHP verifica os dados antes de salvar.
- **Armazenamento em JSON:** Cada cadastro é adicionado ao arquivo `usuarios.json`.
- **Data de Cadastro:** O PHP registra a data e a hora de cada cadastro.
- **Mensagens de Retorno:** Um `alert()` informa o sucesso ou o erro.
- **Efeitos Visuais:** Os inputs e o botão reagem à interação do usuário.
- **Flexbox:** Utilizado para centralizar e organizar o formulário.

## Tecnologias Utilizadas

- HTML5
- CSS3
- JavaScript
- PHP
- JSON
- Arrays
- Objetos
- DOM
- Template Strings
- forEach()
- createElement()
- innerHTML
- appendChild()
- fetch()
- Flexbox
- Font Awesome
- :focus
- :hover
- :active

## Estrutura do Projeto

```text
projeto/
│
├── index.html
├── style.css
├── script.js
├── save.php
└── usuarios.json
```

## Como Executar

Como o projeto utiliza PHP, ele precisa ser aberto através de um servidor. Abrir o `index.html` com dois cliques não executa o `save.php`.

Com o PHP instalado, execute dentro da pasta do projeto:

```bash
php -S localhost:8000
```

Depois acesse `http://localhost:8000` no navegador.

Os ícones são carregados pela internet, através do Font Awesome.

## Código HTML

O arquivo `index.html` contém a estrutura principal da aplicação.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"/>
    <link rel="stylesheet" href="style.css">
    <title>Formulário Dinâmico</title>
</head>
<body>
    <div class="container" id="container">
        <h1>Digite suas informações</h1>
        <form id="ask-data">

        </form>
        <button class="btn-send" type="submit" form="ask-data">Enviar</button>
    </div>

    <script src="script.js" defer></script>
</body>
</html>
```

O formulário:

```html
<form id="ask-data">

</form>
```

começa vazio, pois será preenchido automaticamente pelo JavaScript.

O botão fica fora do formulário, mas continua ligado a ele através do atributo:

```html
form="ask-data"
```

## Array de Campos

As configurações dos campos são armazenadas dentro de um array de objetos:

```javascript
const inputs = [
    {id: "nome", icon: "fa-user", type: "text", label: "Nome", minlength: 3, maxlength: 100},  
    {id: "mail", icon: "fa-envelope", type: "email", label: "E-mail", minlength: 6, maxlength: 100}, 
    {id: "password", icon: "fa-lock", type: "password", label: "Senha", minlength: 6, maxlength: 100},  
    {id: "cpf", icon: "fa-id-card", type: "text", label: "CPF", minlength: 11, maxlength: 14},  
    {id: "idade", icon: "fa-birthday-cake", type: "number", label: "Idade", max: 100}  
];
```

Cada objeto pode possuir as seguintes propriedades:

| Propriedade | Função |
| --- | --- |
| `id` | Identificação do campo |
| `icon` | Ícone do Font Awesome |
| `type` | Tipo do input |
| `label` | Texto exibido ao lado do campo |
| `minlength` | Quantidade mínima de caracteres |
| `maxlength` | Quantidade máxima de caracteres |
| `max` | Maior valor do campo numérico |

## Geração do Formulário

Primeiro, o JavaScript seleciona o formulário:

```javascript
const form = document.getElementById('ask-data');
```

Depois utiliza:

```javascript
inputs.forEach(campo => {
    const div = document.createElement('div');
    div.className = `send-${campo.id}`;
    
    div.innerHTML = `
        <i class="fa-solid ${campo.icon}"></i>
        <label for="${campo.id}">${campo.label}</label>
        <input
            type="${campo.type}"
            id="${campo.id}"
            ${campo.minlength ? `minlength="${campo.minlength}"` : ''}    
            ${campo.maxlength ? `maxlength="${campo.maxlength}"` : ''}    
            ${campo.max ? `max="${campo.max}"` : ''}
            required
        >
    `;
    form.appendChild(div);
});
```

Cada objeto do array gera automaticamente um novo campo:

```text
div.send-id
│
├── Ícone
├── Label
└── Input
```

Assim, os campos não precisam ser escritos manualmente no HTML.

## Funcionamento do forEach()

O método:

```javascript
forEach()
```

percorre todos os elementos do array.

Neste projeto:

```javascript
inputs.forEach(campo => {
```

cada objeto é representado temporariamente por:

```javascript
campo
```

Permitindo acessar:

```javascript
campo.id
campo.icon
campo.type
campo.label
campo.minlength
campo.maxlength
campo.max
```

## Criação dos Elementos

Para cada campo, o `createElement()` cria uma nova `div`:

```javascript
const div = document.createElement('div');
```

Ela recebe uma classe de acordo com o ID do campo:

```javascript
div.className = `send-${campo.id}`;
```

Por fim, o `appendChild()` coloca a `div` dentro do formulário:

```javascript
form.appendChild(div);
```

## Template Strings

As template strings são strings escritas utilizando crases:

```javascript
` `
```

Elas permitem inserir valores utilizando:

```javascript
${}
```

Por exemplo:

```javascript
<label for="${campo.id}">${campo.label}</label>
```

No campo de nome, o HTML gerado será:

```html
<label for="nome">Nome</label>
```

Também é utilizado o operador ternário, para adicionar um atributo somente quando a propriedade existe no objeto:

```javascript
${campo.max ? `max="${campo.max}"` : ''}
```

Neste projeto, apenas o campo de idade possui a propriedade `max`.

## Funcionamento do innerHTML

O `innerHTML` insere o conteúdo criado pela template string dentro de cada `div`:

```javascript
div.innerHTML = ...
```

Portanto, o fluxo de criação do formulário é:

```text
Array
  ↓
forEach()
  ↓
createElement()
  ↓
Template String
  ↓
innerHTML
  ↓
appendChild()
  ↓
Página
```

## Atributos dos Inputs

O JavaScript adiciona atributos HTML aos campos:

| Campo | Atributos |
| --- | --- |
| Nome | `required`, `minlength="3"`, `maxlength="100"` |
| E-mail | `required`, `minlength="6"`, `maxlength="100"` |
| Senha | `required`, `minlength="6"`, `maxlength="100"` |
| CPF | `required`, `minlength="11"`, `maxlength="14"` |
| Idade | `required`, `max="100"` |

Como o clique no botão utiliza `event.preventDefault()`, o envio nativo do formulário é cancelado. O `maxlength` continua limitando a digitação, mas `required`, `minlength`, `max` e o formato do e-mail não são verificados pelo navegador antes do `fetch()`. Quem impede o salvamento de dados inválidos é o `save.php`.

## Captura do Envio

O JavaScript seleciona o botão e aguarda o clique:

```javascript
const btnSubmit = document.querySelector('.btn-send');

btnSubmit.addEventListener('click', function(event) {
    event.preventDefault();
```

O `preventDefault()` impede o comportamento padrão do botão, evitando que a página seja recarregada.

## Criação do Objeto de Dados

O valor de cada campo é obtido através de `getElementById()` e da propriedade `value`:

```javascript
const nome = document.getElementById('nome').value;
```

Depois, os valores são reunidos em um único objeto:

```javascript
    const dados = {
        nome: nome,
        mail: mail,
        password: password,
        cpf: cpf,
        idade: idade
    };
```

## Envio com fetch()

Os dados são enviados para o arquivo `save.php`:

```javascript
    fetch('save.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados)
    })
```

| Parte | Função |
| --- | --- |
| `method: 'POST'` | Define o método de envio |
| `Content-Type` | Informa que o conteúdo enviado é JSON |
| `JSON.stringify()` | Converte o objeto JavaScript em texto JSON |

## Tratamento da Resposta

O PHP responde com um JSON, que é tratado pelo JavaScript:

```javascript
    .then(response => response.json())
    .then(data => {
        if (data.sucesso) {
            alert('✅ ' + data.mensagem);
            form.reset();
        } else {
            alert('❌ ' + data.mensagem);
        }
    })
    .catch(error => {
        alert('❌ Erro ao enviar os dados');
    });
```

- Em caso de **sucesso**, a mensagem é exibida e o formulário é limpo com `form.reset()`.
- Em caso de **erro retornado pelo PHP**, a mensagem de erro é exibida e o formulário continua preenchido.
- Se a requisição falhar ou a resposta não for um JSON válido, o `catch()` é executado.

## Recebimento no PHP

Primeiro, o PHP informa que a resposta será em JSON:

```php
header('Content-Type: application/json');
```

Depois, lê o conteúdo enviado pelo `fetch()`:

```php
$json = file_get_contents('php://input');
$dados = json_decode($json, true);
```

O `php://input` permite ler o corpo da requisição. O `json_decode()` converte o JSON em um array associativo.

Se nenhum dado for recebido, o PHP retorna uma mensagem de erro e encerra a execução com `exit`.

## Validação no PHP

Cada informação é verificada antes de ser salva:

| Campo | Regra |
| --- | --- |
| Nome | Obrigatório, com no mínimo 3 caracteres |
| E-mail | Obrigatório, em formato válido |
| Senha | Obrigatória, com no mínimo 6 caracteres |
| CPF | Obrigatório, com 11 dígitos |
| Idade | Obrigatória, entre 1 e 100 anos |

O e-mail é validado com `filter_var()`:

```php
if (empty($dados['mail']) || !filter_var($dados['mail'], FILTER_VALIDATE_EMAIL)) {
    $erros[] = 'E-mail inválido';
}
```

No CPF, o `preg_replace()` remove tudo o que não é número antes da contagem:

```php
$cpf_limpo = preg_replace('/\D/', '', $dados['cpf']);
```

A validação confere apenas a quantidade de dígitos do CPF, sem calcular os dígitos verificadores.

Os erros são armazenados no array `$erros`. Caso exista algum, o `implode()` junta as mensagens em um único texto e os dados não são salvos.

## Salvando no JSON

Se o arquivo `usuarios.json` existir, o PHP lê os cadastros anteriores. Caso contrário, começa com um array vazio.

Em seguida, a data do cadastro é adicionada e o novo usuário entra no final da lista:

```php
$dados['data_cadastro'] = date('d/m/Y H:i:s');

$usuarios[] = $dados;
```

Por fim, a lista é gravada no arquivo:

```php
$sucesso = file_put_contents(
    $arquivo, 
    json_encode($usuarios, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE)
);
```

| Opção | Função |
| --- | --- |
| `JSON_PRETTY_PRINT` | Formata o JSON para facilitar a leitura |
| `JSON_UNESCAPED_UNICODE` | Mantém os acentos legíveis |

Exemplo de um cadastro salvo (dados fictícios):

```json
[
    {
        "nome": "Maria Silva",
        "mail": "maria@example.com",
        "password": "senha123",
        "cpf": "000.000.000-00",
        "idade": "20",
        "data_cadastro": "26\/11\/2026 14:30:00"
    }
]
```

> **Observação:** este é um projeto didático. A senha é salva em texto puro e deve-se usar apenas dados de teste. Em uma aplicação real, a senha deveria ser protegida com `password_hash()` e o arquivo de dados não poderia ser acessado publicamente.

## Layout com Flexbox

O Flexbox centraliza o formulário na tela:

```css
body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(135deg, #e8f4f8 0%, #f0e8f8 100%);
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}
```

- `display: flex`: ativa o Flexbox.
- `justify-content: center`: centraliza horizontalmente.
- `align-items: center`: centraliza verticalmente.
- `height: 100vh`: faz o `body` ocupar a altura da tela.

No formulário, os campos são organizados em coluna:

```css
.container form {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}
```

O `gap: 16px` cria um espaço de 16px entre os campos.

## Estilização do Container

O container possui:

```css
.container {
  width: 500px;
  background: white;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  padding: 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}
```

Isso define a largura, o fundo, o arredondamento, a sombra, o espaçamento e o alinhamento do conteúdo.

## Estilização dos Campos

Para estilizar todas as `div` dos campos de uma só vez, o CSS utiliza um seletor de atributo:

```css
.container [class^=send-] {
  width: 100%;
  max-width: 300px;
  display: flex;
  align-items: center;
  gap: 10px;
}
```

O `[class^=send-]` seleciona os elementos cujo atributo `class` começa com `send-`.

## Efeitos nos Inputs

Quando o campo está selecionado:

```css
.container input:focus {
  outline: none;
  border-color: #7b9bc1;
  box-shadow: 0 0 0 2px rgba(123, 155, 193, 0.1);
}
```

Quando o mouse passa sobre o campo:

```css
.container input:hover {
  border-color: #b5c8da;
}
```

## Efeitos no Botão

Quando o mouse passa sobre o botão:

```css
.container .btn-send:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(123, 155, 193, 0.3);
}
```

O `translateY(-2px)` move o botão levemente para cima.

Quando o botão é pressionado:

```css
.container .btn-send:active {
  transform: translateY(0);
}
```

o botão volta para a posição original.

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
Array de campos
       │
       ▼
forEach() gera o formulário
       │
       ▼
Usuário preenche e clica em Enviar
       │
       ▼
Objeto com os dados
       │
       ▼
JSON.stringify()
       │
       ▼
fetch() com POST
       │
       ▼
    save.php
       │
       ▼
Validação dos dados
       │
       ├──────────────────────┐
       │                      │
       ▼                      ▼
    Válidos               Inválidos
       │                      │
       ▼                      │
 usuarios.json                │
       │                      │
       ▼                      ▼
Mensagem de sucesso    Mensagem de erro
```

O diagrama mostra o fluxo principal. Se houver falha na gravação do arquivo, o PHP também retorna uma mensagem de erro.

## Campos Utilizados

| ID | Campo | Tipo |
| --- | --- | --- |
| `nome` | Nome | `text` |
| `mail` | E-mail | `email` |
| `password` | Senha | `password` |
| `cpf` | CPF | `text` |
| `idade` | Idade | `number` |

## Conceitos Praticados

```text
HTML
├── form
├── button
├── div
├── label
├── input
└── script

CSS
├── Flexbox
├── Seletor de atributo
├── focus
├── hover
├── active
├── linear-gradient
├── box-shadow
├── border-radius
├── transform
└── transition

JavaScript
├── const
├── Array
├── Objetos
├── getElementById()
├── querySelector()
├── forEach()
├── createElement()
├── Template Strings
├── Operador ternário
├── innerHTML
├── appendChild()
├── addEventListener()
├── preventDefault()
├── JSON.stringify()
└── fetch()

PHP
├── header()
├── file_get_contents()
├── json_decode()
├── empty()
├── strlen()
├── filter_var()
├── preg_replace()
├── implode()
├── file_exists()
├── date()
├── json_encode()
└── file_put_contents()
```

## PROPOSTA

<img width="569" height="181" alt="image" src="https://github.com/user-attachments/assets/6c314a0c-65f7-49f6-9afc-e053a7d4aea5" />

## RESULTADO

<img width="1927" height="984" alt="image" src="https://github.com/user-attachments/assets/5d05d0d6-b0c7-464a-b873-ff2150ede8f8" />
