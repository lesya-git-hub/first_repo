from colorama import Fore, Back, Style, init
import sys
from pathlib import Path

# Тніціалізація колорами
init(autoreset=True)

def visualise_dir(path, prefix=""):
    items = list(path.iterdir())
    total = len(items)

    for i, item in enumerate(items):
        connector = "┗ " if i == total - 1 else "┣ "

        if item.is_dir():
            print(prefix + connector + Fore.CYAN + Style.BRIGHT + "🗃️  " + item.name)
            extension = "  " if i == total - 1 else "┃ "
            visualise_dir(item, prefix + extension)
        else:
            print(prefix + connector + Fore.GREEN + Style.DIM + "📰  " + item.name)
def main():
    if len(sys.argv) < 2:
        print("Please provide a path")
        return
    path = Path(sys.argv[1])
    print(Fore.BLUE + Style.BRIGHT + "📦 " + path.name)
    visualise_dir(path)

if __name__ == "__main__":
    main()



#Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії, 
#виводячи імена всіх піддиректорій та файлів. Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.
#Створіть віртуальне оточення Python для ізоляції залежностей проєкту.
#Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
#Використання бібліотеки colorama для реалізації кольорового виведення.
#Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).
#Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.
#Забезпечте належне форматування виводу, використовуючи функції colorama.
#python hw03.py /шлях/до/вашої/директорії
#📦picture
# ┣ 📂Logo
 #┃ ┣ 📜IBM+Logo.png
 #┃ ┣ 📜ibm.svg
 #┃ ┗ 📜logo-tm.png
 #┣ 📜bot-icon.png
 #┗ 📜mongodb.jpg
