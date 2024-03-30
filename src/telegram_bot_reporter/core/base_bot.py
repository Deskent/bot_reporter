class BaseBot:
    """Telegram Bot API interface
    to send messages to certain chats/users.

    :argument bot_token: Telegram bot token.
    :argument chat_id: Telegram chat id.
    :argument timeout: Time to wait Telegram Api response, seconds. Defaults is 10.
    :argument parse_mode: Message parse mode. Defaults is 'HTML'.
    :argument prefix: Message prefix. Defaults is empty string.

    """

    _CHUNK: int = 4000

    def __init__(
        self,
        bot_token: str,
        chat_id: str | int,
        timeout: int = 10,
        parse_mode: str = 'HTML',
        prefix: str = '',
    ):
        self._token = bot_token
        if not self._token:
            raise ValueError('Token cannot be empty')
        self._chat_id: str = str(chat_id)
        if not self._chat_id:
            raise ValueError('Chat id cannot be empty')
        self._timeout = timeout
        self._parse_mode = parse_mode
        self._prefix = prefix
        self._headers: dict = {'Content-Type': 'application/json'}
        self._url = f'https://api.telegram.org/bot{self._token}'
