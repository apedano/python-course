import json
import subprocess

def load_client_config():

    # Read JSON secret from gopass
    client_secret_json = subprocess.check_output(
        ["gopass", "show", "-o", "websites/google/gmail_api/client_secret_json"],
        text=True
    )
    client_config = json.loads(client_secret_json)
    return client_config