from pyrogram import filters
from Zuli import Zuli



@Zuli.on_message(filters.command("start"))
async def start(_, msg):
  await msg.reply("bot under in maintainance..... bte u can use .ai text")
