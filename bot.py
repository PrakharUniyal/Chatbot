import logging
from flask import Flask, request
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters, Dispatcher
from telegram import ReplyKeyboardMarkup,Bot,Update,ParseMode
from utils import get_reply


#enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


#Telegram Bot Token
TOKEN = "1474907865:AAGqLgIV9keqdeeUVWNwO2svN2uFqx-kwLs" #stresstest_bot
# TOKEN = "1531582165:AAHNtmQ4lyWZ55Rkf0Hs9KxzcB0woGGeX0E" #iitmandi_bot
# TOKEN="1546162713:AAEnv2MvukJma18_GuVqCF92NUaFYITwlBc" #KDbot

imageurls = {
        "campus": "https://i.ibb.co/8NbCyb9/campus.jpg"

}


topics_keyboard = [
    ['Programming Club', 'Heuristics Club'],
    ['Robotronics Club', 'Space Technology and Astronomy Cell', 'Yantrik Club'],
    ['Entrepreneurship Cell', 'Nirmaan Club', 'Literary Society']
]


dict_intents = {
    "branchchange.prospects":

"""
<b>Branch change</b> depends solely on your CGPA (Cumulative Grade Point Average)for the first two semesters. For more details <a href="http://iitmandi.ac.in/academics/branch_change.php"> refer </a> this\n
• Everything is relative and dependent on your batch's performance. Although, if you study diligently (not compromising on the extra-curriculars), I believe you are good to go\n
• If you attend all your classes diligently, and solve the assignments, etc. you would be able to get a cgpa above 8. Keep in mind that there is relative grading in most courses, and other students will also be working hard to get a nice cgpa. In the end it depends on your hardwork.\n
• IIT Mandi offers a liberal branch change policy which allows you to study a branch of your interest. But always be prepared for the branch that you are getting.\n
""",

    "branchchange.criteria": "Kaafi asaan hai Ho jaayegi\n",

    "hostel.rooms": 
    
"""
Hostels have rooms of different sizes, single, double and triple occupancy.\n
First year students usually get a shared room.There is a common washroom for the whole floor\n
""",

    "hostel.carry": "Daily use things , A laptop etc . If you forget any thing various shops are available here",

    "hostel.facilities":
"""Facilities at hostel include a study room with a heater,common room or TV room for watching TV and playing table tennis or for group acitivites.\n
•You also get a microwave,electric kettle on each floor\n
"""
}

welcome_msg = "Welcome to IIT Mandi!, Beautiful Campus is worth the wait🙂\n"


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
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text= dict_intents[intent],
                                 parse_mode=ParseMode.HTML)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=response.fulfillment_text,
                                 parse_mode=ParseMode.HTML)
    
def echo_sticker(update,context):
    """callback function for sticker message handler"""
    context.bot.send_sticker(chat_id=update.effective_chat.id,
                     sticker=update.message.sticker.file_id)

def error(update,context):
    """callback function for error handler"""
    logger.error("Update '%s' caused error '%s'", update, context.error)

if __name__ == "__main__":

    url_for_webhook = "https://a25cbfaef850.ngrok.io/"
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

    app.run(port=8443,debug=True)