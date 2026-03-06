from flask import Flask, request
import requests
import webbrowser
from threading import Thread

app = Flask(__name__)

# ===== CONFIGURATION =====
CLIENT_ID = "google-id-123"
CLIENT_SECRET = "dummy-google-secret"
AUTHORIZATION_URL = "https://oauth-mock.mock.beeceptor.com/oauth/authorize"
TOKEN_URL = "https://oauth-mock.mock.beeceptor.com/oauth/token/google"
REDIRECT_URI = "http://127.0.0.1:5000/callback"
SCOPE = "photo+offline_access"  # depends on API

access_token = None


# ===== ROUTES =====
@app.route("/")
def index():
    # Step 1: Redirect user to OAuth provider
    return f'<a href="{AUTHORIZATION_URL}?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPE}">Login with OAuth2</a>'


@app.route("/callback")
def callback():
    global access_token
    # Step 2: Get authorization code
    code = request.args.get("code")
    if not code:
        return "No code found", 400

    # Step 3: Exchange code for access token
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    response = requests.post(TOKEN_URL, data=data)
    response.raise_for_status()
    token_data = response.json()
    print(token_data)
    access_token = token_data.get("access_token")
    return f"Access token received: {access_token[:10]}..."  # hide most of token

def open_browser():
    webbrowser.open("http://127.0.0.1:5000/")

if __name__ == "__main__":
    # Open browser in a separate thread
    Thread(target=open_browser).start()
    app.run(port=5000)