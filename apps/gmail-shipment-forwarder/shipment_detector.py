import re

TRACKING_PATTERNS = {
    "UPS": r"1Z[0-9A-Z]{16}",
    "FedEx": r"\b\d{12,14}\b",
    "DHL": r"\b\d{10}\b",
    "PostNL": r"[A-Z]{2}\d{9}[A-Z]{2}"
}

def detect_tracking(body):

    for carrier, pattern in TRACKING_PATTERNS.items():

        match = re.search(pattern, body)

        if match:
            return carrier, match.group(0)

    return None, None