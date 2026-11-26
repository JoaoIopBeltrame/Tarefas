function carregar() {
    fetch("http://localhost/tarefa2/index.php")
        .then(res => res.json())
        .then(dados => {
            let html = '';
            dados.forEach(item => {
                html += `<tr>
                    <td>${item.nome}</td>
                    <td>${item.idade}</td>
                    <td>${item.timestamp}</td>
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

    fetch("http://localhost/tarefa2/index.php", {
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