from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped

client_call = None

def init_calls(client):
    global client_call
    client_call = PyTgCalls(client)
    return client_call

async def join_vc(chat_id):
    # подключаемся в голосовой чат с заглушкой
    await client_call.join_group_call(
        chat_id,
        AudioPiped("silence.mp3")
    )

async def leave_vc(chat_id):
    try:
        await client_call.leave_group_call(chat_id)
    except:
        pass

async def play_mp3(chat_id, file_path):
    await client_call.change_stream(
        chat_id,
        AudioPiped(file_path),
    )

async def stop(chat_id):
    await client_call.change_stream(
        chat_id,
        AudioPiped("silence.mp3")
    )
