/*Primeiro passo é selecionar os elementos que irá usar*/
let formulario = document.querySelector("form");

// Pega o dado do campo email
let campoEmail = document.getElementById("id_email");

// Pega o dado do campo senha1
let passwordField = document.getElementById("id_password1");

// Pega o dado do campo senha2
let passwordField2 = document.getElementById("id_password2");

// Pega o texto "A senha deve conter pelo menos oito caracteres;"
let reqLength = document.getElementById("req-length");

// Pega o texto "A senha deve conter pelo menos uma letra minúscula;"
let reqLowercase = document.getElementById("req-lowercase");

// Pega o texto "A senha deve conter pelo menos uma letra maiúscula;"
let reqUppercase = document.getElementById("req-uppercase");

// Pega o texto "A senha deve conter pelo menos um símbolo;"
let reqSymbol = document.getElementById("req-symbol");

// Pega o texto "A senha deve conter pelo menos um número;"
let reqNumber = document.getElementById("req-number");

// Seleciona o botão de mostrar/ocultar senha
let toggleButton1 = document.getElementById("toggle-password");
let icon = toggleButton1.querySelector("i");

let toggleButton2 = document.getElementById("toggle-password2");
let icon2 = toggleButton2.querySelector("i");

// Pega o campo de CPF
let campoCPF = document.getElementById("id_cpf");

// Expressão regular para validar números
let regexInteiros = /[0-9]/;
  

// Aqui valida o email
if (campoEmail){
    campoEmail.addEventListener("keyup", function(){
        // Pega o valor atual do email
        let email = campoEmail.value;
        let regexEmail = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        let emailValido = regexEmail.test(email);
    
        // Verifica se o email é válido
        if (!emailValido){
            // Se não for válido, mostra a mensagem de erro
            let mensagemErro = document.querySelector(".mensagem-erro-formato-incorreto");
            mensagemErro.classList.add("ativa"); // Adiciona a classe que torna a mensagem visível
            
        } else{
            // Se for válido, esconde a mensagem de erro
            let mensagemErro = document.querySelector(".mensagem-erro-formato-incorreto");
            mensagemErro.classList.remove('ativa'); // Remove a classe que torna a mensagem visível
            
        }
    
        // Verifica se o campo de email está vazio
        if (email.trim() === ""){
            // Se estiver vazio, mostra a mensamge de erro
            let mensagemErro = document.querySelector(".mensagem-erro-email-obrigatorio");
            mensagemErro.classList.add("ativa"); // Adiciona a classe que torna a mensagem visível        
        } else{
            // Se não estiver vazio, esconde a mensagem de erro
            let mensagemErro = document.querySelector(".mensagem-erro-email-obrigatorio");
            mensagemErro.classList.remove("ativa"); // Remove a classe que torna a mensagem visível
        }
    })
}


// Aqui valida a senha
passwordField.addEventListener("keyup", function(){
    // Pega o valor atual da senha
    let senha = passwordField.value;
    let allvalid = true; // Variável para verificar se todas as condições são atendidas

    // 1. Verifica o comprimento mínimo
    if (senha.length >= 8){
        reqLength.style.color = "green";
        reqLength.innerHTML = "✔️ Pelo menos oito caracteres;";
    } else {
        reqLength.style.color = "red";
        reqLength.innerHTML = "❌ A senha deve conter pelo menos oito caracteres;";
        allvalid = false; // Se não atender, define como inválido.
    }
    // 2. Valida letra minúscula
    if (/[a-z]/.test(senha)){
        reqLowercase.style.color = "green";
        reqLowercase.innerHTML = "✔️ Pelo menos uma letra minúscula;";
    } else {
        reqLowercase.style.color = "red";
        reqLowercase.innerHTML = "❌ A senha deve conter pelo menos uma letra minúscula;";
        allvalid = false; // Se não atender, define como inválido.
    }

    // 3. Valida letra maiúscula
    if (/[A-Z]/.test(senha)){
        reqUppercase.style.color = "green";
        reqUppercase.innerHTML = "✔️ Pelo menos uma letra maiúscula;";
    } else {
        reqUppercase.style.color = "red";
        reqUppercase.innerHTML = "❌ A senha deve conter pelo menos uma letra maiúscula;";
        allvalid = false; // Se não atender, define como inválido.
    }

    //4. Valida símbolo
    if (/[^a-zA-Z0-9]/.test(senha)){
        reqSymbol.style.color = "green";
        reqSymbol.innerHTML = "✔️ Pelo menos um símbolo;";

    }else{
        reqSymbol.style.color = "red";
        reqSymbol.innerHTML = "❌ A senha deve conter pelo menos um símbolo;";
        allvalid = false; // Se não atender, define como inválido.
    }

    // 5. Valida número
    if (regexInteiros.test(senha)){
        reqNumber.style.color = "green";
        reqNumber.innerHTML = "✔️ Pelo menos um número;";
    }else{
        reqNumber.style.color = "red";
        reqNumber.innerHTML = "❌ A senha deve conter pelo menos um número;";
        allvalid = false; // Se não atender, define como inválido.
    }

    // Habilita/desabilita o botão de cadastrar
    let submitButton = document.getElementById("botao-cadastrar");
    if (allvalid){
        submitButton.disabled = false; // Habilita o botão se todas as condições forem atendidas
    } else {
        submitButton.disabled = true; // Desabilita o botão se alguma condição não for atendida
    }
})

// Aqui você adiciona o evento de clique no botão de mostrar/ocultar senha
toggleButton1.addEventListener("click", function(){
    // Verifica o tipo atual do campo de senha
    let isPassword = passwordField.type === "password";

    if  (isPassword){
        // Se for senha, muda para texto
        passwordField.type = "text";

        // Troca o Ícone para o "olho cortado"
        icon.classList.remove("fa-eye");
        icon.classList.add("fa-eye-slash");

    } else {
        // Se for texto, muda para senha (ocultar senha)
        passwordField.type = "password";

        // Troca o ícone para o "olho aberto"
        icon.classList.remove("fa-eye-slash");
        icon.classList.add("fa-eye");
    }
})

toggleButton2.addEventListener("click", function(){
    // Verifica o tipo atual do campo de senha
    let isPassword2 = passwordField2.type === "password";

    if  (isPassword2){
        // Se for senha, muda para texto
        passwordField2.type = "text";

        // Troca o Ícone para o "olho cortado"
        icon2.classList.remove("fa-eye");
        icon2.classList.add("fa-eye-slash");

    } else {
        // Se for texto, muda para senha (ocultar senha)
        passwordField2.type = "password";

        // Troca o ícone para o "olho aberto"
        icon2.classList.remove("fa-eye-slash");
        icon2.classList.add("fa-eye");
    }
})

// SEÇÃO TELA HOME

//SEÇÃO SIDE BAR
let botaoSidebar = document.getElementById("toggleSidebarBtn");
let sidebar = document.querySelector(".side-bar-chat");
let conteudo = document.getElementById("conteudo");
let icone = botaoSidebar.querySelector("i");

botaoSidebar.addEventListener("click", function(){
    sidebar.classList.toggle("side-bar-chat-desativa");
    sidebar.classList.toggle("side-bar-chat-ativa");
    
    conteudo.classList.toggle("reduzido");

    icone.classList.toggle("fa-book-open");
    icone.classList.toggle("fa-book");


    
});
