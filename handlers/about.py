from telegram import Update
from telegram.ext import ContextTypes

from responses.response import BotResponses
from keyboards.main_menu import get_main_menu

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.edit_message_text(BotResponses.ABOUT)
    await context.bot.send_message(
        chat_id=update.effective_user.id, 
        text=BotResponses.CHOSE, 
        reply_markup=await get_main_menu()
    )