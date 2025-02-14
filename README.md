# Cadastro de Produtos

## 🚀 Desafio proposto pela Oak - Tecnologia para uma possível vaga de estágio

Este projeto consiste em uma aplicação web para cadastro e listagem de produtos, desenvolvida como parte de um desafio técnico. Ele inclui funcionalidades essenciais de validação, armazenamento local e testes automatizados, garantindo qualidade e eficiência na experiência do usuário.

## 📌 Funcionalidades

- Interface amigável para cadastro de produtos 📋
- Validação dinâmica dos dados 🔍
- Armazenamento local dos produtos 📂
- Listagem dos produtos cadastrados com ordenação por preço 📊
- Testes automatizados com Selenium WebDriver ✅
- Geração automática de relatórios de testes em HTML 📝

---

## 🛠 Tecnologias Utilizadas

### Frontend

- HTML5 → Estrutura da página
- CSS3 → Estilização e responsividade
- JavaScript (ES6+) → Manipulação do DOM e validações
- LocalStorage → Persistência de dados no navegador

### Testes Automatizados

- Python 3+ → Execução do script de testes
- Selenium WebDriver → Automação do navegador
- WebDriver Manager → Gerenciamento de drivers para navegadores
- ChromeDriver / GeckoDriver / EdgeDriver → Drivers WebDriver

---

## ⚙️ Como Rodar o Projeto

### 1️⃣ Executando a Aplicação Web

📌 Opção 1: Abrindo diretamente no navegador:

1. Faça o download do projeto.
2. Abra o arquivo `index.html` em um navegador moderno.

📌 Opção 2: Executando com um servidor local (recomendado):

```sh
python -m http.server 8000
```

🔗 Acesse `http://localhost:8000/index.html` no navegador.

---

### 2️⃣ Executando os Testes Automatizados

1️⃣ Instale as dependências necessárias:

```sh
pip install selenium webdriver-manager
```

2️⃣ Execute o script de testes:

```sh
python teste.py
```

3️⃣ Escolha onde deseja rodar os testes:

- Digite 1 para testar o arquivo local `index.html`
- Digite 2 para testar uma URL externa

4️⃣ Escolha o navegador para rodar os testes:

- 1 - Chrome (Padrão)
- 2 - Firefox
- 3 - Edge

📊 Após a execução, um relatório de testes será gerado no arquivo `test_report.html`. Basta abri-lo no navegador para visualizar os resultados.

---

## 🔥 Destaques e Aprendizados

### Desafios Superados

- Implementação de validação dinâmica de formulários no frontend.
- Uso do LocalStorage para armazenar e recuperar dados sem backend.
- Criação de testes automatizados simulando a experiência do usuário.
- Automação de execução e validação de cadastros via Selenium.
- Geração automática de relatórios de testes interativos em HTML.

### Principais Aprendizados

- Manipulação de DOM com JavaScript para navegação sem recarregar a página.
- Importância de validar os dados tanto no frontend quanto no backend.
- Gerenciamento de drivers para testes automatizados com WebDriver Manager.
- Geração de relatórios estruturados para análise dos testes.

---

## ✨ Autor

Paulo Mauricio Pereira Patricio

🔗 [LinkedIn](https://www.linkedin.com/in/paulo-mauricio)
📧 [Email](mailto:paulo@example.com)

---

## 📜 Licença

Este projeto é licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

🚀 Projeto desenvolvido como parte do desafio técnico da Oak - Tecnologia.

Se você gostou, contribua ou deixe uma ⭐ no repositório! 😊
