# 🚀 Web Scraper de Preços de Combustíveis

Este projeto realiza **web scraping** de dados públicos sobre preços de combustíveis a partir do portal **[dados.gov.br](https://dados.gov.br/)**.  
Os dados são baixados automaticamente e processados para manter apenas arquivos relevantes.

## 📂 Estrutura do Projeto

```bash
📦 PrecosCombustiveis/ # Pasta onde os arquivos baixados são armazenados 
├── scrapper.py # Script para coletar os arquivos do site 
├── processamento.py # Script para organizar e processar os arquivos baixados 
├── requirements.txt # Lista de dependências do projeto 
└── README.md # Documentação do projeto
```

---

## 🛠️ **Pré-requisitos**
Certifique-se de ter o **Python 3.8+** instalado em seu sistema.  

### 🔹 Instalando as dependências  
Antes de rodar o projeto, instale as bibliotecas necessárias executando:

```bash
pip install -r requirements.txt

Caso o Playwright seja necessário, execute também:

playwright install
```

### 📌 Uso
#### 1️⃣ Executar o Scraper

Para baixar os arquivos diretamente do site:

```bash
python scrapper.py
```

O script scrapper.py irá:  
✅ Acessar o portal dados.gov.br  
✅ Navegar até a seção correta  
✅ Baixar apenas os arquivos relacionados a "Combustíveis Automotivos"  
✅ Salvar os arquivos na pasta PrecosCombustiveis/  

#### 2️⃣ Processar os Arquivos

Após os downloads, execute o script de processamento:

```bash
python processamento.py
```

O script processamento.py irá:  
✅ Remover arquivos que não começam com "ca"  
✅ Descompactar arquivos ZIP na pasta correta  
✅ Excluir os arquivos ZIP após a extração  

### 🔧 Personalização

Se quiser modificar o comportamento do scraper ou do processamento, edite os arquivos scrapper.py e processamento.py conforme necessário.
🤝 Contribuição

Sinta-se à vontade para sugerir melhorias ou reportar problemas abrindo uma issue ou enviando um pull request.
