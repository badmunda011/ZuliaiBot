from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Zuli import Zuli
from config import BOT_USERNAME

start_txt = """**
ɪ ᴀᴍ ᴢᴜʟɪ

ɪ ᴀᴍ ʙᴜɪʟᴛ ʙʏ ᴄᴏᴍʙɪɴɪɴɢ ᴠᴀʀɪᴏᴜꜱ ᴀɪ ᴄᴀᴘᴀʙɪʟɪᴛɪᴇꜱ. ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴀɴꜱᴡᴇʀꜱ ᴛᴏ ᴀʟʟ ʏᴏᴜʀ Qᴜᴇꜱᴛɪᴏɴꜱ, ᴀɴᴅ ʏᴏᴜ ᴄᴀɴ ᴀꜱᴋ ᴍᴇ ᴀɴʏ Qᴜᴇꜱᴛɪᴏɴꜱ ʏᴏᴜ ʜᴀᴠᴇ. ᴀᴅᴅɪᴛɪᴏɴᴀʟʟʏ, ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ɪᴍᴀɢᴇꜱ ᴀɴᴅ ᴇᴠᴇɴ ᴇᴅɪᴛ ᴄᴏɴᴛᴇɴᴛ. ɪ ʜᴀᴠᴇ ᴍᴀɴʏ ꜰᴇᴀᴛᴜʀᴇꜱ ᴀᴛ ᴍʏ ᴅɪꜱᴘᴏꜱᴀʟ
**"""




@Zuli.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url="https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/DevsOops"),
          InlineKeyboardButton("ᴅᴇᴠ", url="https://t.me/iam_daxx"),
          InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help_")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/f2a5f823b4c0793452504.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )





