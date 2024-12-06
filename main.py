# -*- coding: utf-8 -*-

import os
import sys
import json
import urllib.parse
import random
from pyrogram import Client
from pyrogram.raw import functions

# Убедитесь, что папка 'sessions' существует
if not os.path.exists("sessions"):
    os.makedirs("sessions")

# Убедитесь, что папка 'query_id' существует
if not os.path.exists("query_id"):
    os.makedirs("query_id")

CONFIG_FILE = "config.json"
DEFAULT_CONFIG = {
    "api_id": 0,
    "api_hash": "your_api_hash_here"
}

# Создаем файл конфигурации, если его нет
if not os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "w") as file:
        json.dump(DEFAULT_CONFIG, file, indent=4)
        print("Пожалуйста, заполните api_id и api_hash в config.json, затем перезапустите программу.")
        sys.exit()

# Читаем файл конфигурации
with open(CONFIG_FILE, "r") as file:
    config = json.load(file)
if config["api_id"] == 0 or config["api_hash"] == "your_api_hash_here":
    print("Пожалуйста, заполните api_id и api_hash в config.json, затем перезапустите программу.")
    sys.exit()

# Список доступных устройств
devices = [
    'SM-G960F', 'Pixel 5', 'SM-A505F', 'Pixel 4a', 'Pixel 6 Pro', 'SM-N975F',
    'SM-G973F', 'Pixel 3', 'SM-G980F', 'Pixel 5a', 'SM-G998B', 'Pixel 4',
    'SM-G991B', 'SM-G996B', 'SM-F711B', 'SM-F916B', 'SM-G781B', 'SM-N986B',
    'SM-N981B', 'Pixel 2', 'Pixel 2 XL', 'Pixel 3 XL', 'Pixel 4 XL',
    'Pixel 5 XL', 'Pixel 6', 'Pixel 6 XL', 'Pixel 6a', 'Pixel 7', 'Pixel 7 Pro',
    'OnePlus 8', 'OnePlus 8 Pro', 'OnePlus 9', 'OnePlus 9 Pro', 'OnePlus Nord', 'OnePlus Nord 2',
    'OnePlus Nord CE', 'OnePlus 10', 'OnePlus 10 Pro', 'OnePlus 10T', 'OnePlus 10T Pro',
    'Xiaomi Mi 9', 'Xiaomi Mi 10', 'Xiaomi Mi 11', 'Xiaomi Redmi Note 8', 'Xiaomi Redmi Note 9',
    'Huawei P30', 'Huawei P40', 'Huawei Mate 30', 'Huawei Mate 40'
]

BOT_FILE = "bot.json"

# Функция для загрузки или создания файла bot.json
def загрузить_данные_ботов():
    if not os.path.exists(BOT_FILE):
        with open(BOT_FILE, 'w') as file:
            json.dump({}, file)
    with open(BOT_FILE, 'r') as file:
        return json.load(file)

# Функция для сохранения данных в bot.json
def сохранить_данные_ботов(data):
    with open(BOT_FILE, 'w') as file:
        json.dump(data, file, indent=2)

# Функция для отображения списка доступных ботов
def выбрать_бота():
    данные_ботов = загрузить_данные_ботов()
    имена_ботов = list(данные_ботов.keys())

    print("Выберите бота:")
    print("0. Вернуться")

    for index, имя_бота in enumerate(имена_ботов, start=1):
        print(f"{index}. {имя_бота}")

    выбор = input("Введите ваш выбор: ")
    if выбор == '0':
        return 0
    else:
        индекс = int(выбор) - 1
        if 0 <= индекс < len(имена_ботов):
            имя_бота = имена_ботов[индекс]
            ссылка_реферал = данные_ботов[имя_бота]
            print(f"Используем бот: {имя_бота} с URL: {ссылка_реферал}")
            return {'bot_username': имя_бота, 'referral_url': ссылка_реферал}
        else:
            print("Неверный выбор.")
            return None

# Функция для получения query_id от всех клиентов
def запросить_query_id_у_всех_клиентов():
    файлы_сессий = [f for f in os.listdir("sessions") if f.endswith(".session")]
    if not файлы_сессий:
        print("В папке 'sessions' не найдено ни одной сессии.")
        return

    выбранный_бот = выбрать_бота()
    if выбранный_бот == 0:
        return
    if not выбранный_бот:
        return
    
    имя_бота = выбранный_бот['bot_username']
    ссылка_реферал = выбранный_бот['referral_url']
    
    query_id = []

    for файл_сессии in файлы_сессий:
        имя_сессии = файл_сессии.replace(".session", "")
        print(f"Работаем с сессией: {имя_сессии}")

        app = Client(
            name=имя_сессии,
            phone_number=имя_сессии,
            api_id=config["api_id"],
            api_hash=config["api_hash"],
            workdir='sessions',
            device_model=random.choice(devices),
            app_version='pyrogram'
        )

        try:
            with app:
                попытка = 0
                while попытка < 3:
                    try:
                        bot_peer = app.resolve_peer(имя_бота)
                        # Разделяем ссылку для правильного параметра start
                        start_param = ссылка_реферал.split("startapp=")[1] if "startapp=" in ссылка_реферал else ссылка_реферал.split("start=")[1]
                        
                        # Используем RequestWebView для извлечения query_id
                        result = app.invoke(functions.messages.RequestWebView(
                            peer=bot_peer,
                            bot=bot_peer,
                            platform="android",
                            url=ссылка_реферал,
                            from_bot_menu=False,
                            start_param=start_param
                        ))
                        
                        # Декодируем URL и извлекаем query_id
                        decoded_url = urllib.parse.unquote(result.url)
                        extracted_user = decoded_url.split("tgWebAppData=")[1].split("&tgWebAppVersion=")[0]
                        query_id.append(extracted_user)

                        # Зеленый цвет для успешного получения
                        print(f"\033[32mGET Query ID: {имя_сессии}, Получен.\033[0m")
                        попытка = 3  # Выход из цикла при успешном выполнении
                    except Exception as e:
                        попытка += 1
                        # Красный цвет для ошибки
                        print(f"\033[31mНе удалось открыть WebView для {имя_сессии}: {e}\033[0m")

        except Exception as e:
            # Красный цвет для ошибки
            print(f"\033[31mОшибка при работе с сессией {имя_сессии}: {e}\033[0m")

    # Сохраняем только query_id в файл в папку query_id
    with open(f"query_id/{имя_бота}_query_id.txt", "w") as query_id_file:
        query_id_file.writelines("\n".join(query_id))

    print(f"Все query_id для бота @{имя_бота} готовы и сохранены в файл.")

# Функция для отображения меню
def показать_меню():
    print("\n--- Меню ---")
    print("1. Добавить нового бота")
    print("2. Запросить query ID у всех клиентов")
    print("3. Выход")

# Основная функция
def main():
    while True:
        показать_меню()
        выбор = input("Выберите пункт меню: ")

        if выбор == "1":
            имя_бота = input("Введите имя бота (например, @YourBot): ")
            ссылка_реферал = input("Введите реферальную ссылку: ")
            данные_ботов = загрузить_данные_ботов()
            данные_ботов[имя_бота] = ссылка_реферал
            сохранить_данные_ботов(данные_ботов)
            print(f"Бот {имя_бота} добавлен с URL: {ссылка_реферал}")
        elif выбор == "2":
            запросить_query_id_у_всех_клиентов()
        elif выбор == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
