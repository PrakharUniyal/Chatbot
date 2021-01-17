import logging
from flask import Flask, request
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
from telegram import Bot, Update, ParseMode
from convohandler import conv_handler,admin
from utils.dialogflow import get_reply
from utils.firebase import dict_intents, answers_collection,userlogs_collection,users_collection
from utils.location import suggest_path
from utils.stackoverflow import doubtsearch, suggestion
from utils.speechrec import speech2text
import os
import numpy as np

from dotenv import load_dotenv
load_dotenv()

#enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

#Telegram Bot Token
TOKEN = os.getenv("TOKEN")

welcome_msg = """\n
<b>Congratulations!</b> for qualifying <u>JEE Advanced</u>\n  
This hard-earned laurel opens up for you the gateways of the IIT system where you can earn a BTech degree.
Welcome to IIT Mandi!, Beautiful Campus is worth the wait🙂\n
"""
campus_url = "https://i.ibb.co/8NbCyb9/campus.jpg"

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
    users_collection.document(author).set({"name":author})
    reply = "Hi! <b>{}</b>\n".format(author)
    reply += welcome_msg
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=campus_url,
                           caption=reply,
                           parse_mode=ParseMode.HTML)


def _help(update, context):
    help_text = """
• /courses: Know the course curriculum of various branches.\n
• /pathtoiitmandi: Find the best way to travel to IIT MANDI from your location.\n
• /programming_doubt: Get answers from stack overflow for your programming related doubts.\n
• /mess: Get the mess menu.\n
• /admin: Contact the administrators.\n
• /help: Get details of features of this bot.\n
    """
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=help_text,
                             parse_mode=ParseMode.HTML)

def _mess(update, context):
    context.bot.send_document(chat_id=update.effective_chat.id,
                              document=open("mess.pdf", 'rb'))


def location_handler(update, context):
    print("in location handler")
    # print(update)
    lat = update.message.location.latitude
    lng = update.message.location.longitude

    print(lat, lng)

    best_path = suggest_path(lat, lng)
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=best_path,
                             parse_mode=ParseMode.HTML)

def texthandler(update, context):

    response = get_reply(update.message.text, update.message.chat_id)
    intent = response.intent.display_name

    print("--------\n" ,response,"\nintent:->", intent, "\n--------")

    if (intent in dict_intents):
        intent_response = answers_collection.where('intent', '==',
                                                   intent).get()[0]
        reply_text = intent_response.get('text')
        # print(reply_text)
        imgrefs = intent_response.get('imgrefs')
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=reply_text,
                                 parse_mode=ParseMode.HTML)
        for imgref in imgrefs:
            context.bot.send_photo(chat_id=update.effective_chat.id,
                                   photo=imgref)

    else:
        if intent == "Default Fallback Intent":
            document = {
                "query": update.message.text,
                "username": update.message.from_user.first_name
            }
            userlogs_collection.add(document)

        elif not response.fulfillment_text:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Sorry, I'm still learning about this.",
                                     parse_mode=ParseMode.HTML)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=response.fulfillment_text,
                                 parse_mode=ParseMode.HTML)

def voice_to_text(update, context):

    chat_id = update.message.chat_id
    file_name = str(chat_id)
    update.message.voice.get_file().download(file_name + '.ogg')

    message_text = speech2text(file_name)
    print(message_text)
    update.message.text = message_text
    texthandler(update, context)


def echo_sticker(update, context):
    """callback function for sticker message handler"""
    context.bot.send_sticker(chat_id=update.effective_chat.id,
                             sticker=update.message.sticker.file_id)


def pathtoiitmandi(update, context):
    author = update.message.from_user.first_name
    help_text = "Hey {} ,Please share your live location through telegram\n".format(
        author)
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)


def error(update, context):
    """callback function for error handler"""
    logger.error("Update '%s' caused error '%s'", update, context.error)


def stacksearch(update, context):
    query = ' '.join(context.args)

    if query == "":
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=
            "Send your queries like: '/programming_doubt how to make a chatbot'"
        )
        return

    results = doubtsearch(query)
    reply = suggestion(results)

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=reply,
                             parse_mode=ParseMode.HTML)


if __name__ == "__main__":

    url_for_webhook = os.getenv("url_for_webhook")
    bot = Bot(TOKEN)

    try:
        bot.set_webhook(url_for_webhook + TOKEN)
    except Exception as e:
        print(e)

    dp = Dispatcher(bot, None)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", _help))
    dp.add_handler(CommandHandler("mess", _mess))
    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler("admin", admin))
    dp.add_handler(CommandHandler("pathtoiitmandi", pathtoiitmandi))
    dp.add_handler(CommandHandler("programming_doubt", stacksearch))
    dp.add_handler(MessageHandler(Filters.text, texthandler))
    dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
    dp.add_handler(MessageHandler(Filters.location, location_handler))
    dp.add_handler(MessageHandler(Filters.voice, voice_to_text))
    dp.add_handler(MessageHandler(Filters.audio, voice_to_text))
    dp.add_error_handler(error)

    bot.set_my_commands(
        [["courses", "Know the Branch curriculum"],
         [
             "pathtoiitmandi",
             "Best way to travel to IIT MANDI from your location"
         ],
         [
             "programming_doubt",
             "Search stackoverflow for programming related doubts"
         ], 
         ["mess", "Get mess menu"], 
         ["admin", "Contact admin"],
         ["help", "Guide to Bot"]])
    app.run(port=8443, debug=True)
