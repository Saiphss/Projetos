<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Formulário</title>
</head>

<body>
    <section id="esquerda" class="bodySection">
        <form class="form" action="processa.php" method="post">
            <div class="formBox">
                <h2 class="title">Cadastre-se</h2>
                <div class="inputBox">
                    <label for="nome">Nome</label>
                    <input type="text" autocomplete="off" name="nome_cliente" id="nomeCliente" required maxlength="40" size="40">
                    <span></span>
                    <i></i>
                </div>
                <div class="inputBox">
                    <label for="cpf_cliente">CPF</label>
                    <input type="text" autocomplete="off" name="cpf_cliente" id="cpfCliente" minlength="11" maxlength="11" required>
                    <span></span>
                    <i></i>
                </div>
                <div class="secondBox">
                    <div class="inputBox">
                        <label for="email_cliente">Email</label>
                        <input type="email" autocomplete="#" name="email_cliente" id="emailCliente" required>
                        <span id="spanEmail"></span>
                        <i></i>
                    </div>
                    <div class="inputBox">
                        <label for="data_nascimento">Data de Nascimento</label>
                        <input type="date" autocomplete="off" name="data_nascimento" id="dataNascimento" required>
                        <span></span>
                        <i></i>
                    </div>
                </div>
            </div>
            <div class="inputButton"><input type="submit" value="ENVIAR"></div>
        </form>
        <div class="pag-link"><a href="./listagem.php">Listagem</a></div>
    </section>
</body>

</html>