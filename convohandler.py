from telegram.ext import Updater,CommandHandler,MessageHandler,Filters, Dispatcher
from telegram.ext import CallbackQueryHandler,ConversationHandler,CallbackContext
from telegram import Bot,Update,ParseMode,InlineKeyboardButton, InlineKeyboardMarkup



urls = {
    "cse_circ": "http://www.iitmandi.ac.in/academics/files/btech_cse.pdf",
    "ee_circ": "http://www.iitmandi.ac.in/academics/files/btech_ee.pdf",
    "me_circ": "http://www.iitmandi.ac.in/academics/files/btech_mech.pdf",
    "ce_circ": "http://www.iitmandi.ac.in/academics/files/BTECH_CIVIL.pdf",
    "dse_circ": "http://iitmandi.ac.in/academics/files/B.TechinDataScience.pdf"
}


# Stages
FIRST, SECOND = range(2)
# Callback data
ONE, TWO, THREE, FOUR, FIVE=range(5)


def courses(update: Update, context: CallbackContext) -> None:
    """Send message on `/start`."""

    user = update.message.from_user
    # logger.info("User %s started the conversation.", user.first_name)

    keyboard = [[
        InlineKeyboardButton("CSE", callback_data=str(ONE)),
        InlineKeyboardButton("EE", callback_data=str(TWO)),
        InlineKeyboardButton("ME", callback_data=str(THREE)),
        InlineKeyboardButton("CE", callback_data=str(FOUR)),
        InlineKeyboardButton("DSE", callback_data=str(FIVE))
    ]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Select a branch", reply_markup=reply_markup)

    return FIRST

def admin(update: Update, context: CallbackContext) -> None:
    """Send message on `/start`."""

    user = update.message.from_user
    # logger.info("User %s started the conversation.", user.first_name)

    keyboard = [
        [
            InlineKeyboardButton("Karan Doshi", callback_data=str(ONE),url="https://t.me/karansdoshi"),
            InlineKeyboardButton("Tushar Goyal", callback_data=str(TWO),url="https://t.me/tushartg22"),
            InlineKeyboardButton("Prakhar Uniyal", callback_data=str(THREE),url="https://t.me/Prakhar_uniyal"),

        ]
        ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Feel free to contact any admin by clicking", reply_markup=reply_markup)

    return FIRST

def cs(update: Update, context: CallbackContext) -> None:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()

    context.bot.send_document(chat_id = update.effective_chat.id,document =urls["cse_circ"])
    query.edit_message_text(
         text="Choose an option"
    )
    return ConversationHandler.END


def ee(update: Update, context: CallbackContext) -> None:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    context.bot.send_document(chat_id=update.effective_chat.id,
                              document=urls["ee_circ"])



    query.edit_message_text(
        text="Choose an option"
    )
    return ConversationHandler.END


def me(update: Update, context: CallbackContext) -> None:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    context.bot.send_document(chat_id=update.effective_chat.id,
                              document=urls["me_circ"])

    query.edit_message_text(
        text="Choose an option"
    )
    return ConversationHandler.END


def ce(update: Update, context: CallbackContext) -> None:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    context.bot.send_document(chat_id=update.effective_chat.id,
                              document=urls["ce_circ"])

    query.edit_message_text(
        text="Choose an option"
    )
    return ConversationHandler.END


def dse(update: Update, context: CallbackContext) -> None:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    context.bot.send_document(chat_id=update.effective_chat.id,
                              document=urls["dse_circ"])

    query.edit_message_text(text="Choose an option")
    return ConversationHandler.END


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('courses', courses)],
    states={
        FIRST: [
            CallbackQueryHandler(cs, pattern='^' + str(ONE) + '$'),
            CallbackQueryHandler(ee, pattern='^' + str(TWO) + '$'),
            CallbackQueryHandler(me, pattern='^' + str(THREE) + '$'),
            CallbackQueryHandler(ce, pattern='^' + str(FOUR) + '$'),
            CallbackQueryHandler(dse, pattern='^' + str(FIVE) + '$'),
        ],
    },
    fallbacks=[CommandHandler('courses', courses)],
)