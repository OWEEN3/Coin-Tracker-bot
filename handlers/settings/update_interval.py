from telegram import Update
from telegram.ext import ConversationHandler, CallbackQueryHandler, ContextTypes, CommandHandler, MessageHandler, filters

from handlers.navigation import cancel
from database.dao.users_dao import UsersDAO
from responses.response import BotResponses
from keyboards.settings_menu import get_settings_menu
ASK_TIME = range(1)

async def start_edit_update_interval(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Enter the update interval in seconds (minimum 60):")
    return ASK_TIME

async def ask_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try :
        interval = int(update.message.text)
        if interval < 60:
            await update.message.reply_text("The interval must be at least 60 seconds. Please re-enter:")
            return ASK_TIME
        await UsersDAO.edit_update_interval(
            chat_id=update._effective_user.id,
            update_interval=interval
        )
        await update.message.reply_text(BotResponses.CHOSE, reply_markup=await get_settings_menu(update))
        return ConversationHandler.END
    except:
        await update.message.reply_text("Incorrect interval. Please re-enter:")
        return ASK_TIME
    

conv_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(start_edit_update_interval, pattern="^set_update_interval$")],
    states={
        ASK_TIME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_time)]
    },
    fallbacks=[CommandHandler("cancel", cancel)]
)