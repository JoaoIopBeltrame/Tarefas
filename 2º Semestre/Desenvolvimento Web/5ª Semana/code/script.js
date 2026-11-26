const inputs = [
    {id: "nome", icon: "fa-user", type: "text", label: "Nome", minlength: 3, maxlength: 100},  
    {id: "mail", icon: "fa-envelope", type: "email", label: "E-mail", minlength: 6, maxlength: 100}, 
    {id: "password", icon: "fa-lock", type: "password", label: "Senha", minlength: 6, maxlength: 100},  
    {id: "cpf", icon: "fa-id-card", type: "text", label: "CPF", minlength: 11, maxlength: 14},  
    {id: "idade", icon: "fa-birthday-cake", type: "number", label: "Idade", max: 100}  
];

const form = document.getElementById('ask-data');

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

const btnSubmit = document.querySelector('.btn-send');

btnSubmit.addEventListener('click', function(event) {
    event.preventDefault();
    
    const nome = document.getElementById('nome').value;
    const mail = document.getElementById('mail').value;
    const password = document.getElementById('password').value;
    const cpf = document.getElementById('cpf').value;
    const idade = document.getElementById('idade').value;
    
    const dados = {
        nome: nome,
        mail: mail,
        password: password,
        cpf: cpf,
        idade: idade
    };
    
    fetch('save.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados)
    })
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
});
