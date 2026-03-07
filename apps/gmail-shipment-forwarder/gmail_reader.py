import base64

def search_messages(service, query):

    result = service.users().messages().list(
        userId="me",
        q=query
    ).execute()

    return result.get("messages", [])


def get_message_body(service, msg_id):

    msg = service.users().messages().get(
        userId="me",
        id=msg_id,
        format="full"
    ).execute()

    payload = msg["payload"]

    if "parts" not in payload:
        return ""

    for part in payload["parts"]:

        if part["mimeType"] == "text/plain":
            data = part["body"]["data"]

            return base64.urlsafe_b64decode(data).decode()

    return ""