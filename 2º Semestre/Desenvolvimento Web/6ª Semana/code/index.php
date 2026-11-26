<?php

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: *");

if($_SERVER['REQUEST_METHOD'] == 'POST') {
    $jsonInput = file_get_contents('php://input');
    $data = json_decode($jsonInput, true);

    $nome = $data['nome'] ?? "sem nome";
    $idade = $data['idade'] ?? "sem idade";

    date_default_timezone_set('America/Sao_Paulo');
    $arrayData = [
        "timestamp" => date("Y-m-d H:i:s"),
        "nome" => $nome,
        "idade" => $idade
    ];

    $dados = file_exists("cadastro-dados.json") ? file_get_contents("cadastro-dados.json") : "[]";
    $lista = json_decode($dados, true);

    if(!is_array($lista)) {
        $lista = [];
    }

    $lista[] = $arrayData;

    $jsonString = json_encode($lista, JSON_PRETTY_PRINT);
    file_put_contents('cadastro-dados.json', $jsonString);

    echo json_encode([
        "status" => "success",
        "message" => "Dados salvos"
    ]);
}

if($_SERVER['REQUEST_METHOD'] == 'GET') {
    if(file_exists("cadastro-dados.json")){
        echo file_get_contents("cadastro-dados.json");
    } else {
        echo json_encode([]);
    }
}

?>
