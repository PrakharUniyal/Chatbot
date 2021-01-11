import logging
from flask import Flask, request
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters, Dispatcher
from telegram import ReplyKeyboardMarkup,Bot,Update,ParseMode
from utils import get_reply
​
​
#enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
​
​
#Telegram Bot Token
TOKEN = "1474907865:AAGqLgIV9keqdeeUVWNwO2svN2uFqx-kwLs" #stresstest_bot
# TOKEN = "1531582165:AAHNtmQ4lyWZ55Rkf0Hs9KxzcB0woGGeX0E" #iitmandi_bot
# TOKEN="1546162713:AAEnv2MvukJma18_GuVqCF92NUaFYITwlBc" #KDbot
​
imageurls = {
        "campus": "https://i.ibb.co/8NbCyb9/campus.jpg",
        "tripleroom_url" : "https://scontent.fpnq4-1.fna.fbcdn.net/v/t1.0-9/122140166_815645489197544_8328917430186400303_o.jpg?_nc_cat=111&ccb=2&_nc_sid=dbeb18&_nc_ohc=_qjpA4PQQCoAX9sLkGC&_nc_oc=AQkOWMHtD18797KPIq3SchTfFDnk2x4r-r1UwXiNeFDS1J12HwhL90DjzzmoKLktkz8&_nc_ht=scontent.fpnq4-1.fna&oh=800ac0b364d58711717baeaa4b4bfc24&oe=60219B0C",
        "doubleroom_url" : "https://scontent.fpnq4-1.fna.fbcdn.net/v/t1.0-9/122107179_3351982168247612_3874733656374962850_o.jpg?_nc_cat=111&ccb=2&_nc_sid=dbeb18&_nc_ohc=6K758cHE_JgAX_ZLsh3&_nc_ht=scontent.fpnq4-1.fna&oh=22e78e68d3b474f0894c1caab5264403&oe=60209BBC",
        "mess_url" : "https://scontent.fpnq4-1.fna.fbcdn.net/v/t1.0-9/122370919_2289019017911512_7022478130559725125_o.jpg?_nc_cat=100&ccb=2&_nc_sid=dbeb18&_nc_ohc=IRLhvHpHRY0AX8TOQ1J&_nc_ht=scontent.fpnq4-1.fna&oh=38da5aa0e4db37b35987e70fee6356f7&oe=601FFFB2"
}
​
​
topics_keyboard = [
    ['Programming Club', 'Heuristics Club'],
    ['Robotronics Club', 'Space Technology and Astronomy Cell', 'Yantrik Club'],
    ['Entrepreneurship Cell', 'Nirmaan Club', 'Literary Society']
]
​
​
dict_intents = {
    "branchchange.prospects":[
"""
<b>Branch change</b> depends solely on your CGPA (Cumulative Grade Point Average)
for the first two semesters. For a more details kindly have a   <a href="http://iitmandi.ac.in/academics/branch_change.php"> refer </a> this
Everything is relative and dependent on your batch's performance. Although, if you study diligently (not compromising on the extra-curriculars), I believe you are good to go
- If you attend all your classes diligently, and solve the assignments, etc. you would be able to get a cgpa above 8. Keep in mind that there is relative grading in most courses, and other students will also be working hard to get a nice cgpa. In the end it depends on your hardwork.
- IIT Mandi offers a liberal branch change policy which allows you to study a branch of your interest. But always be prepared for the branch that you are getting.
"""
],
    
    "branchchange.criteria": [
        """
        8.3 for cse
        """
    ],
​
​
    "hostel.rooms": ["Hostels have rooms of different sizes, single, double and triple occupancy. First "
                    "year students usually get a shared room.In the subsequent years, you may get a single room."
                    "There is a common washroom for the whole floor",imageurls["tripleroom_url"]  ,imageurls["doubleroom_url"]],
​
    "hostel.carry": ["Daily use things , A laptop etc . If you forget any thing various shops are available here"],
    "hostel.facilities":["Facilities at hostel include a study room with a heater,common room or TV room for watching TV "
                        "and playing table tennis or for group activities.You also get a microwave,electric kettle ,refrigerator on "
                        "each floor and also shared laundry with several washing machines and dryers"],
    "hostel.life":[
​
"""
The hostels at  <b> IIT Mandi </b> are some of the best hostels you can find in the country. The hostels are equipped with:\n
<u>Hostels are alloted Randomly to freshers and sharing room is there in first year , 2 - 3 students in one room</u> \n
​
<b>Yaar baaki saare city wale colleges to aise hi hote hain, kya padhe kya nahi padhe sab bhool jaenge.Lekin iss jagah ko nhi bhool paenge, ye jagah bahut hi faad hain, aur sabse alag hain!\n</b>
<a href="https://gymkhana.iitmandi.co.in/hostel.html">Visit</a> 
""" 
],
​
    "campus.transportation":["We have regular buses running between the North campus and South campus every 15 minutes "
                            "and buses from college to Mandi every hour.We have a bus stop in the north campus "
                            "near the A10 building and in the south campus near the CV Raman canteen"],
    "campus.mess":["We have several messes in our campus D1,D2 in the south campus and Pine,Oak in the North Campus."
                   "The mess food is also good",imageurls["mess_url"]],
    "fees":[
"""
https://iitmandi.ac.in/academics/fees.php
"""
    ],
    "document":[
        """
        bring 10th,12th certificates
        """
​
    ],
    "fees.waiver": [
        """
        fees waiver
        """
    ],
    "sports":[
        """
        A: Sports activities are coordinated by the Principal Sports Officer and the Faculty
Sports Advisor. A team of highly experienced coaches and ground staff work under
their direction to help you take part in the games of your choice. Participate in various
tournaments like Inter-IIT, Aagaaz, Rann-Neeti and other in-house tournaments.
At Kamand, we have fields for Cricket, Football and Hockey, Basketball, Tennis,
Squash, Badminton, TT and Volleyball courts. TT and Foosball tables are also
available in most hostels. There is also Swimming pool, gym and yoga room etc.
        """
    ],
    "programming.development":[
    """
    GSOC ROCKS
    """
    ],
    "programming.culture":[
        """
        Coding culture is good
        """
    ],
    "programming.compi": [
        """
        DSA karo bhaiyo
        """
    ],
    "programming.os": [
        """
        Use linux over windows
        """
    ],
    "programming.laptop": [
        """
        Mackbook lele
        """
    ],
    "ragging":[
        """
        Zero Tolerance for ragging. We have the following committees to take care of
any issues, Student Welfare and Disciplinary Committee (SWDC), Anti-Ragging
Committee (ARC).
        """
    ],
    "library":[
        """
         In general, you can get the e-books for the materials that the teacher specifies.
Also, you can get them from the library, though the library may have only limited
copies. Local bookshops in Mandi or online stores are also of help, so are the
seniors. Moodle web pages on our intranet site have all the course materials posted
by faculty and students
        """
    ],
    "placements":
    [
        """
        placements are excellent
        """
    ],
    "academics.workingdays":
    [
        """
        Usually we do not have classes on saturdays and sundays but sometimes holidays in the middle of the week are compensated by shifting that day's time table schedule to a weekend day.
        """
    ],
    "academics.companycg":
    [
        """
        CGPA criteria for placement/internship varies from company to company. An ideal CGPA to have is 8.5 or greater.\n
        Most of the companies allow for a CGPA greater than 8.
        """
    ],
    "academics.companycg":
    [
        """
        CGPA criteria for placement/internship varies from company to company. An ideal CGPA to have is 8.5 or greater.\n
        Most of the companies allow for a CGPA greater than 8.
        """
    ],
    "academics.professors":
    [
        """
        It varies from professor to professor. Some are of very good nature and empathetic but some are a bit orthodox and expect a lot from their students.
        """
    ],
    "academics.exams":
    [
        """
        Grading pattern varies across courses.\n
        But most of the courses including the ones in first year have 2 quizzes and one end-sem examination along with some weightage for assignments/practicals/mini-projects.
        """
    ],
    "academics.stationery":
    [
        """
        You don't need to buy any books or other stationery related to your courses.\n
        We have a huge collection at the library which is sufficient for all the students of a course.\n
        You can also find PDF version of books available on the internet.\n
        Other stationery items can easily be purchased at the local store or ordered online.
        """
    ],
    "academics.stationery":
    [
        """
        You don't need to buy any books or other stationery related to your courses.\n
        We have a huge collection at the library which is sufficient for all the students of a course.\n
        You can also find PDF version of books available on the internet.\n
        Other stationery items can easily be purchased at the local store or ordered online.
        """
    ],
    "academics.studying":
    [
        """
        It depend on the person. But combining classes, assignments, quizzes and tests it takes around 50-55 hours every week.
        """
    ],
}
​
welcome_msg = "Welcome to IIT Mandi!, Beautiful Campus is worth the wait🙂\n"
​
​
app = Flask(__name__)
​
@app.route('/')
def index():
    return "Hello!"
