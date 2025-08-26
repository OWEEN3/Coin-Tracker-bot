from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

from config import settings
from response import BotResponses

def get_main_menu():
    keyboard = [
        [InlineKeyboardButton("📊 My tracking", callback_data="my_watchlist")],
        [InlineKeyboardButton("➕ Edit tracked", callback_data="edit_watchlist")],
        [InlineKeyboardButton("⚙️ Settings", callback_data="settings")],
        [InlineKeyboardButton("ℹ️ about", callback_data="about")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(BotResponses.START)
    await update.message.reply_text(BotResponses.CHOSE, reply_markup=get_main_menu())

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    chat_id = query.message.chat_id
    
    if query.data == "my_watchlist":
        await context.bot.send_message(chat_id=chat_id, text="my_watchlist")
        await context.bot.send_message(chat_id=chat_id, text=BotResponses.CHOSE, reply_markup=get_main_menu())
    elif query.data == "edit_watchlist":
        await context.bot.send_message(chat_id=chat_id, text="edit_watchlist")
        await context.bot.send_message(chat_id=chat_id, text=BotResponses.CHOSE, reply_markup=get_main_menu())
    elif query.data == "settings":
        await context.bot.send_message(chat_id=chat_id, text="settings")
        await context.bot.send_message(chat_id=chat_id, text=BotResponses.CHOSE, reply_markup=get_main_menu())
    elif query.data == "about":
        await context.bot.send_message(chat_id=chat_id, text="about")
        await context.bot.send_message(chat_id=chat_id, text=BotResponses.CHOSE, reply_markup=get_main_menu())
    
def main():
    app = Application.builder().token(settings.get_token).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()