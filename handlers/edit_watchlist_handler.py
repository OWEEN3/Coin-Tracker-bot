from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, CallbackQueryHandler, CommandHandler, MessageHandler, filters
from handlers.navigation import cancel
from responses.response import BotResponses
from keyboards.main_menu import get_main_menu
ASK_BASE, ASK_QUOTE = range(2)

async def start_edit_tracked(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("Enter the base currency (e.g., BTC):")
    return ASK_BASE

async def ask_base(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["base"] = update.message.text.upper()
    await update.message.reply_text("Enter the quote currency (e.g., USDT):")
    return ASK_QUOTE

async def ask_quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    symbol = context.user_data["base"] + update.message.text.upper()
    prices = context.application.bot_data.get("prices", {})
    price = prices.get(symbol)
    print(price)
    if price:
        await update.message.reply_text(f"{symbol}: {price} added to your watchlist!")
        if "tracked" not in context.user_data:
            context.user_data["tracked"] = []
        if symbol not in context.user_data["tracked"]:
            context.user_data["tracked"].append(symbol)
    else:
        await update.message.reply_text(f"Not found. Let's try again.")
        await update.message.reply_text("Enter the base currency (e.g., BTC):")
        return ASK_BASE
    await update.message.reply_text(BotResponses.CHOSE, reply_markup=await get_main_menu())
    return ConversationHandler.END

conv_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(start_edit_tracked, pattern="^edit_watchlist$")],
    states={
        ASK_BASE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_base)],
        ASK_QUOTE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_quote)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
    per_message=False
)