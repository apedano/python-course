import requests
import subprocess

BOT_TOKEN = subprocess.check_output(
    [
        "gopass",
        "show",
        "-o",
        "websites/telegram/carrier_notifications_bot", #secret path
        "API token" #key inside the secret
    ],
    text=True
).strip()

print(BOT_TOKEN)


CHANNEL = "-1003852532614"

message = "Hello from Python 🚀"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

payload = {
    "chat_id": CHANNEL,
    "text": message
}

response = requests.post(url, json=payload)

print(response.json())