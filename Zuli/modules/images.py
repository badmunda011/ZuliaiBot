import requests
import config
from pyrogram import filters, Client
from pyrogram.types import InputFile
from pyrogram.enums import ChatAction

api_key = config.DEEP_API



@Zuli.on_message(filters.command("image") & filters.private)
async def generate_image(zuli, message):
    if len(message.command) < 2:
        await message.reply_text("Please provide text after the command.")
        return

    text = message.text.split(' ', 1)[1]

    data = {
        'text': text,
    }

    headers = {
        'api-key': api_key,
    }

    r = requests.post("https://api.deepai.org/api/text2img", data=data, headers=headers)
    response = r.json()

    if 'output_url' in response:
        image_url = response['output_url']
        await zuli.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        await zuli.send_photo(chat_id=message.chat.id, photo=image_url)
    else:
        await message.reply_text("Image generation failed. Check your input and API key.")






