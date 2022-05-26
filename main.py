import wave, math, os, json, shutil, subprocess, asyncio, time
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from vosk import Model, KaldiRecognizer
from display_progress import progress_for_pyrogram, download_progress_hook, read_stderr
from yt_dlp import YoutubeDL
from tqdm import tqdm
from fpdf import FPDF
import requests


BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
# vosk supported language(code), see supported languages here: https://github.com/alphacep/vosk-api
LANGUAGE_CODE = os.environ.get("LANGUAGE_CODE", "en-us")
# language model download link (see available models here: https://alphacephei.com/vosk/models)
MODEL_URL = os.environ.get("MODEL_DOWNLOAD_URL", "https://alphacephei.com/vosk/models/vosk-model-en-us-0.22-lgraph.zip")
# transcript sending format (PDF or TXT)
TRANSCRIPT_FORMAT = os.environ.get("SEND_AS", "TXT")

Bot = Client(
    "Transcript-Extractor-Bot",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH
)

START_TXT = """
Hi {},
I am Transcript Extractor Bot.

Just send a video/audio/voice or a YouTube URL.
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Source Code', url='https://github.com/samadii/Transcript-Extractor-Bot'),
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


Bot.run()
