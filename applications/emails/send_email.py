import base64
import json
from email.message import EmailMessage

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import os
import pickle
import subprocess

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send"
]

# Read JSON secret from gopass
client_secret_json = subprocess.check_output(
    ["gopass", "show", "-o", "websites/google/gmail_api/client_secret_json"],
    text=True
)
client_config = json.loads(client_secret_json)

creds = None

# Load existing token if available
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

# If no valid credentials, run OAuth flow
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_config(
            client_config,
            SCOPES
        )
        creds = flow.run_local_server(port=0)

    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

# Build Gmail service
service = build('gmail', 'v1', credentials=creds)

# Create email
message = EmailMessage()
message.set_content("This email was sent using the Gmail REST API.")
message["To"] = "silvia.pipitone89@gmail.com"
message["From"] = "sample@gmail.com"
message["Subject"] = "Test Email via Gmail API"

# Encode message
encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

create_message = {
    'raw': encoded_message
}

# Send email
send_message = service.users().messages().send(
    userId="me",
    body=create_message
).execute()
print(send_message)
print(f"Message Id: {send_message['id']}")