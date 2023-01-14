import os
import sys

import requests
import dotenv

dotenv.load_dotenv()
SPLIT_LENGTH = 3000
API_URL = os.environ.get("API_URL", None)
if not API_URL:
    print("API_URL not found")
    sys.exit(1)

def translate_and_show(text):
    text_remain = text
    while text_remain:
        if len(text_remain) > SPLIT_LENGTH:
            # 1000文字以前の最後の改行で分割
            text_split = text_remain[:SPLIT_LENGTH].rfind("\n")
            text_1000, text_remain = text_remain[:text_split], text_remain[text_split:]
        else:
            text_1000 = text_remain
            text_remain = ""

        params = {"text": text_1000, "source": "en", "target": "ja"}
        response = requests.get(API_URL, params=params)
        if response.status_code != 200:
            print(response.text)
            sys.exit(1)
        print(response.json()["text"])

if __name__ == "__main__":
    text_en = sys.stdin.read()
    if not text_en:
        print("No input")
        sys.exit(1)

    elif len(text_en) > SPLIT_LENGTH * 10:
        print("Too long")
        if not input("Continue? [y/N] ").lower() == "y":
            sys.exit(1)

    translate_and_show(text_en)
