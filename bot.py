import json
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = "8770670315:AAHLIJUJ2IJshm-pSpFRKQZx-LHo5MP3OPk"

with open("farms.json") as f:
    farms = json.load(f)

def reply(update, context):
    text = update.message.text.lower()

    for farm in farms:
        if farm["name"].lower() in text or farm["area"].lower() in text:
            msg = f"""Name: {farm['name']}
Phone: {farm['phone']}
Area: {farm['area']}
Location: {farm['location']}"""
            update.message.reply_text(msg)
            return

    update.message.reply_text("Farmer not found")

updater = Updater(TOKEN)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, reply))

updater.start_polling()
updater.idle()
