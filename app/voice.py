import os
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import AudioPiped

client_call = None

def init_calls(client):
    global client_call
    client_call = PyTgCalls(client)
    return client_call

async def join_vc(chat_id):
    await client_call.join_group_call(
        chat_id,
        InputStream(
            AudioPiped("silence.mp3")  # заглушка
        )
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
