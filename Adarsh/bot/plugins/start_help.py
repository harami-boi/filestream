# (c) adarsh-goel 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

if MY_PASS:
    buttonz = ReplyKeyboardMarkup(
        [
            ["start", "help", "login", "DC"],
            ["ping", "status""]
        ],
        resize_keyboard=True
    )
else:
    buttonz = ReplyKeyboardMarkup(
        [
            ["start", "help", "DC"],
            ["ping", "status"]
        ],
        resize_keyboard=True
    )


@StreamBot.on_message((filters.command("start") | filters.regex('start')) & filters.private)
async def start(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**New User Joined:**\n\n__My New Friend__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot!!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="__Sorry, You are Banned from using me. Contact the Developer__",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="<i>Join CHANNEL to use me</i>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join now ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),

            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Something went wrong",
                disable_web_page_preview=True)
            return
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Hi {message.from_user.mention(style="md")}!\nI am Telegram File to Link Generator Bot with Channel support.\nSend me any file and get a direct download link and streamable link.!',
        reply_markup=buttonz
    )


@StreamBot.on_message((filters.command("help") | filters.regex('help')) & filters.private)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**New User Joined **\n\n__My New Friend__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot!!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="__Sorry, You are Banned from using me. Contact the Developer__",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="<i>Join CHANNEL to use me</i>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join now", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),

            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Something went wrong",
                disable_web_page_preview=True)
            return
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Hi {message.from_user.mention(style="md")}!\nI am Telegram File to Link Generator Bot with Channel support.\nSend me any file and get a direct download link and streamable link.!',
        reply_markup=buttonz
    )
    
