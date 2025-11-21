import os
from telethon import TelegramClient, events
from config import API_ID, API_HASH, TARGET_CHAT
from voice import init_calls, join_vc, leave_vc, play_mp3, stop
from scheduler import setup_schedulers
from storage import add_post

SESSION = "session/session"

if not os.path.exists("music"):
    os.makedirs("music")

client = TelegramClient(SESSION, API_ID, API_HASH)
calls = init_calls(client)

LAST_MP3 = "music/last.mp3"

# --------------------- ЛИЧКА --------------------------
@client.on(events.NewMessage(incoming=True))
async def handler(event):
    sender = await event.get_sender()
    if event.is_private:

        # Команда поста
        if event.raw_text.startswith("/post"):
            try:
                date_str = event.raw_text.split()[1]
                add_post(date_str)
                await event.reply("Дата сохранена։")
            except:
                await event.reply("Формат: /post YYYY-MM-DD")
            return

        # Получение mp3
        if event.file and event.file.mime_type == "audio/mpeg":
            await event.download_media(LAST_MP3)
            await event.reply("Ֆայլը ընդունվեց։")
            return

# ------------------ ГРУППА --------------------------
@client.on(events.NewMessage(chats=TARGET_CHAT))
async def group_cmd(event):
    text = event.raw_text

    if text == "/join":
        await join_vc(event.chat_id)
        return

    if text == "/leave":
        await leave_vc(event.chat_id)
        return

    if text == "/stop":
        await stop(event.chat_id)
        return

    if text == "/play":
        if not os.path.exists(LAST_MP3):
            await client.send_message(event.sender_id, "Չկա վերջին երգը, խնդրում եմ ուղարկել mp3")
            return

        await play_mp3(event.chat_id, LAST_MP3)
        os.remove(LAST_MP3)
        return


async def main():
    setup_schedulers(client)
    print("Bot started.")
    await client.run_until_disconnected()


client.start()
client.loop.run_until_complete(main())
