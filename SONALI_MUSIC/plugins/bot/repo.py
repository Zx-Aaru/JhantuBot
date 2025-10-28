from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI_MUSIC import app
from config import BOT_USERNAME
from SONALI_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
<u>❃ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛᴇᴧᴍ ᴧᴧʀᴜᴍɪ ʀᴇᴘᴏs ❃</u>
 
✼ ʀᴇᴘᴏ ɪs ɴᴏᴡ ᴘʀɪᴠᴧᴛᴇ ᴅᴜᴅᴇ 😌
 
❉  ʏᴏᴜ ᴄᴧɴ ᴜsᴇ ᴍʏ ᴘᴜʙʟɪᴄ ʀᴇᴘᴏs !!  

✼ || [˹ ᴧᴧʀᴜᴍɪ sᴜᴘᴘᴏʀᴛ ᴄʜᴧᴛ ˼](https://t.me/AarumiChat) ||
 
❊ ʀᴜn 24x7 ʟᴧɢ ϝʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴧᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴧᴛ ✙", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/AarumiChat"),
          InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url="https://t.me/AarumiBots"),
          ],
[
InlineKeyboardButton("ᴍᴧɪɴ ʙᴏᴛ", url=f"https://t.me/AarumiSongBot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/kbi6t5.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
