function habilitarDesabilitarFormulario() {
    // Obtém o elemento de seleção do formulário x
    var selecao = document.getElementById("objetivo");
    // Obtém o elemento do formulário y
    var formularioY = document.getElementById("pesoAlcancar");

    // Verifica se o item 1 está selecionado em formulário x
    if (selecao.value !== "1") {
        // Desabilita o formulário y
        formularioY.disabled = false;
    } else {
        // Habilita o formulário y
        formularioY.disabled = true;
    }
}

const mode = document.getElementById('mode_icon');
console.log(mode)
mode.addEventListener('click', () => {
    if(mode.classList.contains('fa-moon')){
    mode.classList.remove('fa-moon');
    mode.classList.add('fa-sun');
    }
})