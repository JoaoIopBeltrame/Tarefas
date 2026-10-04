var btnComparar = document.getElementById("btnComparar");
var resultadoComparar = document.getElementById("resultadoComparar");
var resultadoCalculadora = document.getElementById("resultado");

btnComparar.addEventListener("click", function () {

    var v1 = Number(document.getElementById("valor1").value);
    var v2 = Number(document.getElementById("valor2").value);

    var mensagem;

    if (v1 > v2) {
        mensagem = "O maior valor é " + v1;
    }
    else if (v2 > v1) {
        mensagem = "O maior valor é " + v2;
    }
    else {
        mensagem = "Os valores são iguais";
    }

    resultadoComparar.textContent = mensagem;
});


var botoesOperacao = document.querySelectorAll("[data-op]");

for (var i = 0; i < botoesOperacao.length; i++) {

    botoesOperacao[i].addEventListener("click", function () {

        var n1 = Number(document.getElementById("numero1").value);
        var n2 = Number(document.getElementById("numero2").value);

        var operador = this.dataset.op;
        var resultado;

        if (operador === "+") {
            resultado = n1 + n2;
        }
        else if (operador === "-") {
            resultado = n1 - n2;
        }
        else if (operador === "*") {
            resultado = n1 * n2;
        }
        else if (operador === "/") {

            if (n2 === 0) {
                resultadoCalculadora.textContent =
                    "Não é possível dividir por zero";

                return;
            }

            resultado = n1 / n2;
        }

        resultadoCalculadora.textContent =
            "Resultado: " + resultado;
    });
}


var btnLimpar = document.getElementById("btnLimpar");

btnLimpar.addEventListener("click", function () {

    resultadoComparar.textContent = "";
    resultadoCalculadora.textContent = "";

});