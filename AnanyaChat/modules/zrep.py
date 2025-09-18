import asyncio
import random
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import IMG
from AnanyaChat import AnanyaBot

start_txt = """<b>
✪ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ @ᴀɴᴀɴʏᴀʙᴏᴛs ✪

➲ ᴇᴀsʏ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ  
➲ ɴᴏ ʙᴀɴ ɪssᴜᴇs  
➲ ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs  
➲ 𝟸𝟺/𝟽 ʟᴀɢ-ғʀᴇᴇ  

⟢ ᴄʜᴇᴄᴋ ᴏᴜᴛ ᴍʏ ʀᴇᴘᴏs  
⟢ sᴛᴀʏ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴡɪᴛʜ ᴛʜᴇ ᴄᴏᴍᴍᴜɴɪᴛʏ!
</b>"""

repo_buttons = [
    [InlineKeyboardButton("⋆ ᴍᴜsɪᴄ + ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ⋆", url="http://github.com/ZOXXOP/AnanyaMusic")],
    [InlineKeyboardButton("⋆ ᴍᴜsɪᴄ ⋆", url="http://github.com/ZOXXOP/AnanyaxMusic")],
    [InlineKeyboardButton("⋆ ᴄʜᴀᴛʙᴏᴛ ⋆", url="http://github.com/ZOXXOP/AnanyaxChat")],
    [InlineKeyboardButton("⋆ ɴᴏʀᴍᴀʟ ᴄʜᴀᴛʙᴏᴛ ⋆", url="http://github.com/ZOXXOP/AnanyaChat")],
    [InlineKeyboardButton("⋆ ᴄᴏᴍᴍᴜɴɪᴛʏ ⋆", url="https://t.me/AnanyaBots")],
]


async def send_repo(_, m: Message):
    reply_markup = InlineKeyboardMarkup(repo_buttons)
    await m.reply_photo(
        photo="https://files.catbox.moe/a52uxu.jpg",
        caption=start_txt,
        reply_markup=reply_markup,
    )


@AnanyaBot.on_cmd(["repo", "repos", "source", "repo_source"])
async def repo_handler(client, message: Message):
    await send_repo(client, message)
  
