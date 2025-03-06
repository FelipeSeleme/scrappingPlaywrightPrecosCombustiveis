from playwright.sync_api import Page
import pytest

def test_scraper_title(page: Page):
    """ O título da página deve ser 'Série histórica de preços de combustíveis e de GLP' """
    page.goto("https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp")
    assert page.title() == "Série histórica de preços de combustíveis e de GLP"

def test_button_expansion(page: Page):
    """ O botão de expansão de recursos deve funcionar corretamente """
    page.goto("https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp")
    page.click("button.botao-collapse-Recursos")
    page.wait_for_timeout(2000)  # Esperar a expansão
    # Verifica se o conteúdo "Metadados de preços" aparece na página
    assert page.inner_text('h4') == "Metadados de preços"

def test_download_button_existence(page: Page):
    """ Verifica se o botão de download para os dados de 'Combustíveis Automotivos' existe """
    page.goto("https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp")
    page.click("button.botao-collapse-Recursos")
    page.wait_for_timeout(2000)  # Esperar a expansão

    # Verifica se o botão "Acessar o recurso" está presente para o conjunto de dados "Combustíveis Automotivos"
    data_blocks = page.locator("div.col-10").all()
    for block in data_blocks:
        title = block.locator("h4").inner_text()
        if "Combustíveis Automotivos" in title:
            button = block.locator("button#btnDownloadUrl")
            assert button.is_visible(), f"Botão de download não encontrado para o título: {title}"

def test_file_download(page: Page, tmp_path):
    """ Teste para garantir que o arquivo CSV é baixado corretamente """
    download_path = tmp_path / "PrecosCombustiveis"
    download_path.mkdir(parents=True, exist_ok=True)

    page.goto("https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp")
    page.click("button.botao-collapse-Recursos")
    page.wait_for_timeout(2000)

    data_blocks = page.locator("div.col-10").all()
    for block in data_blocks:
        title = block.locator("h4").inner_text()
        if "Combustíveis Automotivos" in title:
            with page.expect_download() as download_info:
                block.locator("button#btnDownloadUrl").click()
            download = download_info.value
            download.save_as(download_path / download.suggested_filename)
            # Verifica se o arquivo foi baixado
            assert (download_path / download.suggested_filename).exists(), "Falha ao baixar o arquivo"
