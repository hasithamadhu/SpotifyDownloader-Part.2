import wave, math, os, json, shutil, subprocess, asyncio, time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tqdm import tqdm
from fpdf import FPDF
import requests


BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

Bot = Client(
    "SpotifyDownloader-Part.2",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH
)

START_TXT = """
<b>Hi {},
This is a simple bot to download songs from spotify in an mp3 format. 

📌 You can download:
  ▫️A single song
  ▫️Albums
  ▫️Playlists
  ▫️Artists

How to use me - /help

✍️ @BotsLanka</b>
"""

HELP_TXT = """
<b>🤝 Help Menu :
Select your language ,</b>
"""

ENHELP_TXT = """
<b>📌 If there is only one song you want to download, send the name of the song correctly to Bot.

📌 If you want to download an Album / Artists or Playlist from the Spoyify platform, send its link to Bot.

✍️ @BotsLanka</b>
"""

SIHELP_TXT = """
<b>📌 ඔබට බාගත කරගැනිමට අවශ්‍ය එක සින්දුවක් නම් ,  සින්දුවේ නම නිවැරදිව Bot වෙත එවන්න. 

📌 ඔබට බාගත කරගැනීමට අවශ්‍ය වන්නේ Spoyify වේදිකාවේ ඇති Album / Artists හෝ Playlist එකක් නම් එහි සබැදිය(Link) Bot වෙත එවන්න.

✍️ @BotsLanka</b>
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📣 Update Channel', url='https://t.me/+-M8hbzsqhZ9kOGJl'),
        ]]
    )
HELP_BTN = = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('English 🇦🇺', callback_data='enghelp'),
        InlineKeyboardButton('සිංහල 🇱🇰', callback_data='sihelp')
        ]]
    )

@Bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Bot.on_message(filters.command(["help"]))
async def start(bot, update):
    text = HELP_TXT.format(update.from_user.mention)
    reply_markup = HELP_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

await query.answer('How To use me in English')
    elif query.data == "enghelp":
        buttons = [[
            InlineKeyboardButton('Back 🏃‍♂️', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ENHELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
    )
 
await query.answer('How To use me in Sinhala')
    elif query.data == "sihelp":
        buttons = [[
            InlineKeyboardButton('Back 🏃‍♂️', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SIHELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode='html'
    )

Bot.run()
