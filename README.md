# Описание бота:
  Telegram-bot, который "конвертирует"(парсит с сайта: https://finance.rambler.ru/currencies/) валюты стран мира в рубли! А также сохраняет аву и историю переписки!
  Язык: **python3**, платформа: **linux**
# Описание файлов:
  bot.py - сам бот
  
  finance_rambler_ru_currencies.py - парсер с сайта
  
  command_description.txt - файл для подсказок в самом telegram-bot
  
  requirement.txt - зависимости, которые необходимо установить
  
  папка **history_message** - туть сохраняются история переписки с ботом
  
  папка **jpg** - авы

  token.pickle - тут сохраненный токен от бота
# Установка:
  - Качаем tor browser: https://www.torproject.org/download/
  
  - запускаем tor browser(он необходим для парсинга сайта, чтобы не залочили Ваш ip)
  
  - открываем терминал и Ctrl+C Ctrl+V:
    
    - **sudo apt-get update**
    
    - **sudo apt install git**
    
    - **sudo apt install python3-pip**
    
    - **git clone https://github.com/hulumulu801/telegram_bot_world_cash.git**
    
    - **cd telegram_bot_world_cash**
    
    - **pip3 install -r requirement.txt**
# Как пользоваться:
  - открываем Telegram Desktop
  
  - в поиске находим BotFather(там все примитивно, или создаем нового бота и узнаем токен от бота, или узнаем токен от старого бота)
  
  - можно(необязательно) написать /help для Вашего бота:
  
    - пишем сообщение BotFather:
    
      **/setcommands**
      
     - вставляем все из **command_description.txt**
     
  - **python3 bot.py ТУТ_ТОКЕН_БОТА**
  
  # P.S.: bot постоянно спамит сервера telegram на предмет: не появились ли новые сообщения, чтобы избежать этого, нужно переписать bot.py и поставить **Webhook**
  
  # P.S.S.: рекомендую пользоваться virtualenv
