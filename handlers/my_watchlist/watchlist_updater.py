import json
from datetime import datetime, timezone

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from services.redis_dao import RedisDAO
from responses.response import BotResponses
from handlers.navigation import get_main_menu

async def update_watchlist_job(context: CallbackContext):
    job_data = context.job.data
    chat_id = job_data["chat_id"]
    message_id = job_data["message_id"]
    update_type = job_data["type"]
    try:
        trackings = json.loads(await RedisDAO.get(key=chat_id))
        text = []
        for tracking in trackings:
            price = context.bot_data.get("prices", {}).get(tracking, {"N/A"})
            text.append(f"{tracking}: {price}\n")
        text.append(f"Updated at: {datetime.now(timezone.utc).strftime("%H:%M:%S")}")
        if update_type == "update_message":
            await context.bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="".join(text),
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text="⬅️ Back", callback_data="back_watchlist")]
                ])
            )
        else: await context.bot.send_message(
            chat_id=chat_id,
            text="".join(text),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text="⬅️ Back", callback_data="back_watchlist")]
            ])
        )
    except:
        await context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="No coins to track"
        )
        
async def watchlist_exit(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    user_id = update.effective_user.id
    job_name = f"{user_id}"
    jobs = context.application.job_queue.get_jobs_by_name(job_name)
    for job in jobs:
        job.schedule_removal()
    await RedisDAO.delete(key=user_id)
    
    await query.edit_message_text(
        BotResponses.CHOSE,
        reply_markup=await get_main_menu()
    )