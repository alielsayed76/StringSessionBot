from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message, CallbackQuery, InlineKeyboardButton


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)


# Start Message
@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    user = await bot.get_me()
    mention = user.mention
    await bot.send_message(
        msg.chat.id,
        Data.START.format(msg.from_user.mention, mention),
        reply_markup=InlineKeyboardMarkup(Data.buttons),
    )


# Help Message
@Client.on_callback_query(filter("help"))
async def _help(_, query: CallbackQuery):
    await bot.edit_message(
        msg.chat.id, Data.HELP, reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )


# About Message
@Client.on_callback_query(filter("about"))
async def about(_, query: CallbackQuery):
    await bot.edit_message(
        msg.chat.id,
        Data.ABOUT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons),
    )


# Repo Message
@Client.on_callback_query(filter("repo"))
async def repo(_, query: CallbackQuery):
    await bot.edit_message(
        msg.chat.id,
        Data.REPO,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons),
    )
