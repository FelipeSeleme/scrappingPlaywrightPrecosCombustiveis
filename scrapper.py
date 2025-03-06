import os
from playwright.sync_api import sync_playwright

# Criar a pasta se não existir
download_path = "PrecosCombustiveis"
os.makedirs(download_path, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Abre o navegador visível
    page = browser.new_page()

    # Acessar a página
    page.goto("https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp")

    # Clicar para expandir os recursos
    page.click("button.botao-collapse-Recursos")
    page.wait_for_timeout(2000)  # Aguardar a expansão da lista

    # Encontrar todos os conjuntos de dados
    data_blocks = page.locator("div.col-10").all()

    for block in data_blocks:
        # Pegar o título do conjunto de dados
        title = block.locator("h4").inner_text()

        # Filtrar apenas os que contêm "Combustíveis Automotivos"
        if "Combustíveis Automotivos" in title:
            print(f"Verificando: {title}")

            # Localizar o botão de download correspondente
            with page.expect_download() as download_info:
                block.locator("button#btnDownloadUrl").click()  # Clicar no botão de download
            
            # Capturar o download
            download = download_info.value
            download_path_final = os.path.join(download_path, download.suggested_filename)

            # Verificar se o arquivo já existe
            if os.path.exists(download_path_final):
                print(f"Arquivo já existe: {download_path_final}, pulando download.")
                continue  # Pular para o próximo

            # Salvar o arquivo na pasta
            download.save_as(download_path_final)
            print(f"Salvo em: {download_path_final}")

    browser.close()

print("Fim da execução")