​
​
@app.route(f'/{TOKEN}', methods=['GET', 'POST'])
def webhook():
    """webhook view which receives updates from telegram"""
    # create update object from json-format request data
    update = Update.de_json(request.get_json(), bot)
    # process update
    dp.process_update(update)
    return "ok"
​
def start(update, context):
    print(update)
    author = update.message.from_user.first_name
    reply = "Hi! <b>{}</b>\n".format(author)
    reply+= welcome_msg
    context.bot.send_photo(chat_id = update.effective_chat.id, 
                        photo=imageurls["campus"],caption=reply,parse_mode=ParseMode.HTML)
​
def clubs(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Choose Club/Society",
        reply_markup=ReplyKeyboardMarkup(keyboard=topics_keyboard, one_time_keyboard=True))
​
def _help(update,context):
    help_text = "Hey! This is a help text"
    context.bot.send_message(chat_id = update.effective_chat.id,text = help_text)
​
def location_handler(update,context):
    print(update)
    chandi = np.array((30.741482, 76.768066))
    delhi = np.array((28.644800, 77.216721))
    mumbai = np.array((19.076090, 72.877426))
    user = np.array((update.message.location.latitude, update.message.location.longitude))
    print(user)
​
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
​
​
def dialogflow_connector(update,context):
    
    response = get_reply(update.message.text, update.message.chat_id)
    intent=response.intent.display_name
    
    print("--------")
    print(response)
    print("intent:->", intent)
    print("--------")
​
    if(intent in dict_intents):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text= dict_intents[intent][0],
                                 parse_mode=ParseMode.HTML)
        try:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=dict_intents[intent][1])
        except:
            print("no image")
​
        try:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=dict_intents[intent][2])
        except:
            print("no image")
​
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=response.fulfillment_text,
                                 parse_mode=ParseMode.HTML)
    
def echo_sticker(update,context):
    """callback function for sticker message handler"""
    context.bot.send_sticker(chat_id=update.effective_chat.id,
                     sticker=update.message.sticker.file_id)
​
def error(update,context):
    """callback function for error handler"""
    logger.error("Update '%s' caused error '%s'", update, context.error)
​
if __name__ == "__main__":
​
    url_for_webhook = "https://6df0f97fc317.ngrok.io/"
    bot = Bot(TOKEN)
    bot.set_webhook(url_for_webhook + TOKEN)
​
    dp = Dispatcher(bot,None)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", _help))
    dp.add_handler(CommandHandler("clubs", clubs))
    dp.add_handler(MessageHandler(Filters.text, dialogflow_connector))
    dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
    dp.add_handler(MessageHandler(Filters.location,location_handler))
    dp.add_error_handler(error)
​
    app.run(port=8443,debug=True)
Collapse

