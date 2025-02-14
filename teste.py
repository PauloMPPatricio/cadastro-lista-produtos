import time
import os
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Perguntar ao usuário onde executar os testes (Arquivo Local ou URL)
def get_test_environment():
    option = input("Deseja testar (1) Arquivo local ou (2) URL? ")
    if option == "1":
        return f"file:///{os.path.abspath('index.html')}"
    elif option == "2":
        return input("Digite a URL do sistema: ")
    else:
        print("Opção inválida!")
        return get_test_environment()

# Escolha do navegador para rodar os testes
def get_browser():
    print("Escolha o navegador:")
    print("1 - Chrome (Padrão)")
    print("2 - Firefox")
    print("3 - Edge")
    browser_option = input("Opção: ")
    
    if browser_option == "2":
        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service)
    elif browser_option == "3":
        service = EdgeService(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service)
    else:
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service)

# Inicializar WebDriver e acessar a página do sistema
url = get_test_environment()
driver = get_browser()
driver.get(url)
driver.maximize_window()

# Limpar localStorage antes dos testes para garantir um ambiente limpo
driver.execute_script("localStorage.clear();")
time.sleep(2)  # Aguardar 2 segundos para aplicação das mudanças

# Função para preencher o formulário e tentar cadastrar um produto
def fill_form(name, description, price, available):
    """
    Preenche o formulário de cadastro de produtos e tenta salvar.
    Retorna True se o cadastro foi bem-sucedido, False se falhou.
    """

    # Preencher os campos do formulário
    driver.find_element(By.ID, "productName").clear()
    driver.find_element(By.ID, "productName").send_keys(name)

    driver.find_element(By.ID, "productDescription").clear()
    driver.find_element(By.ID, "productDescription").send_keys(description)

    driver.find_element(By.ID, "productPrice").clear()
    driver.find_element(By.ID, "productPrice").send_keys(str(price))

    # Selecionar a opção "Disponível para Venda", garantindo que valores inválidos não sejam enviados
    product_available = driver.find_element(By.ID, "productAvailable")
    if available in ["Selecione", "Sim", "Não"]:
        product_available.send_keys(available)
    else:
        print("⚠️ Opção inválida para 'Disponível para Venda'. Nenhuma seleção foi feita.")

    time.sleep(2)  # Aguardar a validação automática do formulário

    # Verificar se o botão "Salvar Produto" está habilitado
    save_button = driver.find_element(By.ID, "saveButton")
    
    if save_button.is_enabled():
        print("✅ Formulário preenchido corretamente. Salvando produto...")
        save_button.click()
        time.sleep(2)  # Aguardar a lista de produtos aparecer

        # Clicar no botão "Cadastrar Novo Produto" para novo cadastro
        try:
            novo_produto_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "btnNovoProduto"))
            )
            novo_produto_btn.click()
            time.sleep(2)  # Aguardar transição para o formulário
        except:
            print("⚠️ Erro: O botão 'Cadastrar Novo Produto' não apareceu.")
        return True  # ✅ Cadastro foi bem-sucedido

    else:
        print("❌ Formulário inválido. Teste registrado como falho e seguindo para o próximo caso...")

        # Registrar erro e seguir para o próximo teste
        return False  # ❌ Cadastro falhou

# Acessar a tela de cadastro antes de iniciar os testes
driver.find_element(By.ID, "btnCadastro").click()
time.sleep(2)  # Aguardar a transição de tela

