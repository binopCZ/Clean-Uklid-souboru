import os
import shutil
import winsound

source_dir = "D:\\-Download"
dest_dir_music = "D:\\-Download\\- Hudba"
dest_dir_video = "D:\\-Download\\- Filmy"
dest_dir_image = "D:\\-Download\\- Obrázky"
dest_dir_documents = "D:\\-Download\\- Pdf"

# seznam souborů v adresáři
files = os.listdir(source_dir)

# cyklus přes soubory
for file_name in files:
    # cesta k souboru
    file_path = os.path.join(source_dir, file_name)
    
    # test, zda je soubor složka
    if os.path.isdir(file_path):
        continue
    
    # získání přípony souboru
    file_extension = os.path.splitext(file_path)[1]
    
    # přesunutí souboru do příslušné složky na základě přípony
    if file_extension in [".mp3", ".m4a", ".flac", ".alac", ".wav", ".aac", ".ogg"]:
        shutil.move(file_path, dest_dir_music)
    elif file_extension in [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm"]:
        shutil.move(file_path, dest_dir_video)
    elif file_extension in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"]:
        shutil.move(file_path, dest_dir_image)
    elif file_extension in [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"]:
        shutil.move(file_path, dest_dir_documents)

# zahájení zvukového signálu
winsound.Beep(440, 250)