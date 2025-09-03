from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, CallbackQueryHandler, CommandHandler, MessageHandler, filters

from handlers.navigation import cancel
from responses.response import BotResponses
from keyboards.main_menu import get_main_menu
from database.dao.tracking_dao import TrackingDAO
ASK_BASE, ASK_QUOTE = range(2)

async def add_tracked(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Enter the base currency (e.g., BTC):")
    return ASK_BASE

async def ask_base(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["base"] = update.message.text.upper()
    await update.message.reply_text("Enter the quote currency (e.g., USDT):")
    return ASK_QUOTE

async def ask_quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    symbol = context.user_data["base"] + update.message.text.upper()
    prices = context.application.bot_data.get("prices", {})
    price = prices.get(symbol)
    if price:
        await update.message.reply_text(f"{symbol}: {price} added to your watchlist!")
        await TrackingDAO.add(chat_id=update.effective_user.id, symbol=symbol)
    else:
        await update.message.reply_text(f"Not found. Let's try again.")
        await update.message.reply_text("Enter the base currency (e.g., BTC):")
        return ASK_BASE
    await update.message.reply_text(BotResponses.CHOSE, reply_markup=await get_main_menu())
    return ConversationHandler.END

add_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(add_tracked, pattern="^add_tracking$")],
    states={
        ASK_BASE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_base)],
        ASK_QUOTE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_quote)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
    per_message=False
)