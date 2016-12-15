from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import pifacecad

updater = Updater(token='274985321:AAGk4FCxOx9_ft50O7wrYf2OgZ9rbo38NQ0')
dispatcher = updater.dispatcher

cad = pifacecad.PiFaceCAD()

def backlight_on(bot, update):
	cad.lcd.backlight_on()
	bot.sendMessage(chat_id=update.message.chat_id, text="backlight on")

start_handler = CommandHandler('backlight_on', backlight_on)
dispatcher.add_handler(start_handler)

def backlight_off(bot, update):
	cad.lcd.backlight_off()
	bot.sendMessage(chat_id=update.message.chat_id, text="backlight off")

start_handler = CommandHandler('backlight_off', backlight_off)
dispatcher.add_handler(start_handler)

def echo(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)
	cad.lcd.write(update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
