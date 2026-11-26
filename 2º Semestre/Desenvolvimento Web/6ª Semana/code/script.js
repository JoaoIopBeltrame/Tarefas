function escapar(valor) {
    const div = document.createElement("div");
    div.textContent = valor;
    return div.innerHTML;
}

function carregar() {
    fetch("index.php")
        .then(res => res.json())
        .then(dados => {
            if (dados.length === 0) {
                document.getElementById("corpo").innerHTML = '<tr><td colspan="3">Sem dados</td></tr>';
                return;
            }
            let html = '';
            dados.forEach(item => {
                html += `<tr>
                    <td>${escapar(item.nome)}</td>
                    <td>${escapar(item.idade)}</td>
                    <td>${escapar(item.timestamp)}</td>
                </tr>`;
            });
            document.getElementById("corpo").innerHTML = html;
        })
        .catch(erro => {
            document.getElementById("corpo").innerHTML = '<tr><td colspan="3">Erro ao carregar dados</td></tr>';
        });
}

document.getElementById("btnEnviar").onclick = function() {
    const nome = document.getElementById("inptNome").value;
    const idade = document.getElementById("inptIdade").value;

    if(!nome || !idade) {
        alert("Preencha nome e idade");
        return;
    }

    const dados = {
        nome: nome,
        idade: idade
    };

    fetch("index.php", {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(dados)
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("inptNome").value = '';
        document.getElementById("inptIdade").value = '';
        carregar();
    })
    .catch(erro => alert("Erro ao enviar"));
};

carregar();
