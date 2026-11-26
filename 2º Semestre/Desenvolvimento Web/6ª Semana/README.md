# Ler e Mostrar Dados com Fetch e PHP

Uma aplicação desenvolvida em HTML, CSS, JavaScript e PHP para cadastrar nome e idade e exibir os dados salvos em uma tabela.

Os dados são salvos pelo PHP em um arquivo JSON. Ao carregar a página, o JavaScript busca esses dados através do `fetch()` e gera automaticamente as linhas da tabela com `forEach()`, template strings e `innerHTML`.

O mesmo arquivo `index.php` atende às duas operações: o método `POST` salva um novo cadastro e o método `GET` devolve os cadastros salvos.

## Funcionalidades

- **Cadastro de Dados:** Solicita o nome e a idade.
- **Validação no JavaScript:** Impede o envio quando algum campo está vazio.
- **Envio com fetch():** Envia os dados em formato JSON pelo método `POST`.
- **Leitura com fetch():** Busca os dados salvos pelo método `GET`.
- **Carregamento Automático:** Os dados são buscados quando a página é aberta.
- **Atualização da Tabela:** Após um envio bem-sucedido, a tabela é carregada novamente sem recarregar a página.
- **Tabela Dinâmica:** As linhas são geradas automaticamente pelo JavaScript.
- **Exibição Segura:** Os valores são convertidos em texto antes de entrar na tabela.
- **Armazenamento em JSON:** Cada cadastro é adicionado ao arquivo `cadastro-dados.json`.
- **Data de Cadastro:** O PHP registra a data e a hora no horário de São Paulo.
- **CORS:** O PHP permite requisições de outras origens.
- **Arquivo Inexistente:** Em uma requisição `GET`, o PHP responde `[]` se o arquivo ainda não existir.
- **Mensagem de Sem Dados:** A tabela exibe "Sem dados" quando não há cadastros.
- **Erro de Carregamento:** Uma mensagem é exibida na tabela se a busca falhar.
- **Tabela Zebrada:** As linhas pares possuem uma cor de fundo diferente.
- **Efeito Hover:** As linhas da tabela e o botão mudam de cor ao passar o mouse.
- **Flexbox:** Utilizado para centralizar a aplicação e organizar o formulário.

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
- innerHTML
- fetch()
- CORS
- Flexbox
- :nth-child()
- :hover

## Estrutura do Projeto

```text
Tarefa/
│
├── index.html
├── style.css
├── script.js
├── index.php
└── cadastro-dados.json
```

## Como Executar

O projeto precisa de um servidor com PHP.

1. Coloque a pasta do projeto na pasta pública do servidor. No XAMPP, por exemplo, é a pasta `htdocs`.
2. Inicie o servidor (no XAMPP, o Apache).
3. Acesse o `index.html` pelo servidor. Com a pasta chamada `Tarefa`, o endereço é `http://localhost/Tarefa/index.html`.

Informe o `index.html` no endereço, pois a pasta também possui um `index.php`.

O JavaScript acessa o PHP pelo caminho relativo `index.php`, por isso os arquivos devem ficar na mesma pasta.

> **Atenção:** o GitHub Pages não executa PHP. Para o projeto funcionar por um link na internet, é necessária uma hospedagem com suporte a PHP e permissão para gravar no `cadastro-dados.json`.

## Código HTML

O arquivo `index.html` contém a estrutura principal da aplicação.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ler e Mostrar Dados</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Dados Salvos</h1>
        
        <div class="formulario">
            <input type="text" id="inptNome" placeholder="Nome">
            <input type="text" id="inptIdade" placeholder="Idade">
            <button id="btnEnviar">Enviar</button>
        </div>

        <table id="tabela">
            <thead>
                <tr>
                    <th>Nome</th>
                    <th>Idade</th>
                    <th>Data</th>
                </tr>
            </thead>
            <tbody id="corpo">
            </tbody>
        </table>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

A tabela possui apenas o cabeçalho escrito diretamente no HTML.

O corpo:

```html
<tbody id="corpo">
</tbody>
```

