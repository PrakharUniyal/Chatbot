import logging
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters, Dispatcher
from telegram import ReplyKeyboardMarkup

#enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    level=logging.INFO)
logger = logging.getLogger(__name__)


#Telegram Bot token
TOKEN = "1531582165:AAHNtmQ4lyWZ55Rkf0Hs9KxzcB0woGGeX0E"

url = "https://cache.careers360.mobi/media/article_images/2020/5/12/iit-mandi_625x300_1530963089382.jpg"

topics_keyboard = [
    ['Programming Club', 'Heuristics Club'], 
    ['Robotronics Club', 'Space Technology and Astronomy Cell', 'Yantrik Club'], 
    ['Entrepreneurship Cell', 'Nirmaan Club', 'Literary Society']
]


def start(update, context):
	print(update)
	author = update.message.from_user.first_name
	reply = "Hi! {}".format(author)
	# context.bot.send_message(chat_id = update.effective_chat.id,text = reply)
	context.bot.send_photo(chat_id = update.effective_chat.id, photo=url)

def clubs(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Choose Club/Society", 
        reply_markup=ReplyKeyboardMarkup(keyboard=topics_keyboard, one_time_keyboard=True))

def _help(update,context):
	help_text = "Hey! This is a help text"
	context.bot.send_message(chat_id = update.effective_chat.id,text = help_text)

def echo_text(update,context):
	reply = update.message.text
	author = update.message.from_user.first_name
	print("Message typed by :",author," is -->",reply)
	context.bot.send_message(chat_id=update.effective_chat.id,text=reply)

def echo_sticker(update,context):
    """callback function for sticker message handler"""
    context.bot.send_sticker(chat_id=update.effective_chat.id,
                     sticker=update.message.sticker.file_id)


def error(update,context):
    """callback function for error handler"""
    logger.error("Update '%s' caused error '%s'", update, context.error)


def main():
	updater = Updater(TOKEN)

	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("clubs", clubs))
	dp.add_handler(CommandHandler("help", _help))
	dp.add_handler(MessageHandler(Filters.text, echo_text))
	dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
	dp.add_error_handler(error)


	updater.start_polling()
	logger.info("Started Polling")
	updater.idle()

if __name__ == "__main__":
	main() 