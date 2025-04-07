import re

TOXIC_KEYWORDS = [
    "asshole", "bitch", "stupid", "idiot", "fuck", "shit", "dumb", "jerk", "moron"
]

def is_toxic(text):
    text = text.lower()
    for word in TOXIC_KEYWORDS:
        if re.search(rf"\b{word}\b", text):
            return True
    return False
