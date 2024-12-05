# -*- coding: utf-8 -*-

import os
import sys
import json
import urllib.parse
from pyrogram import Client
from pyrogram.raw import functions

# Убедитесь, что папка 'sessions' существует
if not os.path.exists("sessions"):
    os.makedirs("sessions")

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

# Функция для создания новой сессии
def создать_новую_сессию():
    api_id, api_hash = config["api_id"], config["api_hash"]
    номер_телефона = input("Введите номер телефона: ")
    файл_сессии = f"sessions/{номер_телефона}.session"
    if os.path.exists(файл_сессии):
        print(f"Сессия для номера {номер_телефона} уже существует.")
        return

    # Создаем нового клиента с именем файла, соответствующим номеру телефона
    app = Client(
        name=номер_телефона,
        phone_number=номер_телефона,
        api_id=api_id,
        api_hash=api_hash,
        workdir='sessions',
        device_model='Ulul Azmi',
        app_version='pyrogram'
    )
    with app:
        print(f"Сессия для номера {номер_телефона} успешно создана и сохранена в папке 'sessions/'.")

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
    print("1. Ввести данные бота для этой сессии")
    print("2. Добавить нового бота")

    for index, имя_бота in enumerate(имена_ботов, start=3):
        print(f"{index}. {имя_бота}")

    выбор = input("Введите ваш выбор: ")
    if выбор == '0':
        print("Возвращение в предыдущее меню.")
        return 0
    elif выбор == '1':
        имя_бота = input("Введите имя бота (например, @YourBot): ")
        ссылка_реферал = input("Введите реферальную ссылку: ")
        print(f"Бот {имя_бота} с URL: {ссылка_реферал} добавлен для этой сессии.")
        return {'bot_username': имя_бота, 'referral_url': ссылка_реферал}
    elif выбор == '2':
        имя_бота = input("Введите имя бота (например, @YourBot): ")
        ссылка_реферал = input("Введите реферальную ссылку: ")
        данные_ботов[имя_бота] = ссылка_реферал
        сохранить_данные_ботов(данные_ботов)
        print(f"Бот {имя_бота} сохранен с URL: {ссылка_реферал}")
        return {'bot_username': имя_бота, 'referral_url': ссылка_реферал}
    else:
        индекс = int(выбор) - 3
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
    
    пользователи = []
    query_id = []

    for файл_сессии in файлы_сессий:
        имя_сессии = файл_сессии.replace(".session", "")

        app = Client(
            name=имя_сессии,
            phone_number=имя_сессии,
            api_id=config["api_id"],
            api_hash=config["api_hash"],
            workdir='sessions',
            device_model='Ulul Azmi',
            app_version='pyrogram'
        )
        with app:
            попытка = 0
            while попытка < 3:
                try:
                    bot_peer = app.resolve_peer(имя_бота)
                    start_param = ссылка_реферал.split("startapp=")[1]
                    result = app.invoke(functions.messages.RequestWebView(
                        peer=bot_peer,
                        bot=bot_peer,
                        platform="android",
                        url=ссылка_реферал,
                        from_bot_menu=False,
                        start_param=start_param
                    ))
                    decoded_url = urllib.parse.unquote(result.url)
                    extracted_user = decoded_url.split("tgWebAppData=")[1].split("&tgWebAppVersion=")[0]
                    пользователи.append(extracted_user)
                    query_id.append(extracted_user)
                    
                    print(f"\x1b[32mGET Query ID\x1b[0m : {имя_сессии}")
                    попытка = 3
                except Exception as e:
                    попытка += 1
                    print(f"Не удалось открыть WebView для {имя_сессии}: {e}")
        
    with open("user.txt", "w") as data_file:
        data_file.writelines("\n".join(пользователи))
    with open("query_id.txt", "w") as query_id_file:
        query_id_file.writelines("\n".join(query_id))

# Функция для отображения меню
def показать_меню():
    print("\n--- Меню ---")
    print("1. Создать новую сессию")
    print("2. Запросить query ID у всех клиентов")
    print("3. Выход")

# Основная функция
def main():
    while True:
        показать_меню()
        выбор = input("Выберите пункт меню: ")

        if выбор == "1":
            создать_новую_сессию()
        elif выбор == "2":
            запросить_query_id_у_всех_клиентов()
        elif выбор == "3":
            print("Выход из программы.")
            sys.exit()
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
