# 🐍 Python telegram integration

## Send messages using a Telegram bot on a channel

### Create a bot

Search for `BotFather` https://web.telegram.org/k/#@BotFather

Start the bot creation with `/start` and then `/newbot`

```
bot name: carrier_notifications_bot
bot user: automatic_messsages_bot
```

At the end of the process the API key to be used in combination with the bot


### Create a channel and get ID

Once the new channel is created https://t.me/+3e0nUZtBXsc5YWRk, 
the administrator can add the bot user name to the group

Clicking on the channel in the web view, the ID will be shown on the url: https://web.telegram.org/k/#-3852532614

**Important**:Supergroups and channels usually start with -100.

So the real ID may actually be:

`-1003852532614` not `-3852532614`

### Send messages script

```python
iimport requests
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
```