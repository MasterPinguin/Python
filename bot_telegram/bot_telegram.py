from random import choice
from glob import glob
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "6365175140:AAFXuzN2jD7EWVcQVM0_2IW7czsAX9ZepL0"

def start(update, context):
    update.message.reply_text("MIAO MAO ME GO")

def rispondi(update,context):
    testo = update.message.text.lower()
    if "dove sei" in testo:
        update.message.reply_venue(41.6165505090578, 15.88433994424645, "Via Mario Valente", "71043 Manfredonia FG")
    elif "nonno" in testo:
        update.message.reply_contact("+390000000000","Nonno Lino")
    elif "don matteo" in testo:
        immagini = glob("/Users/newmac/Documents/PROG/Pythone/bot_telegram/don_matteo/*.jpg")
        if immagini:
            immagine = choice(immagini)
            update.message.reply_photo(open(immagine, 'rb'))
        else:
            # Nessuna immagine trovata
            update.message.reply_text("Nessuna immagine disponibile.")

    else:
        update.message.reply_video(open('/Users/newmac/Documents/PROG/Pythone/bot_telegram/dolce_gattino.mp4', 'rb'))


updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, rispondi))
print("bot in ascolto ...")
updater.start_polling()