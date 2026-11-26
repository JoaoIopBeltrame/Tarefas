<?php
header('Content-Type: application/json');

$json = file_get_contents('php://input');
$dados = json_decode($json, true);

if (!$dados) {
    echo json_encode([
        'sucesso' => false,
        'mensagem' => 'Nenhum dado recebido'
    ]);
    exit;
}

$erros = [];

if (empty($dados['nome']) || strlen($dados['nome']) < 3) {
    $erros[] = 'Nome deve ter no mínimo 3 caracteres';
}

if (empty($dados['mail']) || !filter_var($dados['mail'], FILTER_VALIDATE_EMAIL)) {
    $erros[] = 'E-mail inválido';
}

if (empty($dados['password']) || strlen($dados['password']) < 6) {
    $erros[] = 'Senha deve ter no mínimo 6 caracteres';
}

$cpf_limpo = preg_replace('/\D/', '', $dados['cpf']);
if (empty($dados['cpf']) || strlen($cpf_limpo) !== 11) {
    $erros[] = 'CPF deve ter 11 dígitos';
}

if (empty($dados['idade']) || $dados['idade'] < 1 || $dados['idade'] > 100) {
    $erros[] = 'Idade deve estar entre 1 e 100 anos';
}

if (!empty($erros)) {
    echo json_encode([
        'sucesso' => false,
        'mensagem' => implode(', ', $erros)
    ]);
    exit;
}

$arquivo = 'usuarios.json';

if (file_exists($arquivo)) {
    $conteudo = file_get_contents($arquivo);
    $usuarios = json_decode($conteudo, true);
    if (!is_array($usuarios)) {
        $usuarios = [];
    }
} else {
    $usuarios = [];
}

$dados['data_cadastro'] = date('d/m/Y H:i:s');

$usuarios[] = $dados;

$sucesso = file_put_contents(
    $arquivo, 
    json_encode($usuarios, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE)
);

if ($sucesso) {
    echo json_encode([
        'sucesso' => true,
        'mensagem' => 'Dados salvos com sucesso'
    ]);
} else {
    echo json_encode([
        'sucesso' => false,
        'mensagem' => 'Erro ao escrever no arquivo. Verifique as permissões.'
    ]);
}