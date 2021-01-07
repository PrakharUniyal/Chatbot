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
TOKEN = "1474907865:AAGqLgIV9keqdeeUVWNwO2svN2uFqx-kwLs"

url = "https://i.ibb.co/8NbCyb9/campus.jpg"

topics_keyboard = [
    ['Programming Club', 'Heuristics Club'], 
    ['Robotronics Club', 'Space Technology and Astronomy Cell', 'Yantrik Club'], 
    ['Entrepreneurship Cell', 'Nirmaan Club', 'Literary Society']
]

capt = "Welcome to IIT Mandi!, Beautiful Campus is worth the wait🙂"

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
    context.bot.send_photo(chat_id = update.effective_chat.id, photo=url2,caption=capt)

def clubs(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Choose Club/Society", 
        reply_markup=ReplyKeyboardMarkup(keyboard=topics_keyboard, one_time_keyboard=True))

def _help(update,context):
    help_text = "Hey! This is a help text"
    context.bot.send_message(chat_id = update.effective_chat.id,text = help_text)

def location_handler(update,context):
    print(update)
    chandi = np.array((30.741482, 76.768066))
    delhi = np.array((28.644800, 77.216721))
    mumbai = np.array((19.076090, 72.877426))
    user = np.array((update.message.location.latitude, update.message.location.longitude))
    print(user)

    chd = np.linalg.norm(chandi - user)
    ded = np.linalg.norm(delhi - user)
    mumd = np.linalg.norm(mumbai - user)
    if (mumd < ded and mumd < chd):
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text="Take a train till Mumbai then a flight to Chandigarh and then a bus from Chandigarh")
    elif (chd < mumd and chd < ded):
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text="Take a train till Chandigarh  then a bus from Chandigarh")
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Take a train till Delhi then a bus from Delhi")


def dialogflow_connector(update,context):
    intent, reply = get_reply(update.message.text, update.message.chat_id)

    if intent == "club_info":
        if reply!="":
            context.bot.send_message(chat_id=update.message.chat_id, text="You would like to know about "+reply+"? Sure I can tell you everything about "+reply+".")
        else:
            context.bot.send_message(chat_id=update.message.chat_id, text="Sorry I don't know about that :(")
    elif(intent=="reachcollege"):
        print("collegereach")
        context.bot.send_message(chat_id=update.message.chat_id, text="Please send your location")
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
    url_for_webhook = "https://3aa62d0ccbd0.ngrok.io/"
    bot = Bot(TOKEN)
    bot.set_webhook(url_for_webhook + TOKEN)

    dp = Dispatcher(bot,None)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", _help))
    dp.add_handler(CommandHandler("clubs", clubs))
    dp.add_handler(MessageHandler(Filters.text, dialogflow_connector))
    dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
    dp.add_handler(MessageHandler(Filters.location,location_handler))
    dp.add_error_handler(error)

    app.run(port=8443)
    #updater.start_polling()
    #logger.info("Started Polling")
    #updater.idle()