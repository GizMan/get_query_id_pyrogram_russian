Get Query ID Pyrogram
Get Query ID Pyrogram — это инструмент для работы с Telegram API через Pyrogram, позволяющий взаимодействовать с ботами Telegram и получать query_id.

🚀 Требования
Python 3.7+
Библиотека Pyrogram
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
   - Example:
     ```json
     {
       "api_id": 1234567,
       "api_hash": "your_api_hash_here"
     }
     ```

▶️ Использование
Для запуска скрипта выполните команду:
   - Start the program by running:
     ```bash
     python main.py
     ```
     Программа предложит несколько вариантов действий через меню. Вы можете:

1) Создать новую сессию.
2) Получить query_id для всех активных сессий.
   
🛠️ Файлы проекта:
main.py — основной файл программы.
config.json — файл конфигурации, в котором хранятся ваши api_id и api_hash.
sessions/ — папка, где будут сохранены сессии пользователей Telegram.
user.txt и query_id.txt — файлы для сохранения извлеченных данных.

💡 Примечания
Убедитесь, что ваши данные api_id и api_hash защищены и не публикуются публично.
Данные, извлечённые программой, сохраняются только локально и не передаются третьим лицам.

📄 Лицензия
Этот проект распространяется под MIT License. Вы можете свободно использовать, изменять и распространять его.

Если у вас есть вопросы или предложения, не стесняйтесь создавать Issues или отправлять запросы на слияние (Pull Requests).

😊 Спасибо за использование Get Query ID Pyrogram!
