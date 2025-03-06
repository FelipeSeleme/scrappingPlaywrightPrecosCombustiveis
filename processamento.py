import os
import zipfile

# Pasta onde os arquivos estão salvos
download_path = "PrecosCombustiveis"

# Verificar todos os arquivos na pasta
for filename in os.listdir(download_path):
    file_path = os.path.join(download_path, filename)

    # Se o arquivo não começa com "ca", remove
    if not filename.lower().startswith("ca"):
        print(f"Removendo arquivo inválido: {filename}")
        os.remove(file_path)
        continue  # Pular para o próximo arquivo

    # Se for um arquivo ZIP, descompactar e excluir o ZIP
    if filename.lower().endswith(".zip"):
        print(f"Descompactando: {filename}")
        
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(download_path)  # Extrai dentro da pasta

        print(f"Removendo ZIP: {filename}")
        os.remove(file_path)  # Remove o arquivo ZIP após extração

print("Processamento concluído.")
