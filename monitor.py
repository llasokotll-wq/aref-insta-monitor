# monitor.py

import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def notify(user):
    msg = f"📣 اسم عارف در پیج {user} دیده شد!"
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                  data={"chat_id": CHAT_ID, "text": msg})

with open("pages.txt") as f:
    for u in f:
        if "aref" in u.lower():
            notify(u.strip())
