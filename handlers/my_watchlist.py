from telegram import Update
from telegram.ext import ContextTypes

from responses.response import BotResponses
from keyboards.main_menu import get_main_menu
from database.dao.tracking_dao import TrackingDAO

async def my_watchlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = []
    trackings = await TrackingDAO.get_user_tracking(
        chat_id=update.effective_user.id
    )
    if trackings:
        for tracking in trackings:
            text.append(
                f"{tracking.symbol}: {context.application.bot_data.get("prices", {}).get(tracking.symbol)}\n"
            )
        await query.message.reply_text("".join(text))
    else: await query.message.reply_text("No coins to track")
    await query.message.reply_text(BotResponses.CHOSE, reply_markup=await get_main_menu())