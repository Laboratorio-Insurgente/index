<?php
// Verifica se o formulário foi submetido
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Verifica se o campo de e-mail foi preenchido
    if (isset($_POST['email'])) {
        // Limpa e valida o e-mail
        $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);

        // Verifica se o e-mail é válido
        if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
            // Caminho para o arquivo CSV onde os e-mails serão armazenados
            $arquivo = 'emails.csv';

            // Abre o arquivo em modo de "acrescentar" (append) e trava o arquivo para evitar acessos simultâneos
            $file = fopen($arquivo, 'a');

            if ($file) {
                // Grava o e-mail no arquivo CSV com a data/hora atual
                $data_atual = date('Y-m-d H:i:s');
                fputcsv($file, [$email, $data_atual]);

                // Fecha o arquivo
                fclose($file);

                // Mensagem de sucesso
                echo "Obrigado por se inscrever!";
            } else {
                // Caso o arquivo não possa ser aberto
                echo "Erro ao salvar o e-mail.";
            }
        } else {
            // Se o e-mail for inválido
            echo "E-mail inválido. Por favor, insira um e-mail válido.";
        }
    } else {
        // Se o campo de e-mail estiver vazio
        echo "Por favor, insira um e-mail.";
    }
}
?>