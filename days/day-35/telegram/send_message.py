BOT_TOKEN = "***"
CHANNEL_ID = "-1003852532614"

import requests

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = "-1001234567890"

def send_notification(text: str) -> None:
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHANNEL_ID,
        "text": text
    })

send_notification("Server restarted")

