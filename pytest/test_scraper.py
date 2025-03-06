from playwright.sync_api import Page


def test_scraper_title(page: Page):
    """ O título da página deve ser 'Portal de Dados Abertos' """
    page.goto("https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp")
    assert page.title() == "Portal de Dados Abertos"

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
            