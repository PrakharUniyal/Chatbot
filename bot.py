import logging
from flask import Flask, request
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters, Dispatcher
from telegram import ReplyKeyboardMarkup,Bot,Update,ParseMode
from utils import get_reply
from firebaseutils import answers_collection
import speech_recognition as sr
import os

#enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


#Telegram Bot Token
# TOKEN = "1474907865:AAGqLgIV9keqdeeUVWNwO2svN2uFqx-kwLs" #stresstest_bot
# TOKEN = "1531582165:AAHNtmQ4lyWZ55Rkf0Hs9KxzcB0woGGeX0E" #iitmandi_bot
# TOKEN="1546162713:AAEnv2MvukJma18_GuVqCF92NUaFYITwlBc" #KDbot
TOKEN = "1599589352:AAGzf5C0EjT53FsZH63_mfcdlXbJh_vmEs8" #prakharuniyalbot

welcome_msg = "Welcome to IIT Mandi!, Beautiful Campus is worth the wait🙂\n"

imageurls = {
    "campus":
    "https://i.ibb.co/8NbCyb9/campus.jpg"
}

dict_intents = set()
for doc in answers_collection.get():
    dict_intents.add(doc.get('intent'))

rec = sr.Recognizer()

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
    reply = "Hi! <b>{}</b>\n".format(author)
    reply+= welcome_msg
    context.bot.send_photo(chat_id = update.effective_chat.id,
                        photo=imageurls["campus"],caption=reply,parse_mode=ParseMode.HTML)

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

    response = get_reply(update.message.text, update.message.chat_id)
    intent=response.intent.display_name


    print("--------")
    print(response)
    print("intent:->", intent)
    print("--------")

    if(intent in dict_intents):
        intent_response = answers_collection.where('intent', '==', intent).get()[0]
        reply_text = intent_response.get('text')
        imgrefs = intent_response.get('imgrefs')
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text= reply_text,
                                 parse_mode=ParseMode.HTML)
        for imgref in imgrefs:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=imgref)

    else:
        if intent == "Default Fallback Intent":
            f = open('logs.txt', 'a')
            f.write(update.message.text+'\n')
            f.close()
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=response.fulfillment_text,
                                 parse_mode=ParseMode.HTML)


def voice_to_text(update, context):
    chat_id = update.message.chat_id
    file_name = str(chat_id) + '_' + str(update.message.from_user.id) + str(update.message.message_id)
    update.message.voice.get_file().download(file_name+'.ogg')
    os.system('ffmpeg -i '+file_name+'.ogg '+file_name+'.wav')
    os.system('rm '+file_name+'.ogg')
    harvard = sr.AudioFile(file_name+'.wav')
    with harvard as source:
        audio = rec.record(source)

    message_text = rec.recognize_google(audio)

    os.system('rm ' + file_name + '.wav')

    response = get_reply(message_text, chat_id)
    intent = response.intent.display_name

    
    print("--------")
    print(response)
    print("intent:->", intent)
    print("--------")

    if (intent in dict_intents):
        intent_response = answers_collection.where('intent', '==', intent).get()[0]
        reply_text = intent_response.get('text')
        imgrefs = intent_response.get('imgrefs')
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=reply_text,
                                 parse_mode=ParseMode.HTML)
        for imgref in imgrefs:
            context.bot.send_photo(chat_id=update.effective_chat.id,
                                   photo=imgref)

    else:
        if intent == "Default Fallback Intent":
            f = open('logs.txt', 'a')
            f.write(update.message.text+'\n')
            f.close()
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=response.fulfillment_text,
                                 parse_mode=ParseMode.HTML)


def echo_sticker(update, context):
    """callback function for sticker message handler"""
    context.bot.send_sticker(chat_id=update.effective_chat.id,
                             sticker=update.message.sticker.file_id)

def error(update,context):
    """callback function for error handler"""
    logger.error("Update '%s' caused error '%s'", update, context.error)

if __name__ == "__main__":

    url_for_webhook = "https://4f7e8f6e396a.ngrok.io/"
    bot = Bot(TOKEN)
    bot.set_webhook(url_for_webhook + TOKEN)

    dp = Dispatcher(bot,None)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", _help))
    dp.add_handler(CommandHandler("clubs", clubs))
    dp.add_handler(MessageHandler(Filters.text, dialogflow_connector))
    dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
    dp.add_handler(MessageHandler(Filters.location,location_handler))
    dp.add_handler(MessageHandler(Filters.voice, voice_to_text))
    dp.add_handler(MessageHandler(Filters.audio, voice_to_text))
    dp.add_error_handler(error)

    app.run(port=8443,debug=True)
