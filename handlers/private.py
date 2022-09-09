import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os

master_user = os.environ.get("MASTER_USERNAME", None)

if "@" in master_user: 
    master_user.replace("@", "")

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5754a1c5b7f00258f3f7c.jpg",
        caption=f"""**✨  ʙᴇsᴛ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ
💫  ᴇᴀsʏ ᴅᴇᴘʟᴏʏ
💫  ʙᴀsᴇᴅ ᴏɴ ᴘʏʀᴏɢʀᴀᴍ
💫  ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛs
💫  ʙᴇᴡ ғᴇᴀᴛᴜʀᴇs
💫  ᴍᴀᴅᴇ ʙʏ [ᴏғғɪᴄɪᴀʟ ʜᴀᴄᴋᴇʀ](https://t.me/OFFICIALHACKERERA)
💫  ᴀʟᴡᴀʏs ᴡɪʟʟ ᴜᴘᴅᴀᴛᴇ
💫  ʙᴇsᴛ ᴀɴᴅ sᴇᴄᴜʀᴇ
💫  ғᴀsᴛ sᴍᴏᴏᴛʜ ᴀɴᴅ sᴛʏʟɪsʜ
✨  [ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ](t.me/PLUS_MUSIC_BOT?startgroup=new)

**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="• ᴄʜᴀɴɴᴇʟ •",
                            url=f"https://t.me/Broken_Heart_72"),

                            InlineKeyboardButton(
                            text="• ᴏᴡɴᴇʀ •",
                            url=f"https://t.me/OFFICIALHACKERERA"),
                            
                    InlineKeyboardButton(
                            text="• sᴜᴘᴘᴏʀᴛ •",
                            url=f"https://t.me/HEPPYLIFI")
               ]
           ]
       ),
    )





@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5754a1c5b7f00258f3f7c.jpg",
        caption=f"""**ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴀʙᴏᴜᴛ ᴍᴇ ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](https://t.me/OFFICIALHACKERERA)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="💥 ULTRA X MUSIC 💥",
                            url=f"lauda le lo bsdk"),
                            
                    InlineKeyboardButton(
                            text="💞 USERBOT REPO 💝",
                            url=f"maa chudwa lo bsdk")
                ],
                [
 
                     InlineKeyboardButton(
                            text="💫 Channel 💫",
                            url=f"https://t.me/studynsn"),
                            
                    InlineKeyboardButton(
                            text="💫 Support 💫",
                            url=f"https://t.me/studynsn")
 

               ],
               [
                
                    InlineKeyboardButton(
                        "💥 All Repo 💞", url=f"https://t.me/krishna_devill_boy")


              ],
              [

                   InlineKeyboardButton(
                        "♥️ Owner ♥️", url=f"https://t.me/krishna_devill_boy")

             ]
           ]
        ),
    )
