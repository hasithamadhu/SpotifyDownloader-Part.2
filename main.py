import wave, math, os, json, shutil, subprocess, asyncio, time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tqdm import tqdm
from fpdf import FPDF
import requests

import asyncio
import math
import os
import time
import wget
import aiofiles
import aiohttp
import youtube_dl

from yt_dlp import YoutubeDL
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import *
from youtube_search import YoutubeSearch
from random import randint
from urllib.parse import urlparse
from CGS import CGS
from CGS import arq
from CGS import aiohttpsession as session
from pyrogram import filters
from io import BytesIO
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
    
@bot.on_message(filters.command(["lyric"]))
async def lirik(_, message):
    rep = await message.reply_text("🔎 **searching lyrics...**")
    try:
        if len(message.command) < 2:
            await message.reply_text("**give a lyric name too !**")
            return
        query = message.text.split(None, 1)[1]
        resp = requests.get(f"https://api-tede.herokuapp.com/api/lirik?l={query}").json()
        result = f"{resp['data']}"
        await rep.edit(result)
    except Exception as ex:
        print(ex)
        await rep.edit("**Lyrics not found.** please give a valid song name !")
        
@CGS.on_message(filters.command(["video"]))
async def vsong(pbot, message):
    ydl_opts = {
        'format':'best',
        'keepvideo':True,
        'prefer_ffmpeg':False,
        'geo_bypass':True,
        'outtmpl':'%(title)s.%(ext)s',
        'quite':True
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
        views = results[0]["views"]
        results[0]["url_suffix"]
        results[0]["views"]
        rby = message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply_text("📥 **downloading video...**")
        with YoutubeDL(ydl_opts) as ytdl:
            rep = f'🎙 **Title**: [{title[:35]}]({link})\n🎬 **Source**: `YouTube`\n⏱️ **Duration**: `{duration}`\n📤 **By**: @CGSUPDATES '
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"❌**YouTube Download Error !*** {str(e)}\n\n Go support chat👉 @CGSsupport")
    preview = wget.download(thumbnail)
    await msg.edit("📤 **uploading video...**")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=rep,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Updates Channel📢", url=f"https://t.me/CGSUpdates")]]))
    try:
        os.remove(file_name)
        await msg.delete()
    except Exception as e:
        print(e)  
        
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
