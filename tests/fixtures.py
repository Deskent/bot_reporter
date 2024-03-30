import os

import pytest
from dotenv import load_dotenv

from telegram_bot_reporter.core.async_bot import AsyncBot
from telegram_bot_reporter.core.sync_bot import Bot

load_dotenv()


@pytest.fixture
def bot_token() -> str:
    return os.environ.get('TELEBOT_TOKEN')


@pytest.fixture
def chat_id() -> str:
    return os.environ.get('CHAT_ID')


@pytest.fixture
def bot(bot_token: str, chat_id: str) -> Bot:
    yield Bot(bot_token=bot_token, chat_id=chat_id)


@pytest.fixture
def async_bot(bot_token: str, chat_id: str) -> Bot:
    yield AsyncBot(bot_token=bot_token, chat_id=chat_id)
