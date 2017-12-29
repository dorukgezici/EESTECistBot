from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import cleverbot

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Yazın konuşalım beybiler ;)")

def say(bot, update):
    reply = cb.say(update.message.text)
    bot.send_message(chat_id=update.message.chat_id, text=reply)

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Bu komutu bilmiyorum.")

if __name__ == '__main__':
    cb = cleverbot.Cleverbot('CC4zfUgbrPndTHT3tLdz3q9-2DA')
    updater = Updater(token='506075389:AAHhc04sGoAwXS97dQjx53oi3_OsyIyaAqw')
    dispatcher = updater.dispatcher

    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)

    say_handler = CommandHandler("say", say)
    dispatcher.add_handler(say_handler)

    echo_handler = CommandHandler("echo", echo)
    dispatcher.add_handler(echo_handler)

    default_handler = MessageHandler(Filters.text, say)
    dispatcher.add_handler(default_handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()
    updater.idle()
