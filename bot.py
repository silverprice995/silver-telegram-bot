import requests
import time
import os
from telegram import Bot

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

def get_silver_price():
    url = "https://api.metals.live/v1/spot/silver"
    r = requests.get(url)
    data = r.json()
    price = data[0]["silver"]
    return price

last_price = None

while True:
    try:
        price = get_silver_price()
        
        if price != last_price:
            message = f"Silver price995\nقیمت لحظه‌ای اونس نقره: {price}$"
            bot.send_message(chat_id=CHAT_ID, text=message)
            last_price = price

        time.sleep(30)

    except Exception as e:
        print(e)
        time.sleep(30)
