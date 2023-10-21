import pymongo
import pyotp
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Celestia import Celestia 


mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["phone_numbers"]
indian_collection = db["indian_numbers"]
usa_collection = db["usa_numbers"]
users_collection = db["users"]





totp_secret = pyotp.random_base32()


user_otps = {}


def save_phone_number(collection, phone_number):
    collection.insert_one({"number": phone_number})


def remove_phone_number(collection, phone_number):
    collection.delete_one({"number": phone_number})



@Celestia.on_message(filters.command("register"))
async def register_command(_, message):
    user_id = message.from_user.id

    
    totp = pyotp.TOTP(totp_secret)
    otp = totp.now()

    
    user_otps[user_id] = otp

    await message.reply(f"Please use this OTP to register: {otp}")



@Celestia.on_message(filters.command("verify"))
async def verify_command(_, message):
    user_id = message.from_user.id
    if user_id in user_otps:
        saved_otp = user_otps[user_id]
        user_otp = message.command[1]

        if saved_otp == user_otp:
            await message.reply("Registration successful!")

            
            del user_otps[user_id]
            users_collection.insert_one({"user_id": user_id, "registered": True})
        else:
            await message.reply("Invalid OTP. Please try again.")
    else:
        await message.reply("You haven't requested registration. Use /register to get an OTP.")




@Celestia.on_callback_query(filters.regex("get_indian_number"))
async def get_indian_number(_, callback_query):
    user_id = callback_query.from_user.id

    
    user = users_collection.find_one({"user_id": user_id, "registered": True})
    if user:
        number = indian_collection.find_one()
        if number:
            await callback_query.message.edit_text(f"Here's your Indian number: {number['number']}")
            remove_phone_number(indian_collection, number['number'])
        else:
            await callback_query.message.edit_text("No Indian numbers available right now.")
    else:
        await callback_query.message.edit_text("You need to register to use this feature.")




@Celestia.on_message(filters.command("save"))
async def save_command(_, message):
    if len(message.command) == 3:
        country = message.command[1].lower()
        phone_number = message.command[2]
        
        if country == "indian":
            save_phone_number(indian_collection, phone_number)
            await message.reply(f"Indian phone number {phone_number} saved.")
        elif country == "usa":
            save_phone_number(usa_collection, phone_number)
            await message.reply(f"USA phone number {phone_number} saved.")
        else:
            await message.reply("Invalid country. Use '/save indian/usa <phone_number>'")






