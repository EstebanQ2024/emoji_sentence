import re
import emoji
from emoji import EMOJI_DATA

token = 'pizza'

for emoji_char, data in EMOJI_DATA.items():
    if data.get("en") == f':{token}:' or data.get("alias") == token:
        print(f"Emoji: {emoji_char}, Alias: {alias}, Description: {search_term}")