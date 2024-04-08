from pathlib import Path

import httpx
import niquests

from telegram_bot_reporter import Bot


def test_bot_send_message(bot: Bot):
    response: httpx.Response = bot.send_message("Test message")
    assert response.status_code == 200, response.text


def test_bot_send_long_message(bot: Bot):
    response: niquests.Response = bot.send_message(
        "*" * 4097,
        split_message=True,
    )
    assert response.status_code == 200, response.text


def test_bot_send_file(bot: Bot):
    temp_file = Path("test.txt")
    with open(temp_file, mode="w", encoding="utf-8") as f:
        f.write("Test message")
    response: niquests.Response = bot.send_document(temp_file)
    assert response.status_code == 200
    temp_file.unlink(missing_ok=True)
