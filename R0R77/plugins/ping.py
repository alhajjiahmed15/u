import os

from telethon import Button, events

from R0R77 import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/8e1c77c8d70e86d9c9686.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@ku_kx"
)

CAPTION = f"**سرعة البنك:** {ms}\n المطور:『{ALIVE}』"


@R0R77.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/YY8GG")]]
    await R0R77.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