começa vazio, pois será preenchido pelo JavaScript com os dados salvos.

## Busca dos Dados

A função `carregar()` busca os dados no PHP:

```javascript
function carregar() {
    fetch("index.php")
        .then(res => res.json())
```

Quando nenhum método é informado, o `fetch()` utiliza o `GET`.

O `res.json()` converte a resposta em um array de objetos JavaScript.

No final do `script.js`, a função é chamada para carregar os dados assim que o script é executado:

```javascript
carregar();
```

## Geração da Tabela

Com os dados recebidos, o JavaScript monta as linhas da tabela:

Primeiro, o código verifica se o array está vazio:

```javascript
            if (dados.length === 0) {
                document.getElementById("corpo").innerHTML = '<tr><td colspan="3">Sem dados</td></tr>';
                return;
            }
```

Nesse caso, a tabela exibe a mensagem "Sem dados", e o `return` encerra a função.

Quando existem cadastros, as linhas são montadas:

```javascript
            let html = '';
            dados.forEach(item => {
                html += `<tr>
                    <td>${escapar(item.nome)}</td>
                    <td>${escapar(item.idade)}</td>
                    <td>${escapar(item.timestamp)}</td>
                </tr>`;
            });
            document.getElementById("corpo").innerHTML = html;
```

Cada objeto do array gera automaticamente uma nova linha:

```html
<tr>
    <td>Nome</td>
    <td>Idade</td>
    <td>Data</td>
</tr>
```

Assim, as linhas não precisam ser escritas manualmente no HTML.

## Funcionamento do forEach()

O método:

```javascript
forEach()
```

percorre todos os elementos do array.

Neste projeto:

```javascript
dados.forEach(item => {
```

cada cadastro é representado temporariamente por:

```javascript
item
```

Permitindo acessar:

```javascript
item.nome
item.idade
item.timestamp
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
<td>${escapar(item.nome)}</td>
```

Se o nome cadastrado for:

```text
Maria
```

o HTML gerado será:

```html
<td>Maria</td>
```

O operador `+=` acrescenta cada nova linha ao texto que já estava armazenado na variável `html`.

## Funcionamento do innerHTML

Depois que todas as linhas são montadas, o `innerHTML` as insere dentro do corpo da tabela:

```javascript
document.getElementById("corpo").innerHTML = html;
```

Portanto, o fluxo de exibição é:

```text
fetch() com GET
  ↓
res.json()
  ↓
Array
  ↓
forEach()
  ↓
Template Strings
  ↓
innerHTML
  ↓
Tabela
```

## Exibição Segura do Texto

Como as linhas são inseridas com `innerHTML`, um código HTML digitado no nome poderia ser interpretado pelo navegador. Para evitar isso, cada valor passa pela função `escapar()`:

```javascript
function escapar(valor) {
    const div = document.createElement("div");
    div.textContent = valor;
    return div.innerHTML;
}
```

O `textContent` trata o valor como texto comum. Em seguida, o `innerHTML` devolve esse texto com os caracteres especiais, como `<` e `>`, convertidos. Assim, o conteúdo aparece na tabela como texto.

> **Observação:** este é um projeto didático. Não há login, então quem tiver acesso ao endereço pode ver e enviar dados. Utilize apenas dados de teste.

## Erro ao Carregar

Se a requisição falhar ou o processamento da resposta gerar um erro, o `catch()` exibe uma mensagem na tabela:

```javascript
        .catch(erro => {
            document.getElementById("corpo").innerHTML = '<tr><td colspan="3">Erro ao carregar dados</td></tr>';
        });
```

O `colspan="3"` faz a célula ocupar as três colunas.

## Validação no JavaScript

Ao clicar no botão, o JavaScript obtém os valores digitados:

```javascript
document.getElementById("btnEnviar").onclick = function() {
    const nome = document.getElementById("inptNome").value;
    const idade = document.getElementById("inptIdade").value;
```

Depois, verifica se os dois campos foram preenchidos:

```javascript
    if(!nome || !idade) {
        alert("Preencha nome e idade");
        return;
    }
```

