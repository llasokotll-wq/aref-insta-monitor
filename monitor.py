import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def notify(username, message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": f"📣 در پیج {username}:\n\n{message}"
    }
    requests.post(url, data=data)

with open("pages.txt") as f:
    for username in f:
        username = username.strip()
        if "aref" in username.lower():
            notify(username, f"اسم عارف در پیج {username} دیده شد.")
