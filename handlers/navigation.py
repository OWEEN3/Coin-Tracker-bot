from telegram import Update
from telegram.ext import ContextTypes

from responses.response import BotResponses
from keyboards.main_menu import get_main_menu
from database.dao.users_dao import UsersDAO

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(BotResponses.START)
    
    chat_id = update.effective_user.id
    
    if not await UsersDAO.get_user(chat_id=chat_id):
        await UsersDAO.add_user(
            chat_id=chat_id
        )
    
    await update.message.reply_text(
        BotResponses.CHOSE, reply_markup=await get_main_menu()
    )

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(BotResponses.CHOSE, reply_markup=await get_main_menu())