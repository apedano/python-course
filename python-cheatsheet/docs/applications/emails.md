#  🐍 Gmail REST API Guide in Python

## Overview

This guide explains how to send emails using the Gmail REST API with
OAuth2 authentication in a Python application.

Using the Gmail REST API is often simpler and more modern than using
SMTP with XOAUTH2.

------------------------------------------------------------------------

# 1️⃣ Create a Google Cloud Project

1.  Go to: https://console.cloud.google.com/
2.  Create a **New Project**
3.  Navigate to **APIs & Services → Library**
4.  Enable:
    -   ✅ Gmail API
5.  Go to **APIs & Services → Credentials**
6.  Click **Create Credentials → OAuth client ID**
7.  Choose:
    -   Desktop App (for local applications)
8.  Download the `credentials.json` file

Save it in your project directory.

------------------------------------------------------------------------

# 2️⃣ Install Required Libraries

``` bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

------------------------------------------------------------------------

# 3️⃣ Required OAuth Scope

For sending emails, use:

``` python
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
```

------------------------------------------------------------------------

# 4️⃣ Python Example -- Send Email Using Gmail REST API

This example: - Opens browser for authentication - Obtains OAuth2
token - Sends email using Gmail API

``` python
import base64
from email.message import EmailMessage

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import os
import pickle

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

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
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json',
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
message["To"] = "recipient@example.com"
message["From"] = "your_email@gmail.com"
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

print(f"Message Id: {send_message['id']}")
```

------------------------------------------------------------------------

# 5️⃣ How It Works

    Python App
        ↓
    OAuth2 Login (Browser)
        ↓
    Google Authorization Server
        ↓
    Access Token
        ↓
    Gmail REST API (HTTPS)
        ↓
    Email Sent

------------------------------------------------------------------------

# Advantages of REST API Over SMTP

-   No manual XOAUTH2 handling
-   Automatic token refresh
-   Fully HTTPS-based
-   Cleaner authentication flow
-   Better suited for server and cloud apps

------------------------------------------------------------------------

# Common Scopes

  Purpose       Scope
  ------------- ------------------------------------------------
  Send only     https://www.googleapis.com/auth/gmail.send
  Read only     https://www.googleapis.com/auth/gmail.readonly
  Full access   https://mail.google.com/

------------------------------------------------------------------------

# Production Tips

-   Store `credentials.json` securely
-   Protect `token.pickle`
-   Use environment variables in production
-   Consider Service Accounts for domain-wide delegation (Google
    Workspace)

------------------------------------------------------------------------

End of Guide