O `return` interrompe a função, e os dados não são enviados.

Essa validação verifica apenas se os campos estão vazios. Ela não confere se a idade é um número nem impede o preenchimento somente com espaços.

## Envio dos Dados

Os valores são reunidos em um objeto:

```javascript
    const dados = {
        nome: nome,
        idade: idade
    };
```

Depois, são enviados para o PHP:

```javascript
    fetch("index.php", {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(dados)
    })
```

| Parte | Função |
| --- | --- |
| `method: "POST"` | Define o método de envio |
| `Content-Type` | Informa que o conteúdo enviado é JSON |
| `JSON.stringify()` | Converte o objeto JavaScript em texto JSON |

Quando a resposta é recebida, os campos são limpos e a tabela é atualizada:

```javascript
    .then(res => res.json())
    .then(data => {
        document.getElementById("inptNome").value = '';
        document.getElementById("inptIdade").value = '';
        carregar();
    })
    .catch(erro => alert("Erro ao enviar"));
```

## Liberação do CORS

No início do `index.php`:

```php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: *");
```

| Cabeçalho | Função |
| --- | --- |
| `Access-Control-Allow-Origin` | Permite que outras origens acessem a resposta |
| `Access-Control-Allow-Headers` | Permite os cabeçalhos enviados na requisição, como o `Content-Type` |

O `*` libera o acesso para qualquer origem, o que é usado aqui para fins de estudo.

## Salvando os Dados (POST)

O PHP identifica o método da requisição:

```php
if($_SERVER['REQUEST_METHOD'] == 'POST') {
```

Depois, lê os dados enviados pelo `fetch()`:

```php
    $jsonInput = file_get_contents('php://input');
    $data = json_decode($jsonInput, true);

    $nome = $data['nome'] ?? "sem nome";
    $idade = $data['idade'] ?? "sem idade";
```

O operador `??` define um valor padrão quando a informação não existe ou é `null`. O PHP não faz outras validações, como verificar se o texto está vazio.

Em seguida, cria o novo cadastro com a data e a hora:

```php
    date_default_timezone_set('America/Sao_Paulo');
    $arrayData = [
        "timestamp" => date("Y-m-d H:i:s"),
        "nome" => $nome,
        "idade" => $idade
    ];
```

Os cadastros anteriores são lidos, o novo item é adicionado ao final e a lista é gravada novamente:

```php
    $dados = file_exists("cadastro-dados.json") ? file_get_contents("cadastro-dados.json") : "[]";
    $lista = json_decode($dados, true);

    if(!is_array($lista)) {
        $lista = [];
    }

    $lista[] = $arrayData;

    $jsonString = json_encode($lista, JSON_PRETTY_PRINT);
    file_put_contents('cadastro-dados.json', $jsonString);
```

O `JSON_PRETTY_PRINT` formata o arquivo para facilitar a leitura.

Se o arquivo ainda não existir, o PHP utiliza `[]` como conteúdo inicial, e o arquivo é criado na gravação.

Por fim, o PHP devolve uma resposta em JSON:

```php
    echo json_encode([
        "status" => "success",
        "message" => "Dados salvos"
    ]);
```

## Lendo os Dados (GET)

Na requisição `GET`, o PHP verifica se o arquivo existe e devolve o seu conteúdo:

```php
if($_SERVER['REQUEST_METHOD'] == 'GET') {
    if(file_exists("cadastro-dados.json")){
        echo file_get_contents("cadastro-dados.json");
    } else {
        echo json_encode([]);
    }
}
```

| Função | O que faz |
| --- | --- |
| `file_exists()` | Confere se o arquivo existe |
| `file_get_contents()` | Lê o conteúdo do arquivo |
| `echo` | Devolve a resposta |
| `json_encode([])` | Gera o array vazio `[]` |

## Arquivo JSON

Cada cadastro possui três propriedades:

| Propriedade | Função |
| --- | --- |
| `timestamp` | Data e hora do cadastro |
| `nome` | Nome informado |
| `idade` | Idade informada |

