from telegram import Update
from telegram.ext import ContextTypes

from responses.response import BotResponses
from keyboards.main_menu import get_main_menu

async def my_watchlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = []
    if "tracked" in context.user_data:
        for symbol in context.user_data["tracked"]:
            text.append(f"{symbol}: {context.application.bot_data.get("prices", {}).get(symbol)}\n")
        await query.message.reply_text("".join(text))
    else: await query.message.reply_text("No coins to track")
    await query.message.reply_text(BotResponses.CHOSE, reply_markup=get_main_menu())