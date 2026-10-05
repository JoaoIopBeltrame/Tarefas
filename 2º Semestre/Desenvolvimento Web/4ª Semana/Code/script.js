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


const corpoTabela = document.getElementById("corpo-tabela");

const listaCards = document.getElementById("lista-cards");


corpoTabela.innerHTML = aplicativos.map((app) => {
    return `
        <tr>
            <td>${app.id_aplicativo}</td>

            <td>${app.nome}</td>

            <td>${app.descricao}</td>
        </tr>
    `;
}).join("");


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
