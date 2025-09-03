from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import json

from database.dao.tracking_dao import TrackingDAO
from database.dao.users_dao import UsersDAO
from services.redis_dao import RedisDAO
from handlers.my_watchlist.watchlist_updater import update_watchlist_job

async def my_watchlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user = await UsersDAO.get_user(chat_id=update.effective_user.id)
    text = []
    trackings = await TrackingDAO.get_user_tracking(
        chat_id=update.effective_user.id
    )
    if trackings:
        trackings_list = []
        for tracking in trackings:
            price = context.application.bot_data.get("prices", {}).get(tracking.symbol, "N/A")
            text.append(f"{tracking.symbol}: {price}\n")
            trackings_list.append(tracking.symbol)
        msg = await query.edit_message_text(
            text="".join(text),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text="⬅️ Back", callback_data="back_watchlist")]
            ])
        )
        if user.notification_status == "on":
            await RedisDAO.set(key=user.chat_id, value=json.dumps(trackings_list))
            context.application.job_queue.run_repeating(
                update_watchlist_job,
                interval=user.notification_interval,
                first=user.notification_interval,
                name=str(user.chat_id),
                data = {"chat_id": user.chat_id, "message_id": msg.message_id, "type": user.notification_type}
            )
    else: await query.edit_message_text("No coins to track", reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text="⬅️ Back", callback_data="back_watchlist")]
            ]))