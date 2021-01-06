import logging
from flask import Flask, request
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters, Dispatcher
from telegram import ReplyKeyboardMarkup,Bot,Update
from utils import get_reply


#enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


#Telegram Bot token
#TOKEN = "1531582165:AAHNtmQ4lyWZ55Rkf0Hs9KxzcB0woGGeX0E"
TOKEN = "1546162713:AAEnv2MvukJma18_GuVqCF92NUaFYITwlBc"

url = "https://cache.careers360.mobi/media/article_images/2020/5/12/iit-mandi_625x300_1530963089382.jpg"

topics_keyboard = [
    ['Programming Club', 'Heuristics Club'], 
    ['Robotronics Club', 'Space Technology and Astronomy Cell', 'Yantrik Club'], 
    ['Entrepreneurship Cell', 'Nirmaan Club', 'Literary Society']
]

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello!"


@app.route(f'/{TOKEN}', methods=['GET', 'POST'])
def webhook():
    """webhook view which receives updates from telegram"""
    # create update object from json-format request data
    update = Update.de_json(request.get_json(), bot)
    # process update
    dp.process_update(update)
    return "ok"


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

def dialogflow_connector(update,context):
    intent, reply = get_reply(update.message.text, update.message.chat_id)
    if intent == "club_info":
        if reply!="":
            context.bot.send_message(chat_id=update.message.chat_id, text="You would like to know about "+reply+"? Sure I can tell you everything about "+reply+".")
        else:
            context.bot.send_message(chat_id=update.message.chat_id, text="Sorry I don't know about that :(")
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text=reply)

def echo_sticker(update,context):
    """callback function for sticker message handler"""
    context.bot.send_sticker(chat_id=update.effective_chat.id,
                     sticker=update.message.sticker.file_id)


def error(update,context):
    """callback function for error handler"""
    logger.error("Update '%s' caused error '%s'", update, context.error)

if __name__ == "__main__":
    #updater = Updater(TOKEN)
    bot = Bot(TOKEN)
    bot.set_webhook("https://e64444a06b1c.ngrok.io/" + TOKEN)

    dp = Dispatcher(bot,None)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", _help))
    dp.add_handler(CommandHandler("clubs", clubs))
    dp.add_handler(MessageHandler(Filters.text, dialogflow_connector))
    dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
    dp.add_error_handler(error)

    app.run(port=8443)
    #updater.start_polling()
    #logger.info("Started Polling")
    #updater.idle()



