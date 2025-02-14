document.addEventListener("DOMContentLoaded", () => {
    /*
     *  GERENCIAMENTO DE TELAS
     */
    const sections = {
        menu: document.getElementById("menu"),
        cadastro: document.getElementById("cadastro"),
        lista: document.getElementById("lista")
    };

    /*
     * Exibe apenas a seção desejada e oculta as demais
     * @param {string} sectionId - ID da seção a ser exibida
     */
    function showSection(sectionId) {
        Object.values(sections).forEach(section => section.classList.add("hidden"));
        sections[sectionId].classList.remove("hidden");

        // Remove a mensagem de sucesso ao mudar de tela
        if (sectionId !== "cadastro") {
            feedbackMessage.textContent = "";
        }

        // Atualiza a tabela quando a lista de produtos for aberta
        if (sectionId === "lista") {
            updateTable();
        }
    }

    // Adicionando eventos aos botões
    document.getElementById("btnCadastro").addEventListener("click", () => showSection("cadastro"));
    document.getElementById("btnLista").addEventListener("click", () => showSection("lista"));
    document.getElementById("btnNovoProduto").addEventListener("click", () => showSection("cadastro"));
    document.getElementById("btnVoltarMenu1").addEventListener("click", () => showSection("menu"));
    document.getElementById("btnVoltarMenu2").addEventListener("click", () => showSection("menu"));

    /*
     *  SELEÇÃO DE ELEMENTOS
     */
    const productForm = document.getElementById("productForm");
    const productName = document.getElementById("productName");
    const productDescription = document.getElementById("productDescription");
    const productPrice = document.getElementById("productPrice");
    const productAvailable = document.getElementById("productAvailable");
    const saveButton = document.getElementById("saveButton");
    const feedbackMessage = document.getElementById("feedbackMessage");
    const productList = document.getElementById("productList");

    // Elementos para mensagens de erro
    const nameError = document.getElementById("nameError");
    const descriptionError = document.getElementById("descriptionError");
    const priceError = document.getElementById("priceError");

    /*
     * FUNÇÕES DE VALIDAÇÃO
     * Exibe uma mensagem de erro para um campo inválido
     * @param {HTMLElement} element - Elemento onde a mensagem será exibida
     * @param {string} message - Texto da mensagem de erro
     */
    function showErrorMessage(element, message) {
        element.textContent = message;
    }

    /*
     * Remove uma mensagem de erro de um campo
     * @param {HTMLElement} element - Elemento onde a mensagem será removida
     */
    function clearErrorMessage(element) {
        element.textContent = "";
    }

    /*
     * Valida o formulário e habilita o botão de salvar apenas se todos os campos forem válidos
     */
    function validateForm() {
        let isValid = true;

        // Limpa mensagens de erro e bordas vermelhas dos campos
        [nameError, descriptionError, priceError].forEach(clearErrorMessage);
        [productName, productDescription, productPrice].forEach(input => input.classList.remove("error-border"));

        // Validar Nome (somente números não são permitidos)
        if (productName.value.trim() && !isNaN(productName.value)) {
            showErrorMessage(nameError, "Nome do produto inválido.");
            productName.classList.add("error-border");
            isValid = false;
        }

        // Validar Descrição (somente números não são permitidos)
        if (productDescription.value.trim() && !isNaN(productDescription.value)) {
            showErrorMessage(descriptionError, "Descrição inválida.");
            productDescription.classList.add("error-border");
            isValid = false;
        }

        // Validar Preço (somente se for maior zero)
        if (productPrice.value && parseFloat(productPrice.value) <= 0) {
            showErrorMessage(priceError, "O valor inválido.");
            productPrice.classList.add("error-border");
            isValid = false;
        }

        // Habilitar botão se tudo estiver preenchido corretamente e sem erros
        saveButton.disabled = !(
            productName.value.trim() &&
            productDescription.value.trim() &&
            productPrice.value &&
            productAvailable.value &&
            isValid
        );
    }

    // Evento para validar formulário dinamicamente
    productForm.addEventListener("input", validateForm);

    /*
     * FUNÇÃO PARA ATUALIZAR A LISTA
     * Atualiza a tabela de produtos na tela com os dados do LocalStorage
     */
    function updateTable() {
        productList.innerHTML = "";
        let products = JSON.parse(localStorage.getItem("products")) || [];

        // Se não houver produtos cadastrados, exibe uma mensagem na tabela
        if (products.length === 0) {
            productList.innerHTML = "<tr><td colspan='2'>Nenhum produto cadastrado</td></tr>";
            return;
        }

        // Ordenar produtos pelo menor preço
        products.sort((a, b) => a.price - b.price);

        // Adiciona os produtos na tabela
        products.forEach(product => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${product.name}</td>
                <td>${product.price.toLocaleString("pt-BR", { style: "currency", currency: "BRL" })}</td>
            `;
            productList.appendChild(row);
        });
    }

    /*
     * EVENTO DE ENVIO DO FORMULÁRIO
     */
    productForm.addEventListener("submit", (e) => {
        e.preventDefault();
        if (saveButton.disabled) return;

        // Criando um novo produto com os dados do formulário
        const newProduct = {
            name: productName.value.trim(),
            description: productDescription.value.trim(),
            price: parseFloat(productPrice.value),
            available: productAvailable.value
        };

        // Recupera a lista do LocalStorage e adiciona o novo produto
        let products = JSON.parse(localStorage.getItem("products")) || [];
        products.push(newProduct);
        localStorage.setItem("products", JSON.stringify(products));

        // Exibe mensagem de sucesso
        feedbackMessage.textContent = "Produto cadastrado com sucesso!";
        feedbackMessage.style.color = "green";
        feedbackMessage.style.margin = "10px";

        // Reseta o formulário e desabilita o botão de salvar
        productForm.reset();
        saveButton.disabled = true;

        // Exibe a mensagem por 2 segundos antes de redirecionar para a lista de produtos cadastrados.
        setTimeout(() => {
            showSection("lista");
        }, 1000);
    });

    // Exibe a tela inicial do menu ao carregar a página
    showSection("menu");
});
