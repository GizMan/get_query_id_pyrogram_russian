Get Query ID Pyrogram

Это инструмент позволяющий получать query_id из pyrogram sessions.

🚀 Требования

Python 3.7+

Библиотека Pyrogram , tgcrypto.

api_id и api_hash, которые можно получить на my.telegram.org

📦 Установка
1. Клонирование репозитория
   ```bash
   git clone https://github.com/ululazmi18/get_query_id_pyrogram.git
   cd get_query_id_pyrogram
   ```

2. Установка необходимых библиотек
   ```bash
   pip install pyrogram tgcrypto
   ```

3. Настройка API-ключей
При первом запуске скрипт создаст файл config.json в корневой папке проекта.
Откройте этот файл и заполните поля api_id и api_hash:
   - Пример:
     ```json
       "api_id": 1234567,
       "api_hash": "your_api_hash_here"
     ```

▶️ Использование
Для запуска скрипта выполните команду:

     python main.py
     

   
🛠️ Файлы проекта:

main.py — основной файл программы.

config.json — файл конфигурации, в котором хранятся ваши api_id и api_hash.

sessions/ — папка, с сессиями pyrogram.

query_id/ — папка, с сессиями query id.

bot.json — Файл с данными ботов.


💡 Примечания
Убедитесь, что ваши данные api_id и api_hash защищены и не публикуются публично.
Данные, извлечённые программой, сохраняются только локально и не передаются третьим лицам.


📄 Лицензия
Этот проект распространяется под MIT License. Вы можете свободно использовать, изменять и распространять его.

😊 Спасибо за использование Get Query ID Pyrogram!
