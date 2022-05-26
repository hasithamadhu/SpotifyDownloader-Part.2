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
from pyrogram import filters


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

Send me the name of the song you want to download

✍️ @BotsLanka</b>
"""

START_BTN = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('📣 Update Channel', url='https://t.me/BotsLanka'),
            InlineKeyboardButton('♥️ Help ', url='https://t.me/BotsLanka/6')
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
    
Bot.run()
