### Installation

    pip install deskent-bot-reporter

### Usage

    from bot_reporter import Bot

    bot = Bot(bot_token=TELEBOT_TOKEN, chat_id=CHAT_ID)

    # Send message
    bot.send_message('Hello, world')

    # Send file
    temp_file = Path('test.txt')
    with open(temp_file, mode='w', encoding='utf-8') as f:
        f.write('Test message')
    bot.send_document(temp_file)