Exemplo (dados fictícios):

```json
[
    {
        "timestamp": "2026-11-26 14:30:00",
        "nome": "Maria",
        "idade": "20"
    }
]
```

## Layout com Flexbox

O Flexbox centraliza a aplicação na tela:

```css
body {
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
}
```

Ele também organiza os inputs e o botão em uma linha:

```css
.formulario {
    display: flex;
    gap: 10px;
    margin-bottom: 30px;
}
```

Os inputs utilizam `flex: 1` para dividir o espaço disponível.

## Estilização do Container

```css
.container {
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    max-width: 600px;
    width: 100%;
}
```

Isso define o fundo, o espaçamento interno, o arredondamento, a sombra e a largura da área principal.

## Efeito Hover no Botão

```css
button:hover {
    background-color: #764ba2;
}
```

Quando o mouse passa sobre o botão, sua cor de fundo é alterada.

## Estilização da Tabela

```css
table {
    width: 100%;
    border-collapse: collapse;
}
```

O `border-collapse: collapse` remove o espaço entre as bordas das células.

## Tabela Zebrada e Hover

```css
tbody tr:nth-child(even) {
    background-color: #f9f9f9;
}

tbody tr:hover {
    background-color: #f5f5f5;
}
```

O `:nth-child(even)` seleciona as linhas pares.

O `:hover` altera a cor da linha quando o mouse passa sobre ela. Como as duas regras têm a mesma especificidade, a regra `:hover` é declarada depois para funcionar também nas linhas pares.

## Fluxo da Aplicação

```text
Página é aberta
       │
       ▼
script.js é executado
       │
       ▼
   carregar()  ◄───────────────────┐
       │                           │
       ▼                           │
 fetch() com GET                   │
       │                           │
       ▼                           │
   index.php                       │
       │                           │
       ▼                           │
 Dados em JSON ou []               │
       │                           │
       ▼                           │
 Há dados salvos?                  │
       │                           │
       ├── Não ──► "Sem dados"     │
       │                           │
       ▼ Sim                       │
 forEach() + innerHTML             │
       │                           │
       ▼                           │
     TABELA                        │
                                   │
Usuário clica em Enviar            │
       │                           │
       ▼                           │
Validação no JavaScript            │
       │                           │
       ▼                           │
 fetch() com POST                  │
       │                           │
       ▼                           │
   index.php                       │
       │                           │
       ▼                           │
cadastro-dados.json                │
       │                           │
       ▼                           │
Campos são limpos ─────────────────┘
```

O diagrama mostra o fluxo de um cadastro bem-sucedido. Se algum campo estiver vazio, o envio é interrompido.

## Métodos Utilizados

| Método | Função | Quando acontece |
| --- | --- | --- |
| `GET` | Ler os dados salvos | Ao abrir a página e após um envio bem-sucedido |
| `POST` | Salvar um novo cadastro | Ao clicar em Enviar com os campos preenchidos |

## Conceitos Praticados

```text
HTML
├── table
├── thead
├── tbody
├── tr
├── th
├── div
├── input
├── button
└── script

CSS
├── Flexbox
├── box-sizing
├── nth-child
├── hover
├── linear-gradient
├── box-shadow
├── border-radius
└── border-collapse

JavaScript
├── function
├── const
├── let
├── Array
├── Objetos
├── getElementById()
├── createElement()
├── textContent
├── onclick
├── forEach()
├── Template Strings
├── innerHTML
├── JSON.stringify()
└── fetch()

PHP
├── header()
├── $_SERVER
├── file_get_contents()
├── json_decode()
├── json_encode()
├── is_array()
├── file_exists()
├── file_put_contents()
├── date()
└── date_default_timezone_set()
```

## PROPOSTA

<img width="510" height="255" alt="image" src="https://github.com/user-attachments/assets/8b0d9a14-d857-4a75-a190-c60bb33c27d7" />

## RESULTADO
<img width="708" height="349" alt="image" src="https://github.com/user-attachments/assets/99c8878a-9098-4251-bb32-56ca86acd0f8" />
