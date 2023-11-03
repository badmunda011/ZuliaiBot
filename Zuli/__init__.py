import asyncio
import logging
import time
from importlib import import_module
from os import listdir, path
from dotenv import load_dotenv
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, POKI_TOKEN




loop = asyncio.get_event_loop()
load_dotenv()
boot = time.time()


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)



Zuli = Client(
    ":Zuli:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

Poki = Client(
    ":Poki:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=POKI_TOKEN,
)

async def zuli_bot():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    await Zuli.start()
    await Poki.start()
    getme = await Zuli.get_me()
    BOT_ID = getme.id
    BOT_USERNAME = getme.username
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name


loop.run_until_complete(zuli_bot())


