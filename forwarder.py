from telethon import TelegramClient, events
import re

# --- CONFIGURATION ---
api_id = 39719995
api_hash = '8f9b2cf0583c4e31193ce318a0ef0e7a'

# Smiya dyal l-bot jdid dyalk (L-khezna)
target_bot = '@forwarderm3u_bot' 

client = TelegramClient('universal_session', api_id, api_hash)

@client.on(events.NewMessage()) # Bla 'chats=' bach i-checki kolchi
async def handler(event):
    # 1. Skip messages mn l-bot dyal l-khezna rasso bach madir-ch Loop
    if event.chat_id == (await client.get_entity(target_bot)).id:
        return

    text = event.raw_text
    if not text: return

    # 2. Regex l-mtiwwer bach i-qcha3 l-ishtiira-kat
    # Kiy-qleb 3la (http + get.php) oula (http + .m3u) oula (username=)
    iptv_pattern = r'http[s]?://[^\s]+(?:get\.php|\.m3u|username=)'
    links = re.findall(iptv_pattern, text, re.IGNORECASE)
    
    if links:
        # 3. Jbed smiya dyal l-blassa mni jay l-link
        try:
            chat = await event.get_chat()
            chat_title = getattr(chat, 'title', 'Private Chat')
        except:
            chat_title = "Unknown Source"

        # 4. M9add l-message
        msg = f"🛰️ **New IPTV Found**\n"
        msg += f"📍 **Source:** `{chat_title}`\n"
        msg += f"━━━━━━━━━━━━━━━\n"
        for link in list(set(links)):
            msg += f"🔗 `{link}`\n\n"
        
        print(f"🎯 Captured links from: {chat_title}")
        
        # 5. Sifthoum l l-bot dyalk
        await client.send_message(target_bot, msg)

print("[*] UserBot Universal is RUNNING...")
print("[*] Monitoring ALL groups, channels, and chats...")
client.start()
client.run_until_disconnected()