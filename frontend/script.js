async function login() {

    const usuario = document.getElementById("usuario").value;
    const senha = document.getElementById("senha").value;

    const mensagem = document.getElementById("mensagem");


    try {

        const resposta = await fetch(
            "http://localhost:8000/api/login",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    usuario: usuario,
                    senha: senha
                })
            }
        );


        const dados = await resposta.json();


        if (resposta.ok) {

            localStorage.setItem(
                "usuario",
                dados.usuario
            );

            localStorage.setItem(
                "perfil",
                dados.perfil
            );


            window.location.href = "dashboard.html";


        } else {

            mensagem.innerHTML =
                dados.detail;

        }


    } catch (erro) {

        mensagem.innerHTML =
            "Erro ao conectar com servidor";

        console.log(erro);

    }

}
