from telegram import Update
from telegram.ext import ContextTypes

from responses.response import BotResponses
from keyboards.main_menu import get_main_menu
from database.dao.users_dao import UsersDAO
from services.redis_dao import RedisDAO

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(BotResponses.START)
    
    chat_id = update.effective_user.id
    
    if not await UsersDAO.get_user(chat_id=chat_id):
        await UsersDAO.add_user(
            chat_id=chat_id
        )
    
    job_name = f"{chat_id}"
    jobs = context.application.job_queue.get_jobs_by_name(job_name)
    for job in jobs:
        job.schedule_removal()
    await RedisDAO.delete(key=chat_id)
    
    await update.message.reply_text(
        BotResponses.CHOSE, reply_markup=await get_main_menu()
    )

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(
            BotResponses.CHOSE, 
            reply_markup=await get_main_menu()
        )
        chat_id = update.effective_user.id
        job_name = f"{chat_id}"
        jobs = context.application.job_queue.get_jobs_by_name(job_name)
        for job in jobs:
            job.schedule_removal()
        await RedisDAO.delete(key=chat_id)
    elif update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(
            BotResponses.CHOSE,
            reply_markup=await get_main_menu()
        )
    else:
        pass