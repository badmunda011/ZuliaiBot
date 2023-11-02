from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Zuli import Poki
from config import POKI_USERNAME

start_txt = """**
Hey, I am the Poki bot. I have many games for you to enjoy, and this bot is created purely for entertainment. Just click the games button and have fun playing.
**"""




@Poki.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{POKI_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/DevsOops"),
          InlineKeyboardButton("ᴅᴇᴠ", url="https://t.me/iam_daxx"),
      
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/f2a5f823b4c0793452504.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )


