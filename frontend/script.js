async function login() {

    const usuario = document.getElementById("usuario").value.trim();
    const senha = document.getElementById("senha").value.trim();

    const mensagem = document.getElementById("mensagem");


    if (!usuario || !senha) {

        alert("Digite usuário e senha.");

        return;
    }


    try {

        const resposta = await fetch(
            "https://crm-adriana.onrender.com/api/login",
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


            alert(
                "Login realizado com sucesso!"
            );


            window.location.href = "dashboard.html";


        } else {


            alert(
                "Usuário ou senha incorreto!"
            );


            mensagem.innerHTML =
                "Usuário ou senha incorreto.";


        }


    } catch (erro) {


        console.log(
            "Erro:",
            erro
        );


        alert(
            "Não foi possível conectar ao servidor."
        );


        mensagem.innerHTML =
            "Erro ao conectar com servidor.";


    }

}
