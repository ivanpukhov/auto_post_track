import fitz
import re
import os
import pyperclip

def find_and_copy_words(file_path):
    with fitz.open(file_path) as doc:
        for page in doc:
            text = page.get_text()

            # Используем регулярное выражение для поиска слов, начинающихся на "AP" и заканчивающихся на "KZ"
            matches = re.findall(r'\bAP\w+KZ\b', text)

            if matches:
                # Копируем первое найденное слово
                word = matches[0]

                # Копируем слово в буфер обмена
                pyperclip.copy("Отследить посылочку сможете по треку https://post.kz/services/postal/"+word)

                print("Найдено слово:", word)
                print("Скопировано в буфер обмена.")

# Пример использования
folder_path = '/Users/ix/Downloads'
processed_files = set()

while True:
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(folder_path, file_name)
            if file_path not in processed_files:
                find_and_copy_words(file_path)
                processed_files.add(file_path)

