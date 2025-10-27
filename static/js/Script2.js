// Controle de Sidebar (colapsar/expandir)
let botaoSidebar = document.getElementById("toggleSidebarBtn");
let sidebar = document.getElementById("sidebar");
let conteudo = document.getElementById("conteudo");
let icone = botaoSidebar.querySelector("i");


botaoSidebar.addEventListener("click", function () {
    sidebar.classList.toggle("ativa");
    sidebar.classList.toggle("desativa");
    conteudo.classList.toggle("reduzido");
    icone.classList.toggle("fa-book-open");
    icone.classList.toggle("fa-book");
});
