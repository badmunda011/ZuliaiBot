import os
import openai
from pyrogram import filters
from Zuli import Zuli
from pyrogram.enums import ChatAction, ParseMode





openai.api_key = "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"




@Zuli.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(zuli :Zuli, message):
  name = message.from_user.first_name
    
    try:
        await zuli.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply(f"Hello {name}\nPlease provide text after the .ai command ")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            await message.reply_text(f"{x}")     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ**: {e} ")        