# Lista de casos de teste
test_cases = [
    {"name": "Teclado Mecânico", "description": "Teclado RGB com switches mecânicos", "price": 350, "available": "Sim", "expected_success": True},
    {"name": "Mouse Gamer", "description": "Mouse óptico de alta precisão", "price": 180, "available": "Sim", "expected_success": True},
    {"name": "Monitor 24'", "description": "Monitor Full HD com taxa de 144Hz", "price": 1200, "available": "Sim", "expected_success": True},
    {"name": "Cadeira Gamer", "description": "Cadeira ergonômica com ajuste de altura", "price": 900, "available": "Sim", "expected_success": True},
    {"name": "Notebook Dell", "description": "Notebook com processador i7 e 16GB RAM", "price": 5000, "available": "Sim", "expected_success": True},
    {"name": "SSD 1TB", "description": "Unidade de armazenamento SSD NVMe", "price": 600, "available": "Sim", "expected_success": True},
    {"name": "Placa de Vídeo RTX 4060", "description": "Placa de vídeo para jogos em 4K", "price": 3000, "available": "Não", "expected_success": True},
    {"name": "Headset Gamer", "description": "Fone de ouvido com som surround 7.1", "price": 350, "available": "Não", "expected_success": True},
    {"name": "Microfone USB", "description": "Microfone condensador para podcasts", "price": 280, "available": "Não", "expected_success": True},
    {"name": "Smartphone Samsung", "description": "Celular Android com câmera de 108MP", "price": 3500, "available": "Sim", "expected_success": True},
    {"name": "Tablet iPad", "description": "Tablet Apple com tela Retina", "price": 4500, "available": "Sim", "expected_success": True},
    {"name": "Controle Xbox", "description": "Controle sem fio para Xbox e PC", "price": 400, "available": "Sim", "expected_success": True},
    {"name": "Câmera DSLR", "description": "Câmera profissional para fotografia", "price": 8000, "available": "Sim", "expected_success": True},
    {"name": "Roteador Wi-Fi 6", "description": "Roteador de alta velocidade com tecnologia Wi-Fi 6", "price": 650, "available": "Sim", "expected_success": True},
    {"name": "Impressora Multifuncional", "description": "Impressora a laser com scanner integrado", "price": 1200, "available": "Sim", "expected_success": True},
    {"name": "Teclado Mecânico", "description": "Teclado RGB", "price": 250, "available": "Sim", "expected_success": True},
    {"name": "", "description": "Monitor 4K", "price": 1000, "available": "Sim", "expected_success": False},  # Nome vazio
    {"name": "Mouse Gamer", "description": "", "price": 200, "available": "Sim", "expected_success": False},  # Descrição vazia
    {"name": 12345, "description": "Monitor 4K", "price": 1000, "available": "Sim", "expected_success": False},  # Nome somente com números
    {"name": "Mouse Gamer", "description": 12345, "price": 200, "available": "Sim", "expected_success": False},  # Descrição somente com números
    {"name": "Cadeira Gamer", "description": "Ergonômica", "price": -500, "available": "Sim", "expected_success": False},  # Valor negativo
    {"name": "Cadeira Gamer", "description": "Ergonômica", "price": "", "available": "Sim", "expected_success": False},  # Valor vazio
    {"name": "Cadeira Gamer", "description": "Ergonômica", "price": 0, "available": "Sim", "expected_success": False},  # Valor zerado
    {"name": "Cadeira Gamer", "description": "Ergonômica", "price": "kljlkjlk", "available": "Sim", "expected_success": False},  # Valor com caracteres alfabéticos
    {"name": "Webcam", "description": "Full HD", "price": 300, "available": "Selecione", "expected_success": False}  # Disponível para venda inválido
]

# Função para verificar se um produto foi cadastrado corretamente na tabela
def is_product_in_table(product_name):
    table_rows = driver.find_elements(By.CSS_SELECTOR, "#productList tr")
    for row in table_rows:
        if product_name in row.text:
            return True
    return False

# Executar os testes e armazenar os resultados
results = []
for test in test_cases:
    success = fill_form(test["name"], test["description"], test["price"], test["available"])
    
    result = {
        "Nome": test["name"],
        "Descrição": test["description"],
        "Preço": test["price"],
        "Disponível": test["available"],
        "Esperado": test["expected_success"],
        "Obtido": success,
        "Passou": success == test["expected_success"]
    }
    
    results.append(result)

# Gerar relatório dos testes em HTML
with open("test_report.html", "w") as f:
    f.write("<html><body><h1>Relatório de Testes</h1><table border='1'>")
    f.write("<tr><th>Nome</th><th>Descrição</th><th>Preço</th><th>Disponível</th><th>Esperado</th><th>Obtido</th><th>Passou</th></tr>")
    for res in results:
        f.write(f"<tr><td>{res['Nome']}</td><td>{res['Descrição']}</td><td>{res['Preço']}</td><td>{res['Disponível']}</td><td>{res['Esperado']}</td><td>{res['Obtido']}</td><td>{res['Passou']}</td></tr>")
    f.write("</table></body></html>")
# Finalizar WebDriver e abrir relatório
driver.quit()

# Exibir mensagem no terminal
print("\n✅ Teste concluído! Abrindo o relatório...")
time.sleep(2)

# Abrir automaticamente o relatório no navegador padrão
if os.name == "nt":  # Windows
    os.startfile("test_report.html")
else:  # Linux/Mac
    subprocess.run(["xdg-open", "test_report.html"])