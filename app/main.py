import os
from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, TARGET_CHAT
from voice import init_calls, join_vc, leave_vc, play_mp3, stop
from storage import add_post
from scheduler import setup

LAST_MP3 = "music/last.mp3"

app = Client(
    "userbot_session",
    api_id=API_ID,
    api_hash=API_HASH,
    workdir="."
)

calls = None

@app.on_message(filters.private & filters.audio)
async def save_mp3(client, message: Message):
    file = await message.download(file_name=LAST_MP3)
    await message.reply("Ֆայլը ընդունվեց։")

@app.on_message(filters.private & filters.command("post"))
async def add_post_cmd(client, message):
    try:
        date_str = message.text.split()[1]
        add_post(date_str)
        await message.reply("Պահպանվեց։")
    except:
        await message.reply("Օգտագործեք՝ /post YYYY-MM-DD")

@app.on_message(filters.chat(TARGET_CHAT) & filters.command("join"))
async def join_call(client, message):
    await join_vc(message.chat.id)

@app.on_message(filters.chat(TARGET_CHAT) & filters.command("leave"))
async def leave_call(client, message):
    await leave_vc(message.chat.id)

@app.on_message(filters.chat(TARGET_CHAT) & filters.command("stop"))
async def stop_cmd(client, message):
    await stop(message.chat.id)

@app.on_message(filters.chat(TARGET_CHAT) & filters.command("play"))
async def play_cmd(client, message):
    if not os.path.exists(LAST_MP3):
        await app.send_message(message.from_user.id, "Չկա վերջին երգը, խնդրում եմ ուղարկել mp3")
        return
    await play_mp3(message.chat.id, LAST_MP3)
    os.remove(LAST_MP3)

async def main():
    global calls
    calls = init_calls(app)
    setup(app)
    await app.start()
    await calls.start()
    print("Bot started")
    await app.idle()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
