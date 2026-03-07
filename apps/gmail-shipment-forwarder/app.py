import subprocess
import json
from googleapiclient.discovery import build

from gmail_auth import get_credentials
from gmail_reader import search_messages, get_message_body
from shipment_detector import detect_tracking
from email_forwarder import forward_email
from config import SHIPMENT_QUERY, DESTINATION_EMAIL
from client_config_loader import load_client_config


def main():

    client_config = load_client_config()

    creds = get_credentials(client_config)

    service = build("gmail", "v1", credentials=creds)

    messages = search_messages(service, SHIPMENT_QUERY)

    for msg in messages:

        body = get_message_body(service, msg["id"])

        carrier, tracking = detect_tracking(body)

        if tracking:

            forward_email(
                service,
                body,
                tracking,
                carrier,
                DESTINATION_EMAIL
            )


if __name__ == "__main__":
    main()