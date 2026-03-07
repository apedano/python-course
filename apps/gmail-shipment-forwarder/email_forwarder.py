from email.message import EmailMessage
import base64

def forward_email(service, body, tracking, carrier, destination):

    message = EmailMessage()

    message["To"] = destination
    message["From"] = "me"
    message["Subject"] = f"📦 Shipment update ({carrier})"

    message.set_content(
        f"""
Carrier: {carrier}
Tracking: {tracking}

Original email:

{body}
"""
    )

    encoded = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    service.users().messages().send(
        userId="me",
        body={"raw": encoded}
    ).execute()