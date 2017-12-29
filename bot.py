from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import cleverbot

cb = cleverbot.Cleverbot('CC4zfUgbrPndTHT3tLdz3q9-2DA')

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def say(bot, update):
    reply = cb.say(update.message.text)
    bot.send_message(chat_id=update.message.chat_id, text=reply)

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

if __name__ == '__main__':
    updater = Updater(token='506075389:AAHhc04sGoAwXS97dQjx53oi3_OsyIyaAqw')
    dispatcher = updater.dispatcher

    say_handler = CommandHandler('say', say)
    dispatcher.add_handler(say_handler)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()
    updater.idle()
