from pathlib import Path

import niquests

from telegram_bot_reporter import AsyncBot


async def test_bot_send_async_message(async_bot: AsyncBot):
    response: niquests.Response = await async_bot.send_message("Test message")
    assert response.status_code == 200, response.text


async def test_bot_send_long_message(async_bot: AsyncBot):
    response: niquests.Response = await async_bot.send_message(
        "*" * 4001,
        split_message=True,
    )
    assert response.status_code == 200, response.text


async def test_bot_send_file(async_bot: AsyncBot):
    temp_file = Path("test.txt")
    with open(temp_file, mode="w", encoding="utf-8") as f:
        f.write("Test message")
    response: niquests.Response = await async_bot.send_document(temp_file)
    assert response.status_code == 200
    temp_file.unlink(missing_ok=True)
