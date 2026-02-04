import os
import re
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from flask import Flask
from threading import Thread

api_id = 39719995
api_hash = '8f9b2cf0583c4e31193ce318a0ef0e7a'

# Railway ghadi i-at7ina had l-m3lomat mn l-Variables
session_str = os.getenv("SESSION_STRING")
target_bot = os.getenv("TARGET_BOT")

# Fake Server l Railway bach i-bqa Healthy
app = Flask('')
@app.route('/')
def home(): return "Healthy"
def run(): app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

client = TelegramClient(StringSession(session_str), api_id, api_hash)

@client.on(events.NewMessage())
async def handler(event):
    text = event.raw_text
    if not text: return
    urls = re.findall(r'(https?://[^\s]+)', text)
    found = [u for u in urls if any(k in u.lower() for k in ["get.php", ".m3u", "password="])]
    if found:
        try:
            await client.send_message(target_bot, f"🛰️ **IPTV Found**\n" + "\n".join([f"🔗 `{l}`" for l in found]))
        except: pass

if __name__ == "__main__":
    Thread(target=run).start()
    client.start()
    client.run_until_disconnected()
